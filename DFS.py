from pprint import pprint
import numpy as np
from typing import List
import codecs, json

def show_game(game: np.array):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 15)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(game[i][j], end="")
        print()

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

def find_square(line: int, row: int) -> List[int]:
    # Finds the center of the square the spot is in
    return ((line//3) * 3) + 1, ((row//3) * 3) + 1

def check_square(game: np.array, line: int, row: int) -> List[int]:
    # Check possible numbers on the spot's square
    square_x, square_y = find_square(line, row)
    possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(square_x - 1, square_x + 2):
        for j in range(square_y - 1, square_y + 2):
            if game[i][j] in possible_numbers:
                possible_numbers.remove(game[i][j])
    return possible_numbers

def list_moves(game: np.array, line: int, row: int) -> List[int]:
    # Returns the intersection between the possible moves in the line, row and square
    line_possibilities = check_line(game, line)
    row_possibilities = check_row(game, row)
    square_possibilities = check_square(game, line, row)

    # Obtaning the interssection and sorting the list
    possible_moves = list(set(line_possibilities) & set(row_possibilities) & set(square_possibilities))
    possible_moves.sort()

    return possible_moves

def DFS_solve(game: np.array) -> np.array:
    # Iterate over the board
    for i in range(9):
        for j in range(9):
            # Found an empty spot
            if game[i][j] == 0:
                # Search possible moves
                for t in list_moves(game, i, j):
                    # Try possible moves
                    game[i][j] = t
                    show_game(game)
                    print("\n")
                    # Recursive call if there is possible moves
                    if DFS_solve(game) is not None:
                        return game
                    # If no possible moves are found, erase the spot
                    game[i][j] = 0
                # If no possible moves are found, return None
                return None
    return game

# Importing the game from a JSON file

# jason = codecs.open("game.json", 'r', encoding='utf-8').read()
# game_json = json.loads(jason)
# game = np.array(game_json)

# show_game(game)

# print("\n\n")

# if DFS_solve(game) is None:
#     print("The game is unsolvable!")
# else:
#     print("\n\n\nSolved game:")   
#     show_game(game)