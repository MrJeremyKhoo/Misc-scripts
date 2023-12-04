#!/bin/bash

# Check if syslog-ng is installed, if not, install it
if ! command -v syslog-ng &> /dev/null; then
    echo "syslog-ng is not installed. Installing..."
    sudo apt update
    sudo apt install -y syslog-ng
    echo "syslog-ng has been installed."
else
    echo "syslog-ng is already installed."
fi

# Check if loggen is installed
if command -v loggen &> /dev/null; then
    read -p "Enter log size (optional): " log_size
    read -p "Enter log rate (optional): " log_rate
    read -p "Enter log interval (optional): " log_interval
    read -p "Enter log destination (IP<space>Port) (optional): " log_destination
    read -p "Enter reference file (optional): " reference_file

    loggen_cmd="loggen --stream --loop-reading"

    if [ -n "$log_size" ]; then
        loggen_cmd+=" --size $log_size"
    fi

    if [ -n "$log_rate" ]; then
        loggen_cmd+=" --rate $log_rate"
    fi

    if [ -n "$log_interval" ]; then
        loggen_cmd+=" --interval $log_interval"
    fi

    if [ -n "$log_destination" ]; then
        loggen_cmd+=" $log_destination"
    fi

    if [ -n "$reference_file" ]; then
        if [ -f "$reference_file" ]; then
            loggen_cmd+=" -R $reference_file"
        else
            echo "Error: Provided file does not exist."
        fi
    fi

    eval "$loggen_cmd"
else
    echo "loggen is not installed. Please install it to continue."
fi

