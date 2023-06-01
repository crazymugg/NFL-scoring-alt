import os
import csv
from .game import Game
from.team import Team


class App():
    def __init__(self):
        pass

    def run(self):
        self.create_teams()
        for root, _, files in os.walk('./src/data/misc', topdown=True, followlinks=False):
            for file in files:
                path = root + '/' + file
                game = Game(data=path)
                # new = path.split('/')
                # print(f'The Year was: {new[-3]}')
                # print(f'The Week was: {new[-2]}')
                # print(f'The Game was: {os.path.splitext(new[-1])[0]}')
                # if game.team_a == 'GNB' or game.team_b == 'GNB':
                if game.changed == True:
                    print(f'CHANGED OUTCOME: {game.team_a} vs {game.team_b}:{int(game.orgin_score_a)}-{int(game.orgin_score_b)} turns into {int(game.score_a)}-{int(game.score_b)}')
                else:
                    print(f'{game.team_a} vs {game.team_b}:{int(game.orgin_score_a)}-{int(game.orgin_score_b)} turns into {int(game.score_a)}-{int(game.score_b)}')
        print(Team.team_dict)
                

    def create_teams(self):
        with open("./src/data/teams.csv", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for i, row in enumerate(reader):
                team = Team(i, row)
                Team.team_dict[team.name] = team





class New():
    def __init__(self, data):
        self.id = ''
        self.year = ''
        self.week = ''
        self.number = ''
        self.team_a_name = ''
        self.team_b_name = ''
        self.team_a_orgin_score = ''
        self.team_b_origin_score = ''
        self.team_a_new_score = ''
        self.team_b_new_score = ''
        self.data = data
        self.calced = False


id = 'year-week-number'
res = {'year-week-number': 
        {'Team A': 'Falcons',
        'Team B': 'Saints',
        'Score A': '27',
        'Score B': '29',
        'New Score A': '54',
        'New Score B': '30', 
        'Data': ['GameData']
        }
    }


