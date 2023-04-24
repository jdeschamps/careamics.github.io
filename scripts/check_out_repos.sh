#!/bin/bash

# We could use this rather: https://github.com/jdoiro3/mkdocs-multirepo-plugin
TEMP=".temp/"
SRC="src/"
REPOS="scripts/repos.txt"

# create source folder
mkdir $SRC

while IFS="" read -r p || [ -n "$p" ]
do
    # create temporary folder
    mkdir $TEMP

    # clone repository
    git clone $p $TEMP

    # extract repo name
    REPO_NAME=$(echo $p | sed 's/.*\///')

    # if cloning was successful, a src folder will be created
    if [ -d "$TEMP/$SRC" ]; then
        echo "Cloning $REPO_NAME was successful"

        # copy content of temp/src to src/ 
        cp -r $TEMP/$SRC/* $SRC
 
        # list folder in src
        ls -d $SRC/
        ls -d $TEMP/

        # remove temp
        rm -rf $TEMP
    else
        echo "Cloning $REPO_NAME failed"
    fi

done < $REPOS

# list folder in src
ls -d $SRC/