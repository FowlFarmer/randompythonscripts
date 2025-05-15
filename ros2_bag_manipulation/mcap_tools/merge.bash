#!/bin/bash

echo "This script requires the homebrew version of mcap."
export PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"

for file in *_video.mcap; do
    filename="${file%_video.mcap}"
    if([ -f "${filename}_data.mcap" ]); then
        echo "Merging $filename"
        mcap merge "${filename}_video.mcap" "${filename}_data.mcap" -o "${filename}_merged.mcap"
        rm "${filename}_video.mcap" "${filename}_data.mcap"
    fi
done