#!/bin/bash
# This script is used to clone all repositories in repos.txt, it installs the
# packages and move the content of their src folder into a single src folder.

# Note: We could potentially use: https://github.com/jdoiro3/mkdocs-multirepo-plugin


TEMP=".temp"
SRC="src"
REPOS="scripts/git_repositories.txt"

# create source folder
mkdir $SRC

while IFS="" read -r p || [ -n "$p" ]
do
    # create temporary folder
    mkdir $TEMP

    # clone repository
    git clone $p $TEMP

    # extract repo name without .git
    FOLDER_NAME=$(echo $p | sed 's/.*\///' | sed 's/.git//')

    # replace hyphens by underscores
    REPO_NAME=$(echo $FOLDER_NAME | sed 's/-/_/g')

    # if cloning was successful, a src folder will be created
    if [ -d "$TEMP/$SRC" ]; then
        echo "Cloning $REPO_NAME was successful"

        # attempt to install package from source
        pip install $TEMP

        # copy content of temp/src to src/
        cp -r $TEMP/$SRC/* $SRC

        # remove temp
        rm -rf $TEMP

        # check if repo was copied to src
        if [ -d "$SRC/$REPO_NAME" ]; then
            echo "Copying $REPO_NAME was successful"
        else
            echo "Copying $REPO_NAME failed"
        fi
    else
        echo "Cloning $REPO_NAME failed"
    fi

done < $REPOS
