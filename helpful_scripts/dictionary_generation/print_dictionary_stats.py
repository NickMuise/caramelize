import os
import sys
from pprint import pprint

if __name__ == "__main__":
    my_occurences = {}
    with open("new_dictionary") as f:
        for line in f:
            line = line.strip()
            length = len(line)
            if length in my_occurences:
                my_occurences[length] = my_occurences[length] + 1
            else:
                my_occurences[length] = 1

    my_ratios = {}
    lcd = my_occurences[2]
    for key in my_occurences:
        ratio = my_occurences[key] / lcd
        ratio *= 100
        ratio = int(ratio)
        ratio /= 100
        my_ratios[key] = ratio

    scrabble_occurences = {
        2: 127,
        3: 1065,
        4: 4169,
        5: 9320,
        6: 16940,
        7: 25152,
        8: 31392,
        9: 26100,
        10: 17429,
        11: 11885,
        12: 7954,
        13: 5117,
        14: 3029,
        15: 1735
    }
    scrabble_ratios = {}
    scrabble_lcd = scrabble_occurences[2]
    for key in scrabble_occurences:
        ratio = scrabble_occurences[key] / scrabble_lcd
        ratio *= 100
        ratio = int(ratio)
        ratio /= 100
        scrabble_ratios[key] = ratio
    
    print("raw occurences:\n official scrabble | this dictionary")
    for key in range(2, 16):
        print(f"{key}: {scrabble_occurences[key]}  | {my_occurences[key]}")
    
    print("ratios:\n official scrabble | this dictionary")
    for key in range(2, 16):
        print(f"{key}: {scrabble_ratios[key]}  | {my_ratios[key]}")
    
    total = 0
    for key, value in scrabble_occurences.items():
        total += value
    print(total)