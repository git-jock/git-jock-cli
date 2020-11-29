#! /bin/bash

ARCH_NAME="jock-$(uname)-$(uname -m)"
ZIP_NAME="$ARCH_NAME.zip"
TMP_ZIP="/tmp/$ZIP_NAME"
TMP_UNZIP="/tmp/$ARCH_NAME"

echo "Downloading $ARCH_NAME to tmp"
rm "$TMP_ZIP"
curl -L "https://github.com/git-jock/git-jock-cli/releases/latest/download/$ZIP_NAME" --output "$TMP_ZIP"

echo "Unzipping in tmp"
rm -r "$TMP_UNZIP"
mkdir "$TMP_UNZIP"
unzip "$TMP_ZIP" -d "$TMP_UNZIP"

echo "Moving jock to /usr/bin"
mv "$TMP_UNZIP/jock" /usr/bin/

echo "Removing tmp files"
rm "$TMP_ZIP"
rm -r "$TMP_UNZIP"