
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

Please highlight the text below for spoilers/answers. 

* How many times does the string "verdigris" appear, enter a number only: <span style#"color: black; background: black;">9</span>
* What is the surname of the author of the filename “1107.txt”, the answer is case sensitive: <span style#"color: black; background: black;">Shakespeare</span>
* What is the surname of the book author, of the file that is exactly 255258 bytes. The answer is case sensitive: <span style#"color: black; background: black;">Lobo</span>
* What is the filename of the file with the 3rd oldest creation date: <span style#"color: black; background: black;">1498.txt</span>
* Find the word that follows the follows the text “Next day there was a surprise for Jack”: <span style#"color: black; background: black;">Halliday</span> (Case sensitive-no spaces)

