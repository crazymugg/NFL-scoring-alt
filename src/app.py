import os
import csv
from .game import Game
from.team import Team


class App():
    def __init__(self):
        pass

    def run(self):
        self.create_teams()
        for root, _, files in os.walk('./data', topdown=True, followlinks=False):
            for file in files:
                path = root + '/' + file
                game = Game(data=path)
                # print(path)
                if game.team_a == 'GNB' or game.team_b == 'GNB':
                    print(f'The original was: {int(game.orgin_score_a)} {game.team_a} to {int(game.orgin_score_b)} {game.team_b}')
                    print(f'The new final is: {int(game.score_a)} {game.team_a} to {int(game.score_b)} {game.team_b}')
        print(Team.team_dict)
                

    def create_teams(self):
        with open("teams.csv", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for i, row in enumerate(reader):
                team = Team(i, row)
                Team.team_dict[team.name] = team

