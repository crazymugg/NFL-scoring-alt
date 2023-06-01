import csv
from .team import Team
from .utils import convert_time
from .utils import get_outcome


"""
This method is depreciated. It took the score and multiplied that by the amount of time left in the game.
"""
class Game():
    def __init__(self, data):
        self.data = data
        self.team_a: str
        self.team_b: str
        self.score_a: int = 0
        self.score_b: int = 0
        self.orgin_score_a:str
        self.orgin_score_b: str
        self.read_data()
        self.change_records()

    def read_data(self):
        with open(self.data, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            for i, row in enumerate(reader):
                if i == 0:
                    self.team_a = row[-2]
                    self.team_b= row[-1]
                else:
                    if len(row) == 6:
                        quarter = row[0]
                        time = row[1]
                    elif len(row) == 5:
                        time = row[0]

                    sec = convert_time(quarter, time)
                    self.score_a += int(row[-2]) * (sec /5000)
                    self.score_b += int(row[-1]) * (sec /5000)


                    self.orgin_score_a = int(row[-2])
                    self.orgin_score_b = int(row[-1])



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
            a.difference -= original_outcome
            b.difference += original_outcome





# Check orinignal outcome
# Check new outcome
# if different
# subtract old outcome
# add new outcome

"""
'team A wins'
'team A loses'
'draw'
"""