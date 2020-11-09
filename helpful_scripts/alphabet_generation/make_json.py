import json
from pprint import pprint
letters = {
    "_": 2,
    "A":9,
    "B":2,
    "C":2,
    "D":4,
    "E":12,
    "F":2,
    "G":3,
    "H":2,
    "I":9,
    "J":1,
    "K":1,
    "L":4,
    "M":2,
    "N":6,
    "O":8,
    "P":2,
    "Q":1,
    "R":6,
    "S":4,
    "T":6,
    "U":4,
    "V":2,
    "W":2,
    "X":1,
    "Y":2,
    "Z":1
}
letter_values = {
    "_":0,
    "A":1,
    "B":3,
    "C":3,
    "D":2,
    "E":1,
    "F":4,
    "G":2,
    "H":4,
    "I":1,
    "J":8,
    "K":5,
    "L":1,
    "M":3,
    "N":1,
    "O":1,
    "P":3,
    "Q":10,
    "R":1,
    "S":1,
    "T":1,
    "U":1,
    "V":4,
    "W":4,
    "X":8,
    "Y":4,
    "Z":10
}

combined = {}
for key, value in letters.items():
    combined[key] = {"occurences":value, "value":letter_values[key]}
    if key.isalpha():
        combined[key.lower()] = {"occurences":0, "value":0}
# letters_s = json.dumps(letters)
# letter_values_s = json.dumps(letter_values)
# pprint(letters_s)
# pprint(letter_values_s)
# print(json.dumps(letters, indent=4))
# print(json.dumps(letter_values, indent=4))
# pprint(letters, indent=4)
# pprint(letter_values, indent=4)
print(json.dumps(combined, indent=4))