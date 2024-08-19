import csv
from pprint import pprint

def catch_game(fp: str, game_number: int) -> list:
    with open(fp) as csvfile:
        game = []
        reader = csv.reader(csvfile)

        for key, csv_game in enumerate(reader):
            if key == (game_number + 1):
                row = []
                pprint(csv_game[0])
                for i in range(len(csv_game[0])):
                    if i == 0:
                        row.append(int(csv_game[0][i]))
                    elif (i % 9 == 0):
                        game.append(row)
                        row = []
                        row.append(int(csv_game[0][i]))
                    else:
                        row.append(int(csv_game[0][i]))
                game.append(row)

        return game

pprint(catch_game('archive/sudoku.csv', 0))
