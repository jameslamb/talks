# httr-talk

#### Contents

* [HTTP Basics](#http-basics)
    - [Request](#request)
    - [Response](#response)
* [JSON Basics](#json-basics)
* [R Examples](#r-examples)

## HTTP Basics

This is a lightweight introduction to HTTP. For moore, see [Mozilla's excellent docs](https://developer.mozilla.org/en-US/docs/Web/HTTP).

[HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) stands for "Hypertext Transfer Protocol". A **protocol** defines how two computers send information to each other.

Those computers get names based on their role in the protocol:

* "client": wants something
* "server": gives the client that thing if the client comes correct

The client asks the server to do something by sending a "request", and the server sends back a "response" describing what was / was not done.

### Request

A `request` has a few components.

* `URL`: Uniform Resource Locator, basically an address to find the server
    - this is often a human-readable name like `https://api.github.com`, and the details of how that gets turned into the address of the "server" are outside the scope of this doc
* `method`: tells the server what "type" or request you are sending
    - here are slightly-oversimplified descriptions of the main ones:
        - `DELETE`: client wants the server to remove something
        - `GET`: client wants the server to send it something
        - `PATCH`: client wants to change something on the server
        - `POST`: client wants the server to create something, unless it already exists
        - `PUT`: clients wants the server to create something, and overwrite it if it already exists
* `headers`: additional context the server might need to do the right thing with the request
    - for example, `{"Accept": "application/text"}` says *"hey server, I am sending you a text file, not something like an image or audio file"*

There is a bunch of other stuff involved in the protocol but if you get those three things you can accomplish a lot.

### Response

A `response` has the following important components.

* `status code`: a number that tells the client if the request was successful or not
    - There are a lot of ways a request could succeed or fail, and each has its own status code. A few common ones:
        - `2xx`: success! client asked and server did the thing.
            - **200**: totally successful
            - **201**: successful, and the server created something
        - `3xx`: the server doesn't live at this `URL` anymore, but your request made it to the new place
            - **301**: the server has moved, and the client should re-send the request to that new place
        - `4xx`: failure! server got and understood request, but can't or won't do what client wants
            - **400**: server doesn't understand what the client wants
            - **401**: server can't tell if the client is allowed to ask for what it's asking for
            - **403**: client is definitely not allowed to ask for what it's asking for
            - **404**: thing the client wants doesn't exist
            - **408**: server has been trying to do what the client wants but it's taking too long, so the server wants to quit
        - `5xx`: failure! server is unable to receive requests or broke while trying to do what the client wanted
            - **500**: server started doing what the client wanted, but then something broke
            - **503**: server isn't able to take any requests right now
* `body`: data the client asked for (if the client asked for something back)
    - this might be something like an image file or text for a website

## JSON Basics

As mentioned above, sometimes the server sends the client a "body" containing some data. It's common for that body to be a text file with information stored in Javascript Object Notation ([JSON](https://en.wikipedia.org/wiki/JSON)).

It looks something like this.

```javascript
{
    "username": "jameslamb",
    "profile_public": true,
    "media": {
        "profile_picture": "profile.png"
    },
    "notifications": {
        "num_bells": 1,
        "num_messages": 1,
        "notifications": [
            {"type": "direct-message", "preview": "Emily sent you a message", "url": "https://twitter.com/messages/917780412134457344"},
            {"type": "like", "preview": "Edward liked your tweet", "url": "https://twitter.com/LilNasX/status/1248356745816109056"}
        ]
    },
    "timeline": [
        "https://twitter.com/Corey_Yanofsky/status/1248110948122013696",
        "https://twitter.com/_ColinFay/status/1245458045376892930",
        "https://twitter.com/Chas10Buttigieg/status/1243975360800346113"
    ]
}
```

The spec has a standard way to organize collections of data. Each thing in `{}` is a map, with "keys" as strings. Because this can be arbitrarily nested (you can have maps of maps of maps of ...), it is best represented by a named list in R. The data above roughly maps to this R object.

```r
social_profile <- list(
    "username" = "jameslamb"
    , "profile_public" = TRUE
    , "media" = list(
        "profile_picture" = "profile.png"
    )
    , "notificationos" = list(
        "num_bells" = 1
        , "num_messages" = 1
        , "notifications" = list(
            list("type" = "direct-message", "preview" = "Emily sent you a message", "url" = "https://twitter.com/messages/917780412134457344")
            , list("type" = "like", "preview" = "Edward liked your tweet", "url" = "https://twitter.com/LilNasX/status/1248356745816109056")
        )
    )
    , "timelines" = c(
        "https://twitter.com/Corey_Yanofsky/status/1248110948122013696",
        "https://twitter.com/_ColinFay/status/1245458045376892930",
        "https://twitter.com/Chas10Buttigieg/status/1243975360800346113"
    )
)
```

My favorite R package for taking JSON text and turning it into an R object is `jsonlite`. It has very few dependencies, is fast, and is reasonably easy to use.

## HTTTP in R with `httr`

My favorite R package for making HTTP requests is `httr`. You can learn more about it [in the vignetttets](https://cran.r-project.org/web/packages/httr/index.html).

`httr` is awesome for writing *clients*. Recall that clients make `requests`.

```r
response <- httr::GET(
    url = "api.github.com/repos/jayqi/spongebob"
)
```

This response has a `status code`

```r
httr::status_code(response)
```

> [1] 200

and it has a `body`, in this case some details about a repo stored in JSON.

```r
cat(httr::content(response, as = "text"))
```

> {
  "id": 162783634,
  "node_id": "MDEwOlJlcG9zaXRvcnkxNjI3ODM2MzQ=",
  "name": "spongebob",
  "full_name": "jayqi/spongebob",
  "private": false,
  "owner": {
    "login": "jayqi",

The body is just a string, but it can be converted into an R list witth `jsonlite::fromJSON()`.

```r
response_list <- jsonlite::fromJSON(
    httr::content(response, as = "txt")
    , simplifyVector = FALSE
    , simplifyDataFrame = FALSE
)
str(response_list, max.levl = 1)
```

> List of 76
 $ id               : int 162783634
 $ node_id          : chr "MDEwOlJlcG9zaXRvcnkxNjI3ODM2MzQ="
 $ name             : chr "spongebob"
 $ full_name        : chr "jayqi/spongebob"
 $ private          : logi FALSE
 $ owner            :List of 18
 $ html_url         : chr "https://github.com/jayqi/spongebob"
 $ description      : chr "spongebob : SPoNgeBOb-CAse cONveRSioN iN R"
 $ fork             : logi FALSE
