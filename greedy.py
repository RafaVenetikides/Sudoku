import json, codecs
from DFS import show_game, list_moves, DFS_solve
import numpy as np
import time
from memory_profiler import memory_usage

def fetch_game(fp: str) -> np.array:
    # Retrieving the game from a JSON file

    jason = codecs.open(fp, 'r', encoding='utf=8').read()
    game_jason = json.loads(jason)
    game = np.array(game_jason)
    return game

def get_distances(game: np.array) -> list:
    # To define the closest state, we check the distances based on the number os possible moves on each spot

    lengths = []
    for i in range(len(game)):
        row = []
        for j in range(len(game)):
            if game[i][j] != 0:
                row.append(0)
            else:
                row.append(len(list_moves(game, i, j)))
        lengths.append(row)
    return lengths

def get_min_position(distances: np.array) -> list[int]:
    # Search in the distances array, the first spot with the closest value (least amount of possible moves)

    minimum = 10
    pos = [0, 0]

    for i in range(len(distances)):
        for j in range(len(distances[i])):
            if distances[i][j] != 0 and distances[i][j] < minimum:
                minimum = distances[i][j]
                pos[0] = i
                pos[1] = j
    return pos

def get_state(game: np.array) -> tuple:
    # Defines the h value for that game state and saves it in a tuple for inseartion in the list

    h = 0
    for i in game:
        for j in i:
            if j == 0:
                h += 1
    return (game, h)

def greedy_solve(game: np.array) -> np.array:
    distances = get_distances(game)
    game_states = list()

    while 0 in game:
        #Gets the play position
        play_position = get_min_position(distances)

        for i in list_moves(game, play_position[0], play_position[1]):
            #Play the possible moves in that position
            game[play_position[0]][play_position[1]] = i

            # Inserts the value in the list and sorts it by its "h" value
            game_states.append(get_state(game))
            game_states.sort(key=lambda x: x[1])

            if greedy_solve(game) is not None:
                # Gets the game state with the lowest h found
                return game_states[0][0]
            
            game[play_position[0]][play_position[1]] = 0
        # If no moves are available in that spot, returns None
        return None
    return game


# game = fetch_game('game.json')

# show_game(game)

# print("\n \n")

# game_states = list()

# start_mem = memory_usage()[0]
# start_time = time.time()

# greedy_solution = greedy_solve(game)

# if greedy_solution is not None:
#     show_game(greedy_solution)
# else:
#     print("Game has no solution")

# solve_time = time.time() - start_time
# memory_usage = memory_usage()[0] - start_mem

# print(f'Solve time: {(solve_time * 1000):.4f} ms')
# print(f'Memory used: {memory_usage:.4f} MB')