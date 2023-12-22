<p align="center">
  <a href="https://careamics.github.io/">
    <img src="https://github.com/CAREamics/.github/blob/main/profile/images/banner_careamics.png">
  </a>
</p>

[![Github page](https://github.com/CAREamics/careamics.github.io/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/CAREamics/careamics.github.io/actions/workflows/deploy-pages.yml)

# Welcome to CAREamics docs

This repository contains the source code for the CAREamics documentation website. The 
website is built using [MkDocs](https://www.mkdocs.org/) and the 
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme, with a few
modifications.

Beside the static pages, the website automatically checks out repositories listed in
[git_repositories.txt](scripts/git_repositories.txt) and generates documentation for
the corresponding projects, all thanks to [mkdocstring](https://mkdocstrings.github.io/)
, [mkdocs-gen-files](https://oprypin.github.io/mkdocs-gen-files/) and 
[mkdocs-literate-nav](https://oprypin.github.io/mkdocs-literate-nav/reference.html).
Similarly, it also uses [mkdocs-jupyter](https://pypi.org/project/mkdocs-jupyter/) to
add Jupyter notebooks to the documentation from the list in 
[notebooks.csv](scripts/notebooks.csv).

## How to build the pages locally

In order to build the pages locally, follow these steps:

1. Fork this repository and clone it.
2. Create a new environment and install the dependencies:
    ```bash
    conda create -n careamics-docs python=3.11
    pip install -r requirements.txt
    ```
4. Run the following scripts (which are normally run by the CI):
    ```bash
    python scripts/check_out_repos.sh
    python scripts/check_out_notebooks.sh
    ```
3. Build the pages:
    ```bash
    mkdocs serve
    ```
4. Open the local link in your browser.


## How to add a new project to the documentation

In order to add a new project to the documentation, simply edit 
[git_repositories.txt](scripts/git_repositories.txt):

```
https://github.com/CAREamics/careamics
https://github.com/CAREamics/careamics-portfolio
<new project here>
```

## How to add a new notebook to the documentation

In order to add a new notebook to the documentation, simply edit
[notebooks.csv](scripts/notebooks.csv):

```
repository url, path in repository, destination in docs, title
https://github.com/CAREamics/careamics.git,examples/2D/example_SEM.ipynb,N2V,2D_SEM
<reference repository>,<relative path to the notebook>,<destination in applications>,<title>
<new line>
```

The script clones the repository, copy the notebook to the relative destination (with
respect to `docs/applications`) and change the name of the notebook. The name of the 
notebook will be used as title in the documentation navigation side-bar (with 
underscores replaced by spaces).

In is important to end the `.csv` file with a new line.

## How to update the pages without any commit

This can be useful when one of the project has changed and we need to update the API
doc. In such a case, click on the `Deploy to GitHub Pages` in the `Actions` tab, and
run the workflow.

