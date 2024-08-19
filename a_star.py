from DFS import show_game, list_moves
import numpy as np
import time
from memory_profiler import memory_usage
from greedy import fetch_game, get_distances, get_min_position

def get_state(game_state: list) -> tuple:
    # Defines the h value for that game state and saves it in a tuple for inseartion in the list

    h = 0
    for i in game:
        for j in i:
            if j == 0:
                h += 1



    return [game, h]

def get_fn(game: np.array) -> tuple:
    # Gets the game state and it's "h" value
    state = get_state(game)

    # TODO: add the numbers of moves it took to get to that state
    fn_state = (state[0], state[1] + 1)
    return fn_state

game = fetch_game('game.json')

def a_star_solve(game: np.array) -> np.array:
    distances = get_distances(game)
    game_states = list()

    while 0 in game:
        #Gets the play position
        play_position = get_min_position(distances)

        for i in list_moves(game, play_position[0], play_position[1]):
            #Play the possible moves in that position
            game[play_position[0]][play_position[1]] = i

            # Inserts the value in the list and sorts it by its f(n) value
            game_states.append(get_fn(game))
            game_states.sort(key=lambda x: x[1])

            if a_star_solve(game) is not None:
                # Gets the game state with the lowest h found
                return game_states[0][0]
            
            game[play_position[0]][play_position[1]] = 0
        # If no moves are available in that spot, returns None
        return None
    return game

game = fetch_game('game.json')

show_game(game)

print("\n \n")

game_states = list()

start_mem = memory_usage()[0]
start_time = time.time()

a_star_solution = a_star_solve(game)

if a_star_solution is not None:
    show_game(a_star_solution)
else:
    print("Game has no solution")

solve_time = time.time() - start_time
memory_usage = memory_usage()[0] - start_mem

print(f'Solve time: {(solve_time * 1000):.4f} ms')
print(f'Memory used: {memory_usage:.4f} MB')