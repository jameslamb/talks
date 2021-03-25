# R from the Command Line

This document contains notes and examples for use with the talk "R from the Command Line".

## Core Concepts

### Input and Output Streams

Processes read data from a stream called `stdin`, and then can optionally write data to **stdout** or **stderr**.

In the example below, the contents of `README.md` is read in to `cat`'s **stdin**, then written out to `cat`'s **stdout**.

```shell
cat < README.md
```

These output streams can be connected to each other. One processes `stdout` can be come another's `stdin`. In the example below, `cat`'s **stdout** is redirected to `wc`,  which then produces a count of lines in `README.md` on its own **stdout**

```shell
cat < README.md | wc -l
```

`stdout` is typically used for diagnostic messages or for the expected output of a process. `stderr` is usually reserved for warnings or error messages.

```shell
ls some-garbage
```

> ls: some-garbage: No such file or directory

Output streams can also be redirected to a file. The code below reads in `README.md`, then passes it through `grep` to search for lines that start with `#`, then writes them to a file.

```shell
cat < README.md | grep -E '^#' > out.txt
```

### Exit Codes

Processes return an integer status called an "exit code".

```shell
# this should succeed and return 0
ls
echo "exit code: $?"

# this will return a non-0 code
ls some-garbage
echo "exit code: $?"
```

### Customizing Programs

Every process has access to a set of environment variables. You can see them with `env`.

```shell
env
```

Some programs will have code in them that reads configuration values from these environment variables.

Try setting a variable in a shell...

```shell
export GREETING="good morning"
```

... then referencing it from R code.

```r
greeting <- Sys.getenv("GREETING")
print(paste0(greeting, ", friend"))
```

> [1] "good morning, friend"

## Rscript

This section describes the `Rscript` executable, which is bundled with most distributions of R.

`Rscript` can be used to run an R script from the command line.

```shell
Rscript sample-r-code/print-random-numbers.R
```

### `-e`

`-e` means "I'm passing you R code in a string, not a path to a file".

```shell
Rscript -e "library(data.table); data.table(m = rnorm(10))"
```

### Redirection of Rscript output

Some R functions, like `print()`, write to stdout of an R process.

Others, like `message()`, `stop()`, and `warning()` print to stderr.

The code below redirects stderr and stdout to two different files, so you can test this.

```shell
Rscript \
    -e "print('printing'); message('messaging'); warning('warning'); stop('stopping')" \
    1> stdout.txt \
    2> stderr.txt
```

### `--help`

`--help` can be used to retrieve documentation about the available arguments.

```shell
Rscript --help
```

### `--version`

`--version` prints the version of `Rscript`, which is almost always the same as the version of R.

```shell
Rscript --version
```

### `--verbose`

To get more information about what `Rscript` is doing when it runs your code, you can use `--verbose`.

```shell
Rscript --verbose -e "library(data.table); data.table(m = rnorm(10))"
```

### `--default-packages`

By default, R code runs with a few packages attached (e.g. `base`, `graphics`, `methods`, `stats`, `tools`). You can configure this by passing the argument `--default-packages`.

```shell
Rscript -e "data.table(m = rnorm(10))"
```

> Error in data.table(m = rnorm(10)) : could not find function "data.table"
> Execution halted

```shell
Rscript --default-packages="data.table,stats" -e "data.table(m = rnorm(10))"
```

```text
             m
 1: -1.1439311
 2:  0.1853920
 3: -2.3771550
 4:  0.2617524
 5: -0.2855616
 6: -0.3109145
 7: -0.3957713
 8: -0.7548992
 9: -0.7685032
10: -0.1135844
```

### `--save` and `--restore`

If you want the state of the environment to be saved before exiting, you can pass `--save`. If this argument is provided, a file `.RData` will be created.

To prove this, the code below creates a variable `some_var` and then exits.

```shell
Rscript --save -e "some_var <- 11.5"
```

Try running some code that references `some_var` with `--no-restore`. You'll see that R doesn't know anything about that variable.

```shell
Rscript --no-restore -e "print(some_var)"
```

> Error in print(some_var) : object 'some_var' not found
> Execution halted

If you run the same code with `--restore`, R will first load up the saved environment in `.RData`, and now your code can magically reference `some_var`!

```shell
Rscript --restore -e "print(some_var)"
```

### `--no-site-file`, `--no-init-file`, and `--no-environ`

`--no-site-file` and `--no-init-file` can be used to avoid loading specific R config files like `.Rprofile`. `--no-environ` can be used to prevent loading `.Renviron` files.

See https://support.rstudio.com/hc/en-us/articles/360047157094-Managing-R-with-Rprofile-Re[…]on-Rprofile-site-Renviron-site-rsession-conf-and-repos-conf for an overview of these different config files.

### `--vanilla`

Running with `--vanilla` combines the effects of `--no-site-file`, `--no-init-file`, `--no-environ`, and `--no-restore`. It's the safest way to ensure that your code's behavior is predictable when run in different environments.

## Linting Example

This example shows how to write R code that is intended to be run from the command line. Specifically, it explores writing an R script that uses [`{lintr}`](https://github.com/jimhester/lintr) to catch issues in R code.

The directory `sample-r-code/` contains some R scripts intended to trigger linter warnings.

### `lint-basic.R`

To begin, let's start with a simple script that defines a few linters and uses `lintr::lint_dir()` to check for problems.

```r
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
    , "todo_comments"        = lintr::todo_comment_linter(
        c("todo", "fixme", "to-do")
    )
    , "trailing_blank"       = lintr::trailing_blank_lines_linter
    , "trailing_white"       = lintr::trailing_whitespace_linter
    , "true_false"           = lintr::T_and_F_symbol_linter
    , "unneeded_concatenation" = lintr::unneeded_concatenation_linter
)

lintr::lint_dir(
    path = DIR_TO_LINT
    , linters = LINTERS_TO_USE
)
```

Run this from the command line to check for linting errors.

```shell
Rscript --vanilla lint-basic.R
```

This does catch some linting errors!

### `lint-ci.R`

`lint-basic.R` is catching some linting errors, but it could definitely be improved.

1. Even though some linting issues were found, the script returns a 0 exit code! That means this wouldn't be able to fail a continuous integration (CI) build.

    ```shell
    echo $?
    ```

2. The directory `"sample-r-code"` is hard-coded in the script. We should be able to configure that withoout needing to change the code.

To fix the exit-code problem, you can use `quit()` and set an exit code explicitly. To get the necessary information to figure this out, capture the return value of `lintr::lint_dir()`. That function returns a list of errors. If that list has anything in it, the script should return a non-0 exit code.

```r
issues <- lintr::lint_dir(
    path = DIR_TO_LINT
    , linters = LINTERS_TO_USE
)
print(issues)

quit(save = "no", status = length(issues))
```

To make the directory to lint configurable, add a command line argument. R scripts can read arguments from the command line using [`commandArgs()`](https://stat.ethz.ch/R-manual/R-devel/library/base/html/commandArgs.html).

```r
args <- commandArgs(
    trailingOnly = TRUE
)

# assume first argument is the directory to lint
DIR_TO_LINT <- args[[1L]]
```

Try running this new script. You should now see that the linting issues cause a non-0 exit code.

```shell
Rscript lint-ci.R ./sample-r-code
echo "exit code: $?"
```

### `lint-argparse.R`

This script is looking pretty good! But now imagine that you'd like to share this script with teammates. If other people are going to use this code, it should have some documentation baked into it.

It's commoon for command line interfaces (CLIs) to print documentation using `--help` and to print a version using `--version`.

[`{argparse}`](https://cran.r-project.org/web/packages/argparse/index.html) can be used to add this type of functionality. Add this code to `lint-argparse.R`.

```r
library(argparse)
library(lintr)

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
    cat(paste0(VERSION, "\n"))
    quit(save = "no", status = 0)
}
```

With this change, this linter is now starting to look like a legit CLI!

Try printing the help.

```shell
Rscript lint-argparse.R --help
```

```text
usage: lint-argparse.R [-h] [--dir-to-lint DIR_TO_LINT] [--version]

Lint R code with {lintr}

optional arguments:
  -h, --help            show this help message and exit
  --dir-to-lint DIR_TO_LINT
                        Directory to lint
  --version             Print the version of this linting tool.
```

Try printing the version.

```shell
Rscript lint-argparse.R --version
```

> 0.0.1

Try running the linter again.

```shell
Rscript lint-argparse.R --dir-to-lint=$(pwd)/sample-r-code
```

### `lint-pretty.R`

As a final touch, just because we can, let's try adding some color and ascii art to this tool. It's totally unnecessary but it's fun.

You can use `{crayon}` to change the color of terminal output and `{spongebob}` to create some fun ASCII art.

Add the following to print an ASCII spongemock at the beginning of every run.

```r
cat(crayon::yellow(
    spongebob::spongebobsay(
        what = "linting is important"
        , print = FALSE
    )
))
```

And the following near the end of the script to change the color of the summary text based on whether or not linting issues were found.

```r
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
```

Run the following to test the changes.

```shell
Rscript lint-pretty.R --dir-to-lint=$(pwd)/sample-r-code
```

### Removing `Rscript` entirely

If you want to get REALLY fanncy, you can remove the need to use `Rscript` altogether, and add a shebang to the top of the script that indicates `Rscript` should be used to run it.

With this approach, you can also remove the `.R` extension and give your linter a fun name. From this point, it will look like any other command-line tool you install with `apt`, `brew`, `yum`, etc.

```shell
echo '#!/usr/bin/env Rscript' > critiquer
cat lint-pretty.R >> critiquer
chmod +x critiquer
```

With this change, you can now use `critiquer` to run your code. If you put that on `PATH`, it can be called like any other executable.

```shell
export PATH=$(pwd)/:${PATH}

critiquer --help

critiquer --version

critiquer --dir-to-lint=$(pwd)/sample-r-code
```
