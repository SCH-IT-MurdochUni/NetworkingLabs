#!/bin/bash

# File containing the extracted SSH keys and associated users
KEY_FILE="student_keys"

# Declare an associative array to store keys and corresponding users
declare -A key_map

# Read the key file and process each line
while IFS= read -r line; do
    # Check if the line indicates a new user
    if [[ $line == Keys\ for\ user* ]]; then
        # Extract the username from the line
        current_user=$(echo "$line" | awk '{print $4}')
    elif [[ $line == ssh-* ]]; then
        # Extract the key from the line (assuming key starts with ssh-)
        key=$(echo "$line" | awk '{print $1" "$2" "$3}')
        
        # Check if the key already exists in the array
        if [[ -n "${key_map[$key]}" ]]; then
            # If key exists, append the current user to the list
            key_map[$key]="${key_map[$key]}, $current_user"
        else
            # If key does not exist, add it to the array
            key_map[$key]="$current_user"
        fi
    fi
done < "$KEY_FILE"

# Check for and print duplicate keys
for key in "${!key_map[@]}"; do
    users=${key_map[$key]}
    # If there are multiple users for a single key, flag it
    if [[ $users == *","* ]]; then
        echo "Duplicate key found for users: $users"
    fi
done

