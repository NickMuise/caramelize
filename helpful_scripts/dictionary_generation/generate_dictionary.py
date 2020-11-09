# This script reads in newline-separated words from a file and creates an
# output file of words that (aside from rules about archaic words, foreign
# words, etc.) could concievably be allowed in Scrabble.

# TODO: make callable with parameters from commandline
# TODO: add option to include tileset + board size with input file to only 
# select words that could be played using those tiles

import sys
import os
from random import sample

def main():
    viable_words = []
    min_word_length = 2
    max_word_length = 15
    num_desired_words = 105000
    input_path = os.path.join(sys.argv[0],"..","resources","linux.words")
    output_path = "new_dictionary"
    
    if os.path.exists(output_path):
        print(f"ERROR: Path {output_path} already exists. Exiting...")
        return 1

    # Get all potentially good words
    all_words = open(input_path).readlines()
    index = 1
    for word in all_words:
        word = word.split()[0]
        if index % (len(all_words) // 10) == 0:
            print(f"Processing input words... {index}/{len(all_words)}")
        if (word.islower()
            and word.isalpha()
            and min_word_length <= len(word)
            and len(word) <= max_word_length
            ):
            viable_words.append(word)
        index += 1
    
    # Check if enough viable words were found
    if len(viable_words) < num_desired_words:
        print(f"WARNING: only {len(viable_words)} viable words were found to meet the number of desired words. Exiting...")
        return 1

    chosen_words = sample(viable_words, num_desired_words)

    # Write selected words into dictionary file
    final_words = "\n".join(chosen_words) # because writelines() doesn't add newlines
    with open(output_path, mode="x") as dest:
        dest.writelines(final_words)

if __name__ == "__main__":
    main()
    