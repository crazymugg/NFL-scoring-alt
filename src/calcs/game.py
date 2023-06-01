import csv
import os
from .team import Team
from .utils import convert_time, get_outcome


class Game():
    def __init__(self, data):
        self.data = data
        self.id = self.get_id()
        self.team_a: str
        self.team_b: str
        self.score_a = 0
        self.score_b = 0
        self.orgin_score_a = 0
        self.orgin_score_b = 0
        self.rate = 600
        self.seconds = 0
        self.changed = False
        self.read_data()
        self.change_records()


    def read_data(self):
        with open(self.data, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            for i, row in enumerate(reader):
                if i == 0:
                    self.team_a = row[-2]
                    self.team_b = row[-1]
                else:
                    if len(row) == 6:
                        quarter = row[0]
                        game_time = row[1]
                    elif len(row) == 5:
                        game_time = row[0]

                    sec = convert_time(quarter, game_time)
                    self.calc_score(sec)

                    self.orgin_score_a = int(row[-2])
                    self.orgin_score_b = int(row[-1])
            self.calc_score()


    def calc_score(self, sec=3600):
        difference = self.orgin_score_a - self.orgin_score_b
        area = difference * (sec-self.seconds)
        if difference > 0:
            self.score_a += area/self.rate
        elif area < 0:
            self.score_b -= area/self.rate
        self.seconds = sec


    def change_records(self):
        a = Team.team_dict[self.team_a]
        b = Team.team_dict[self.team_b]
        a.points_for += self.score_a
        a.points_against += self.score_b
        b.points_for += self.score_b
        b.points_against += self.score_a
        original_outcome = get_outcome(self.orgin_score_a, self.orgin_score_b)
        new_outcome = get_outcome(self.score_a, self.score_b, a, b)
        if original_outcome != new_outcome:
            self.changed = True
            a.difference -= original_outcome
            b.difference += original_outcome


    def get_id(self) -> str:
        path_list = self.data.split('/')
        year = path_list[-3]
        week = path_list[-2]
        num = os.path.splitext(path_list[-1])[0]
        # print(f'The Year was: {path_list[-3]}')
        # print(f'The Week was: {path_list[-2]}')
        # print(f'The Game was: {os.path.splitext(path_list[-1])[0]}')
        # return (year, week, num)
        return str(f'{year}.{week}.{num}')