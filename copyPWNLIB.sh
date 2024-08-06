#!/bin/bash

SCRIPT_DIR="$(dirname "$(realpath "$0")")"
SOURCE_DIR="$SCRIPT_DIR/MyPwnLib"
TARGET_DIR="$SCRIPT_DIR/.."

if [ ! -d "$SOURCE_DIR" ]; then
    echo "Source directory $SOURCE_DIR does not exist."
    exit 1
fi

cp -r "$SOURCE_DIR/"* "$TARGET_DIR/"

if [ $? -eq 0 ]; then
    echo "Contents copied successfully from $SOURCE_DIR to $TARGET_DIR"
else
    echo "Failed to copy contents."
    exit 1
fi
