class Team():
    team_dict={}
    def __init__(self,id, data):
        self.id = id
        self.name = data[0]
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.orgin_wins = data[1]
        self.orgin_losses = data[2]
        self.orgin_ties = data[3]
        self.difference = 0
        self.points_for = 0
        self.points_against = 0


    def get_difference():
        pass

    def __repr__(self):
        return f'({self.wins}-{self.losses}-{self.ties} Diff:{self.difference})\n'