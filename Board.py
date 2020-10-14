import json
import csv

class Board:

    def __init__(self, board_path="standard_board.csv", alphabet_path="standard_letters.json"):
        # initialize game board
        self.board = []
        with open(board_path) as board_file:
            board_reader = csv.reader(board_file)
            for row in board_reader:
                self.board.append(row)

        # initialize tilebag
        letters = json.load(open(alphabet_path))
        self.tilebag = []
        for letter, values in letters.items():
            for _ in range(values["occurences"]):
                new_tile = Tile(letter, values["value"])
                if letter == "_":
                    new_tile.is_blank = True
                self.tilebag.append(new_tile)

    def display_board(self):
        """Display the current board state."""
        board_string = ""
        
        for row in self.board:
            for space in row:
                board_string += space + " "
            board_string += "\n"
        
        board_string += (
            "* = starting space (double word value)\n"
            + "! = double letter value, @ = triple letter value\n"
            + "# = double word value, $ = triple word value"
        )
        print(board_string)

    #TODO implement
    def save_game(self):
        """Dump the current board state and game settings in a human-readable 
        format that can be reloaded later.
        """
        pass 

class Tile:
    def __init__(self, letter, value, is_blank=False):
        self.letter = letter
        self.value = value
        self.is_blank = is_blank
    
    def __str__(self):
        return self.letter

if __name__ == "__main__":
    board = Board()
    board.display_board()