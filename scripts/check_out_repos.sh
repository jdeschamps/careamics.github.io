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

    # copy content of temp/src to src/ 
    cp -r $TEMP/$SRC/* $SRC

    # remove temp
    rm -rf $TEMP

done < $REPOS
