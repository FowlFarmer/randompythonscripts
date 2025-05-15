#!/bin/bash

echo "This script requires the homebrew version of mcap."
skip_done=false
remove_done=false
export PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"
for arg in "$@"; do
  if [ "$arg" = "--skipdone" ]; then
    skip_done=true
  elif [ "$arg" = "--removedone" ]; then
    remove_done=true
  else
    echo "Unknown argument: $arg"
    echo "Valid args: --skipdone --removedone"
    exit 1
  fi
done

for file in *.bag; do
    filename="${file%.bag}"
    if [ $skip_done = true ]; then
        if [ -f "${filename}.mcap" ]; then
            echo "Skipping $file, already converted to ${file%.bag}.mcap"
            continue
        fi
    fi
    echo "Processing $filename"
    mcap convert "$filename.bag" "$filename.mcap"
    if [ $remove_done = true ]; then
        echo "Removing $filename.bag"
        rm "$filename.bag"
    fi
done