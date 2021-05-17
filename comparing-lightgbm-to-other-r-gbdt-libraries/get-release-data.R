library(data.table)
library(httr)
library(jsonlite)

.get_json <- function(url_str){
    gh_token <- Sys.getenv("GITHUB_TOKEN")
    if (gh_token == "") {
        stop("environment variable GITHUB_TOKEN must be set")
    }
    res <- httr::RETRY(
        verb = "GET"
        , url = url_str
        , times = 3
        , terminate_on = c(401, 403, 404)
        , httr::add_headers(c(
            "Accept" = "application/vnd.github.v3+json"
            , "Authorization" = sprintf("Bearer %s", Sys.getenv("GITHUB_TOKEN"))
        ))
    )
    httr::stop_for_status(res, task = sprintf("fetch %s", url_str))
    return(jsonlite::fromJSON(
        txt = httr::content(res, as = "text")
        , simplifyVector = FALSE
        , simplifyDataFrame = FALSE
        , simplifyMatrix = FALSE
        , flatten = FALSE
    ))
}

.get_release_date <- function(release_json) {
    commit_url <- release_json[["commit"]][["url"]]
    json_data <- .get_json(commit_url)
    release_date_str <- json_data[["commit"]][["committer"]][["date"]]
    return(as.POSIXct(release_date_str, tz = "UTC"))
}

get_releases <- function(org, repo_name) {
    gh_url <- sprintf(
        "https://api.github.com/repos/%s/%s/tags?per_page=200"
        , org
        , repo_name
    )
    json_data <- .get_json(gh_url)
    print(sprintf("Found %d releases for %s/%s", length(json_data), org, repo_name))
    out <- lapply(
        X = json_data
        , FUN = function(release_json) {
            return(list(
                tag = release_json[["name"]]
                , release_date = .get_release_date(release_json)
            ))
        }
    )
    return(out)
}

catboost_data <- get_releases(
    org = "catboost"
    , repo_name = "catboost"
)
catboostDT <- data.table::rbindlist(catboost_data)
catboostDT[, project := "catboost"]
catboostDT <- catboostDT[tag != "commit"]

lightgbm_data <- get_releases(
    org = "microsoft"
    , repo_name = "LightGBM"
)
lightgbmDT <- data.table::rbindlist(lightgbm_data)
lightgbmDT[, project := "lightgbm"]
lightgbmDT <- lightgbmDT[tag != "stable"]

xgboost_data <- get_releases(
    org = "dmlc"
    , repo_name = "xgboost"
)
xgboostDT <- data.table::rbindlist(xgboost_data)
xgboostDT[, project := "xgboost"]

releaseDT <- data.table::rbindlist(
    l = list(catboostDT, lightgbmDT, xgboostDT)
    , fill = TRUE
)
releaseDT[, year := as.integer(format(release_date, "%Y"))]

data.table::setorderv(releaseDT, cols = c("project", "release_date"))
releaseDT[
    , days_since_last_release := as.integer(
        difftime(
            time1 = release_date
            , time2 = data.table::shift(release_date, n = 1, type = "lag")
            , units = "d"
        )
    )
    , by = project
]

print("First release")
releaseDT[, min(release_date), by = project]

print("median time between releases (days)")

releaseDT[, median(days_since_last_release, na.rm = TRUE), by = project]

print("median time between releases, since January 2019")

releaseDT[year >= 2019, median(days_since_last_release, na.rm = TRUE), by = project]
