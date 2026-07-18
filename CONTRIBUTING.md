# Contributing

Welcome to `QTLab` contributor's guide.

This document focuses on getting any potential contributor familiarized
with the development processes, but [other kinds of
contributions](https://opensource.guide/how-to-contribute) are also
appreciated.

If you are new to using [git](https://git-scm.com) or have never
collaborated in a project previously, please have a look at
[contribution-guide.org](http://www.contribution-guide.org/). Other
resources are also listed in the excellent [guide created by
FreeCodeCamp](https://github.com/FreeCodeCamp/how-to-contribute-to-open-source)[^1].

Please notice, all users and contributors are expected to be **open,
considerate, reasonable, and respectful**. When in doubt, [Python
Software Foundation\'s Code of
Conduct](https://www.python.org/psf/conduct/) is a good reference in
terms of behavior guidelines.


## Issue Reports

If you experience bugs or general issues with `QTLab`, please
have a look on the [issue
tracker](https://github.com/luisfdo/QTLab/issues). If you
don't see anything useful there, please feel free to fire an issue
report.

>Please don\'t forget to include the closed issues in your search.
Sometimes a solution was already reported, and the problem is considered
**solved**.

New issue reports should include information about your programming
environment (e.g., operating system, Python version) and steps to
reproduce the problem. Please try also to simplify the reproduction
steps to a very minimal example that still illustrates the problem you
are facing. By removing other factors, you help us to identify the root
cause of the issue.


## Documentation Improvements

You can help improve `QTLab` docs by making them more readable
and coherent, or by adding missing information and correcting mistakes.

`QTLab` documentation uses
[Markdown](https://www.markdownguide.org/basic-syntax/) as its main
documentation compiler. This means that the docs are kept in the same
repository as the project code, and that any documentation update is
done in the same way was a code contribution.


>Please notice that the [GitHub web
interface](https://docs.github.com/en/github/managing-files-in-a-repository/managing-files-on-github/editing-files-in-your-repository)
provides a quick way of propose changes in `QTLab`\'s files.
While this mechanism can be tricky for normal code contributions, it
works perfectly fine for contributing to the docs, and can be quite
handy.

>If you are interested in trying this method out, please navigate to the
`docs` folder in the source
[repository](https://github.com/luisfdo/QTLab), find which
file you would like to propose changes and click in the little pencil
icon at the top, to open [GitHub\'s code
editor](https://docs.github.com/en/github/managing-files-in-a-repository/managing-files-on-github/editing-files-in-your-repository).
Once you finish editing the file, please write a message in the form at
the bottom of the page describing which changes have you made and what
are the motivations behind them and submit your proposal.


## Engineering Principles

1. Correctness before performance.
2. Explicit is better than implicit.
3. Make illegal states impossible.
4. Small composable components.
5. Immutable domain models where practical.
6. Every feature must be testable.
7. Document decisions.
8. Research before optimization.
9. Separate concerns.
10. A passing backtest is not evidence of a good strategy.


## Code Contributions

To help you get started quickly please refer to our [README.md](README.md) and
[ADR (Architectural Design Records)](docs/adr).


### Submit an issue

Before you work on any non-trivial code contribution it's best to first
create a report in the [issue
tracker](https://github.com/luisfdo/QTLab/issues) to start
a discussion on the subject. This often provides additional
considerations and avoids unnecessary work.


### Create an environment

Before you start coding, we recommend creating an isolated [virtual
environment](https://realpython.com/python-virtual-environments-a-primer/)
to avoid any problems with your installed Python packages. This can
easily be done via either `uv` or `virtualenv`.


### Clone the repository

1.  Create an user account on GitHub if you do not already have one.

2.  Fork the project
    [repository](https://github.com/luisfdo/QTLab): click
    on the *Fork* button near the top of the page. This creates a copy
    of the code under your account on GitHub.

3.  Clone this copy to your local disk:

        git clone git@github.com:YourLogin/QTLab.git
        cd QTLab

4.  You should run:

        uv pip install -r requirements.txt

    `QTLab` comes with a lot of hooks configured to automatically
    help the developer to check the code being written.

### Implement your changes

1.  Create a branch to hold your changes:

        git checkout -b my-feature

    and start making changes. Never work on the master branch!

2.  Start your work on this branch. Don\'t forget to add
    [docstrings](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html)
    to new functions, modules and classes, especially if they are part
    of public APIs.

3.  Add yourself to the list of contributors in `AUTHORS.rst`.

4.  When you're done editing, do:

        git add <MODIFIED FILES>
        git commit

    to record your changes in [git](https://git-scm.com).

    >Don\'t forget to add unit tests and documentation in case your
    contribution adds an additional feature and is not just a bugfix.

    Moreover, writing a [descriptive commit
    message](https://chris.beams.io/posts/git-commit) is highly
    recommended. In case of doubt, you can check the commit history
    with:

        git log --graph --decorate --pretty=oneline --abbrev-commit --all

    to look for recurring communication patterns.

5.  Please check that your changes don\'t break any unit tests


### Submit your contribution

1.  If everything works fine, push your local branch to GitHub with:

        git push -u origin my-feature

2.  Go to the web page of your fork and click \"Create pull request\" to
    send your changes for review.


### Troubleshooting

The following tips can be used when facing problems to build or test the
package:

1.  Make sure to fetch all the tags from the upstream
    [repository](https://github.com/luisfdo/QTLab). The
    command `git describe --abbrev=0 --tags` should return the version
    you are expecting. If you are trying to run CI scripts in a fork
    repository, make sure to push all the tags. You can also try to
    remove all the egg files or the complete egg folder, i.e., `.eggs`,
    as well as the `*.egg-info` folders in the `QTLab` folder or
    potentially in the root of your project.


## Maintainer tasks

### Releases

If you are part of the group of maintainers and have correct user
permissions, the following steps can be used to release a new version for `QTLab`:

1.  Make sure all unit tests are successful.
2.  Tag the current commit on the main branch with a release tag, e.g.,
    `v1.2.3`.
3.  Push the new tag to the upstream
    [repository](https://github.com/luisfdo/QTLab), e.g.,
    `git push upstream v1.2.3`
4.  Clean up the `dist` and `build` folders with `tox -e clean` (or
    `rm -rf dist build`) to avoid confusion with old builds and Sphinx
    docs.


[^1]: Even though, these resources focus on open source projects and
    communities, the general ideas behind collaborating with other
    developers to collectively create software are general and can be
    applied to all sorts of environments, including private companies
    and proprietary code bases.
