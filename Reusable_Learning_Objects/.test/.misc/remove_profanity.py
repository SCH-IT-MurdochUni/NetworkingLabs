#!/usr/bin/env python3

"""
remove_profanity.py

A script to remove common profanity from a password list.

Usage:
    python3 remove_profanity.py -i input_passwords.txt -o cleaned_passwords.txt
    python3 remove_profanity.py --input input_passwords.txt --output cleaned_passwords.txt --profanity custom_profanity.txt

Arguments:
    -i, --input        Path to the input password list file.
    -o, --output       Path to the output cleaned password list file.
    -p, --profanity    (Optional) Path to a custom profanity list file.

Example:
    python3 remove_profanity.py -i passwords.txt -o cleaned_passwords.txt
"""

import argparse
import os
import sys

def load_profanity_list(profanity_file=None):
    """
    Load profanity words from a file or use a predefined list.

    :param profanity_file: Path to a custom profanity list file.
    :return: A set of profane words in lowercase.
    """
    if profanity_file:
        if not os.path.isfile(profanity_file):
            print(f"Error: Profanity file '{profanity_file}' does not exist.")
            sys.exit(1)
        with open(profanity_file, 'r', encoding='utf-8') as f:
            profanity = set(line.strip().lower() for line in f if line.strip())
    else:
        # Predefined list of common profane words. You can expand this list as needed.
        profanity = {
            'badword1',
            'badword2',
            'badword3',
            # Add more profane words here.
            'shit',
            'fuck',
            'bitch',
            'bastard',
            'dick',
            'piss',
            'crap',
            'cunt',
            'damn',
            'hell',
            'slut',
            'whore',
            'asshole',
            'douche',
            'fag',
            'faggot',
            'nigger',
            'coon',
            'kike',
            'spic',
            'chink',
            'dyke',
            'tranny',
            'tard',
            'retard',
            # Note: This list contains offensive terms. Use responsibly.
        }
    return profanity

def is_profane(password, profanity_set):
    """
    Check if the password contains any profane words.

    :param password: The password string to check.
    :param profanity_set: A set of profane words.
    :return: True if profane, False otherwise.
    """
    password_lower = password.lower()
    for profane_word in profanity_set:
        if profane_word in password_lower:
            return True
    return False

def filter_passwords(input_file, output_file, profanity_set):
    """
    Filter out profane passwords from the input file and write cleaned passwords to the output file.

    :param input_file: Path to the input password list file.
    :param output_file: Path to the output cleaned password list file.
    :param profanity_set: A set of profane words.
    """
    if not os.path.isfile(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        sys.exit(1)

    cleaned_passwords = []
    total = 0
    removed = 0

    with open(input_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            password = line.strip()
            if not password:
                continue  # Skip empty lines
            total += 1
            if not is_profane(password, profanity_set):
                cleaned_passwords.append(password)
            else:
                removed += 1

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for pwd in cleaned_passwords:
            outfile.write(pwd + '\n')

    print(f"Filtering complete. Total passwords processed: {total}")
    print(f"Passwords removed due to profanity: {removed}")
    print(f"Cleaned passwords saved to: {output_file}")

def parse_arguments():
    """
    Parse command-line arguments.

    :return: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Remove common profanity from a password list.")
    parser.add_argument('-i', '--input', required=True, help='Path to the input password list file.')
    parser.add_argument('-o', '--output', required=True, help='Path to the output cleaned password list file.')
    parser.add_argument('-p', '--profanity', help='(Optional) Path to a custom profanity list file.')
    return parser.parse_args()

def main():
    args = parse_arguments()
    profanity_set = load_profanity_list(args.profanity)
    filter_passwords(args.input, args.output, profanity_set)

if __name__ == "__main__":
    main()

