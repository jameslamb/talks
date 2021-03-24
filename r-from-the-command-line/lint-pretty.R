#!/usr/bin/env Rscript

library(argparse)
library(lintr)
library(spongebob)

.VERSION <- "0.0.1"

parser <- argparse::ArgumentParser(
    description = "Lint R code with {lintr}"
)
parser$add_argument(
    "--dir-to-lint"
    , type = "character"
    , help = "Directory to lint"
)
parser$add_argument(
   "--version"
   , action = "store_true"
   , help = "Print the version of this linting tool."
)

# Grab args (store in constants for easier debugging)
args <- parser$parse_args()
DIR_TO_LINT <- args[["dir_to_lint"]]

# print version and exit early if --version was passed
if (isTRUE(args[["version"]])){
    cat(paste0(.VERSION, "\n"))
    quit(save = "no", status = 0)
}

cat(crayon::yellow(
    spongebob::spongebobsay(
        what = "linting is important"
        , print = FALSE
    )
))

cat("\n\n")

LINTERS_TO_USE <- list(
    "absolute_path"          = lintr::absolute_path_linter
    , "assignment"           = lintr::assignment_linter
    , "closed_curly"         = lintr::closed_curly_linter
    , "commas"               = lintr::commas_linter
    , "equals_na"            = lintr::equals_na_linter
    , "function_left"        = lintr::function_left_parentheses_linter
    , "implicit_integers"    = lintr::implicit_integer_linter
    , "infix_spaces"         = lintr::infix_spaces_linter
    , "long_lines"           = lintr::line_length_linter(length = 120L)
    , "no_tabs"              = lintr::no_tab_linter
    , "non_portable_path"    = lintr::nonportable_path_linter
    , "open_curly"           = lintr::open_curly_linter
    , "paren_brace_linter"   = lintr::paren_brace_linter
    , "semicolon"            = lintr::semicolon_terminator_linter
    , "seq"                  = lintr::seq_linter
    , "single_quotes"        = lintr::single_quotes_linter
    , "spaces_inside"        = lintr::spaces_inside_linter
    , "spaces_left_parens"   = lintr::spaces_left_parentheses_linter
    , "todo_comments"        = lintr::todo_comment_linter(c("todo", "fixme", "to-do"))
    , "trailing_blank"       = lintr::trailing_blank_lines_linter
    , "trailing_white"       = lintr::trailing_whitespace_linter
    , "true_false"           = lintr::T_and_F_symbol_linter
    , "unneeded_concatenation" = lintr::unneeded_concatenation_linter
)

issues <- lintr::lint_dir(
    path = DIR_TO_LINT
    , linters = LINTERS_TO_USE
)
num_issues <- length(issues)

print(issues)

header_txt <- sprintf(
    "\n---------- %i issues found ----------\n"
    , num_issues
)
if (num_issues == 0) {
    cat(crayon::green(header_txt))
} else {
    cat(crayon::red(header_txt))
}

quit(save = "no", status = num_issues)
