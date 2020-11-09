# This script reads in a newline-separated list of words and, based on the 
# JSON tileset it is provided with, and the minimum/maximum
# word length provided, it generates a list of words from the original list
# which could be formed using that tileset and those rules.

# TODO: make callable with parameters from commandline
# TODO: add option to include tileset + board size with input file to only 
# select words that could be played using those tiles

import sys
import os
import json
from random import sample
from collections import Counter

class DictionaryGenerator:

    def __init__(self, tileset, min_word_length=2, max_word_length=15):
        self.tileset = tileset
        self.min_word_length = min_word_length
        self.max_word_length = max_word_length

    def extract_letters_from_word(self, word):
        """Return all the letters in the supplied word, in alphabetic order.
        """
        letters = list(word)
        letters.sort()
        letters = "".join(letters)
        return letters

    def get_legal_words(self, words):
        """Get all words that are within the min/max word length, and which
        contain only characters within the current character set.
        """
        index = 1
        legal_words = []
        legal_letters = set(self.tileset)
        if "_" in legal_letters:
            legal_letters.remove("_")
        for word in words:
            word = word.split()[0]
            if (self.min_word_length <= len(word)
                and len(word) <= self.max_word_length
                and len(set(word) - legal_letters) == 0
                ):
                legal_words.append(word)
            index += 1

        return legal_words
    
    def get_playable_words(self, words):
        """Get all words which can be played using the tiles in the current
        tileset, including any wildcard tiles.
        """
        playable_words = []
        legal_letters = set(self.tileset)
        num_wildcards = 0
        if "_" in self.tileset:
            num_wildcards = self.tileset["_"]["occurences"]
        for word in words:
            letter_counts = Counter(word)
            shared_letters = set(letter_counts) | legal_letters
            wildcards_needed = 0
            for letter in shared_letters:
                if self.tileset[letter]["occurences"] < letter_counts[letter]:
                    wildcards_needed += letter_counts[letter] - self.tileset[letter]["occurences"]
            if wildcards_needed <= num_wildcards:
                playable_words.append(word)

        return playable_words

    def validate_words(self, words):
        """Sort the given list of words, and remove all duplicate words + all
        words which can't be played in the current tileset.
        """
        print(f"Validating {len(input_words)} words:")
        for i in range(len(words)):
            words[i] = words[i].upper()

        # remove duplicates
        unique_words = list(dict.fromkeys(words))
        print(f"Removed {len(words) - len(unique_words)} duplicate words.")

        legal_words = self.get_legal_words(unique_words)
        print(f"Removed {len(unique_words) - len(legal_words)} illegal words.")

        playable_words = self.get_playable_words(legal_words)
        print(f"Removed {len(legal_words) - len(playable_words)} unplayable words.")

        playable_words.sort()
        return playable_words

    def get_play_dictionary(self, words, num_desired_words=105000):
        """Given a list of words, return a random sample of those words.
        """
        chosen_words = sample(words, num_desired_words)
        chosen_words.sort()
        return chosen_words

if __name__ == "__main__":
    tileset_path = os.path.join(sys.argv[0], "..", "..", "alphabet_generation", "standard_letters.json")
    tileset = json.load(open(tileset_path))
    input_words_path = os.path.join(sys.argv[0],"..","linux.words")
    input_words = open(input_words_path).readlines()
    output_path = "english_words"
    generator = DictionaryGenerator(tileset)
    
    if os.path.exists(output_path):
        sys.exit(f"ERROR: Path {output_path} already exists. Exiting...")

    valid_words = generator.validate_words(input_words)

    chosen_words = generator.get_play_dictionary(valid_words)

    # Write selected words into dictionary file
    final_words = "\n".join(chosen_words) # because writelines() doesn't add newlines
    with open(output_path, mode="x") as dest:
        dest.writelines(final_words)
