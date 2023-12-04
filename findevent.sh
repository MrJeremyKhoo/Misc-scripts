#!/bin/bash

# Specify the file containing strings, each on a new line
strings_file="eventcode"

# Specify the directory to search
directory="YAML3"

# Check if the strings file exists
if [ ! -f "$strings_file" ]; then
    echo "Error: Strings file not found."
    exit 1
fi

# Read strings from the file into an array
mapfile -t strings < "$strings_file"

# Iterate over each string and search for it in the directory
for string in "${strings[@]}"; do
    # Remove leading and trailing whitespace from each string
    string=$(echo "$string" | sed 's/^[ \t]*//;s/[ \t]*$//')
    
    # Construct the case-insensitive regular expression with any number of characters between "eventid" and the current string
    regex="splunk.*event.*$string"
    
    echo "Searching for occurrences of '$regex' in $directory..."
    find "$directory" -type f -exec grep -i -H -E "$regex" {} \; -print
done

