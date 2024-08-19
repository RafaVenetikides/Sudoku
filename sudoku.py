""" Description: Solves a sudoku game
    Code by: Rafael Honorio Venetikides 
"""

from pprint import pprint
import numpy as np
from typing import List
import codecs, json

def find_square(line: int, row: int) -> tuple:
    # Finds the center of the square the spot is in
    if line < 3:
        square_x = 1
    elif line < 6:
        square_x = 4
    else:
        square_x = 7
    if row < 3:
        square_y = 1
    elif row < 6:
        square_y = 4
    else:
        square_y = 7
    return square_x, square_y

def check_line(game: np.array, line: int) -> List[int]:
    # Check possible numbers on the spot's line
    possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in game[line]:
        if i in possible_numbers:
            possible_numbers.remove(i)
    return possible_numbers

def check_row(game: np.array, row: int) -> List[int]:
    # Check possible numbers on the spot's row
    possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(len(game)):
        if game[i][row] in possible_numbers:
            possible_numbers.remove(game[i][row])
    return possible_numbers

def check_square(game: np.array, line: int, row: int) -> List[int]:
    # Check possible numbers on the spot's square
    square_x, square_y = find_square(line, row)
    possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(square_x - 1, square_x + 2):
        for j in range(square_y - 1, square_y + 2):
            if game[i][j] in possible_numbers:
                possible_numbers.remove(game[i][j])
    return possible_numbers

# Importing the game from a JSON file

jason = codecs.open("game.json", 'r', encoding='utf-8').read()
game_json = json.loads(jason)
game = np.array(game_json)

pprint(game)

# Iterating through the game, if no 0s are found (empty spaces), the game is solved 
while (0 in game):
    current_game = game.copy()
    for i in range(len(game)):
        for j in range(len(game[i])):

            # If spot is 0 (empty), check line, row and square for possible numbers
            if game[i][j] == 0:
                line = check_line(game, i)
                row = check_row(game, j)
                square = check_square(game, i, j)
                # Find the intersection between the three lists
                possible_numbers = list(set(line) & set(row) & set(square))

                # If only one number is possible in that spot, it is the correct number
                if len(possible_numbers) == 1:
                    game[i][j] = possible_numbers[0]
                    print(f"Value found in {i}, {j}: {possible_numbers[0]}")
                    pprint(game)
    if np.array_equal(current_game, game):
        print("No progress was made")
        break
        

# When no 0s are found, the game is solved
if 0 in game:
    print("The game could not be solved")
else:
    print("Sudoku solved!")
    pprint(game)