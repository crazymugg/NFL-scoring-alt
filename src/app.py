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
                # if game.team_a == 'GNB' or game.team_b == 'GNB':
                if game.changed == True:
                    print(f'CHANGED OUTCOME: {game.team_a} vs {game.team_b}:{int(game.orgin_score_a)}-{int(game.orgin_score_b)} turns into {int(game.score_a)}-{int(game.score_b)}')
                else:
                    print(f'{game.team_a} vs {game.team_b}:{int(game.orgin_score_a)}-{int(game.orgin_score_b)} turns into {int(game.score_a)}-{int(game.score_b)}')
        print(Team.team_dict)
                

    def create_teams(self):
        with open("teams.csv", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for i, row in enumerate(reader):
                team = Team(i, row)
                Team.team_dict[team.name] = team

