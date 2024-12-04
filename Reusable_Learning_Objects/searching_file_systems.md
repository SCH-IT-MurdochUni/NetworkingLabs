```
 ____                      _     _             
/ ___|  ___  __ _ _ __ ___| |__ (_)_ __   __ _ 
\___ \ / _ \/ _` | '__/ __| '_ \| | '_ \ / _` |
 ___) |  __/ (_| | | | (__| | | | | | | | (_| |
|____/ \___|\__,_|_|  \___|_| |_|_|_| |_|\__, |
                                         |___/ 
 _____ _ _                     _                     
|  ___(_) | ___  ___ _   _ ___| |_ ___ _ __ ___  ___ 
| |_  | | |/ _ \/ __| | | / __| __/ _ \ '_ ` _ \/ __|
|  _| | | |  __/\__ \ |_| \__ \ ||  __/ | | | | \__ \
|_|   |_|_|\___||___/\__, |___/\__\___|_| |_| |_|___/
                     |___/                           
```

These following are some notes on how to search for files on filesystems. Use these to search the Gutenberg Archive [[:Media:gutenberg.tar.bz2]].

## Extracting the Archive ## 

You can extract the archive with:

	bunzip2 Gutenberg.tar.bz2

Then:

	tar -xvf Gutenberg.tar

Once you have done this, explore the contents for a few minutes, then play with the different command-line search options below. You can finish the lab by answering the questions at the bottom of the page.

## Searching the Archive ##

### Searching for filenames ###

To search for a filename containing certain characters you can use

	find /path/to/where/you/search/from -name "*.extension"

### Searching for text ###

To search for text within a certain structure you can adapt the following. 

	find /path/to/where/you/search/from -type f -exec grep -H 'text-to-find-here' {} \;

Or you can use grep:

	grep -r "string" /path

To show the lines surrounding the string match:

	grep -r -C 3 foo README.txt

### Modification and creation dates ###

To search for the most recently modified file:

	find $1 -type f -exec stat --format '%Y :%y %n' "{}" \; | sort -nr | cut -d: -f2- | head

To search for the oldest creation date:

	find /path/to/where/you/search/from -type f -printf '%T+ %p\n' | sort | head -n 20

To find a file of a certain size for example 68 bytes

	find /path/to/where/you/search/from -type f -size 68c -exec ls {} \;

To find files 512k you could use:

	find /path/to/where/you/search/from -type f -size +512k -exec ls -lh {} \;

To find the largest files in the filesystem

	du -a /path/to/where/you/search/from | sort -n -r | head -n 20

### Investigating the frequency of elements in a file ###

I use the following on the command line to look for frequent elements. You need to use your brain to filter the signal from the noise but it can be useful to identify uncommonly frequent IP addresses, MAC addresses and usernames et cetera.

	sed -e 's/\s/\n/g' < file_of_interest.txt | sort | uniq -c | sort -nr | head  -200

## Questions ##

Please click the spoilers for answers below: 

1. How many times does the string "verdigris" appear, enter a number only:<details><summary>Spoiler</summary>9</details>
2. What is the surname of the author of the filename “1107.txt”, the answer is case sensitive: <details><summary>Spoiler</summary>Shakespeare</details>
3. What is the surname of the book author, of the file that is exactly 255258 bytes. The answer is case sensitive: <details><summary>Spoiler</summary>Lobo</details>
4. What is the filename of the file with the 3rd oldest creation date: <details><summary>Spoiler</summary>1498.txt</details>
5. Find the word that follows the follows the text “Next day there was a surprise for Jack”: (Case sensitive-no spaces) <details><summary>Spoiler</summary>Halliday</details> 

