#!/bin/bash

VERSION=1
MINOR=0
PATCH=
EXTRAVERSION="-rc2"

NOTES="(update)"
BRANCH="dev"

if [[ -z $PATCH ]]; then
    PATCH=""
else
    PATCH=".$PATCH"
fi

if [[ $EXTRAVERSION == *"-rc"* ]]; then
    FULL_VERSION="$VERSION.$MINOR$PATCH$EXTRAVERSION"
else

    if [[ -z $EXTRAVERSION ]]; then
        FULL_VERSION="$VERSION.$MINOR$PATCH"
    else
        FULL_VERSION="$VERSION.$MINOR$PATCH.$EXTRAVERSION"
    fi
fi

git add .
git commit -m "$FULL_VERSION $NOTES"
git push -u origin $BRANCH
git tag v$FULL_VERSION
git push --tags