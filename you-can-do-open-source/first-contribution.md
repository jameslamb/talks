# Finding Your First Open Source Contribution

When making your 1st or 5th or 10th open source contribution, it can be difficult to know where to start. This document contains some ideas for contributions that are:

* low-commitment (<1 hour)
* easy to find
* helpful to projects, and therefore likely to be accepted.

If you have ideas for others, please submit a pull request :).

## No Git Required

To develop software, you will eventually have to learn a version control system like `git`. However, there are some open source contributions that you can make without needing to ever use version control, because code hosting platforms allow you to suggest edits in the browser!

This section has no-git contribution ideas.

### Add Unwanted files to .gitignore

Most repositories using `git` for version control will have a file at their root called `.gitignore`. This file contains a set of patterns. Any files that match those patterns will not be "checked in" to the repository.

People typically like to use this to avoid checking in the following types of files:

```text
# build artifacts
*.7z
*.a
**/build/
*.bz2
**/dist/
*.dll
*.dylib
**/*.egg-info/
*.exe
*.msi
*.o
**/__pycache__/
*.py[cod]
*.rar
*.so
*.tar.gz
*.zip

# data files
*.csv
*.db
*.json
*.ndjson
*.npy
*.parquet
*.pkl
*.pq
*.sqlite
*.xls
*.xlsm
*.xlsx

# credentials and key material
*.env
*.pem
*.pub
*.rdp
*_rsa
```

Adding these types of things to a project's `.gitignore` will often be a welcome addition, especially the "credentials and key material" part.

1. Find a repository on GitHub that you're interested in.
1. Click on that project's .gitignore file
1. Click the little pencil icon, which will say "edit this file"
1. In that editor window, look for some of the extensions above. If they're missing, add them.
1. When you're done, scroll to the bottom. Where it says "Update .gitignore", change that to a more useful message like "Add credentials to .gitignore"
1. Click "Commit Changes". This will open the "Submit a Pull Request" screen.
1. In the description, add a short message explaining what this PR does and why you think it is useful. It's important that this proactively answers the question "why should these changes be merged?".
1. When you're ready, click "Create Pull Request".
