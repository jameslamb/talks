library(lintr)

DIR_TO_LINT <- "sample-r-code"

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


lintr::lint_dir(
    path = DIR_TO_LINT
    , linters = LINTERS_TO_USE
)

