from DFS import show_game, list_moves
import numpy as np
import time
from memory_profiler import memory_usage
from greedy import fetch_game, get_distances, get_min_position

def get_h(game: np.array) -> int:
    # Defines the h value (distance to the end) for that game state

    h = 0
    for i in game:
        for j in i:
            if j == 0:
                h += 1

    return h

def get_fn(game_state: list, attempts: int) -> list:
    """ Creates a new list with:
       game_state[0] = game
       game_state[1] = h (distance to the end)
       game_state[2] = g (distance traveled)
       game_state[3] = f (h + g)
    """

    game_state[1] = get_h(game_state[0])
    game_state[2] = attempts
    game_state[3] = game_state[1] + game_state[2]

    return game_state

game = fetch_game('game.json')

def a_star_solve(game: np.array) -> np.array:
    distances = get_distances(game)
    game_states = list()

    state = [game, get_h(game), 0, get_h(game)]

    game_states.append(state)

    while 0 in game:
        #Gets the play position
        play_position = get_min_position(distances)

        attempts = 0
        for i in list_moves(state[0], play_position[0], play_position[1]):
            attempts += 1

            #Play the possible moves in that position
            state[0][play_position[0]][play_position[1]] = i

            # Inserts the value in the list and sorts it by its f(n) value
            game_states.append(get_fn(state, attempts))
            game_states.sort(key=lambda x: x[3])

            if a_star_solve(state[0]) is not None:
                # Gets the game state with the lowest h found
                return game_states[0][0]
            
            state[0][play_position[0]][play_position[1]] = 0
        # If no moves are available in that spot, returns None
        return None
    return state[0]

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