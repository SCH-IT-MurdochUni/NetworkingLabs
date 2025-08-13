#!/bin/bash

# Directory where user home directories are located
HOMEDIR="/home"

# Iterate through each user home directory and collect SSH keys
for userdir in "$HOMEDIR"/*; do
    if [ -d "$userdir/.ssh" ] && [ -f "$userdir/.ssh/authorized_keys" ]; then
        echo "Keys for user $(basename "$userdir"):"
        cat "$userdir/.ssh/authorized_keys"
        echo
    fi
done

