def create_models(db):

    # tags = db.Table('tags',
    #                 db.Column('tag_id', db.Integer, db.ForeignKey('tag_id'), primary_key=True),
    #                 db.Column('page_id', db.Integer, db.ForeignKey('page_id'), primary_key=True))

    # class Page(db.Model):
    #     id = db.Column(db.Integer, primary_key = True)
    #     tags = db.relationship('Tag', lazy='subquery', backref=db.backref('pages', lazy=True))

    # class Tag(db.Model):
    #     id = db.Column(db.Integer, primary_key=True)


    team_table = db.Table('teams_in_games',
        db.Column('game_id', db.Integer, db.ForeignKey('game.id'), primary_key = True),
        db.Column('team_id', db.Integer, db.ForeignKey('team.id'), primary_key = True))

    class Team(db.Model):
        id = db.Column(db.Integer, primary_key=True, unique=True)
        name = db.Column(db.String(3), nullable=False, unique=True)
        wins = db.Column(db.Integer)
        losses = db.Column(db.Integer)
        ties = db.Column(db.Integer)
        new_wins = db.Column(db.Integer)
        new_losses = db.Column(db.Integer)
        new_ties = db.Column(db.Integer)
        difference = db.Column(db.Integer)
        games = db.relationship('Game', secondary=team_table, backref=db.backref('team', lazy=True))

        def __repr__(self):
            return f'{self.name}'


    class Game(db.Model):
        id = db.Column(db.Integer, primary_key=True, unique=True)
        code = db.Column(db.String, unique=True)
        season = db.Column(db.String, nullable=False)
        week = db.Column(db.String, nullable=False)
        number = db.Column(db.String, nullable=False)
        # team_a = db.Column(db.String(40), nullable=False) #foreign Key
        team_a = db.Column(db.String(3), db.ForeignKey('team.name'), nullable=False)
        # team_b = db.Column(db.String(40), nullable=False) # Foreign Key
        team_b = db.Column(db.String(3), db.ForeignKey('team.name'), nullable=False)
        original_score_a = db.Column(db.Integer, nullable=False)
        original_score_b = db.Column(db.Integer, nullable=False)
        new_score_a = db.Column(db.Integer)
        new_score_b = db.Column(db.Integer)
        different_result = db.Column(db.Boolean)
        lines = db.relationship('Line', backref='game', lazy=True)
        rate = 600
        seconds = 0

        def __repr__(self):
            return f'{self.id}'
        
        def read_data(self):
            pass

        def calc_score(self):
            pass

        def change_record(self):
            pass

        def get_id(self):
            pass


    class Line(db.Model):
        id = db.Column(db.Integer, primary_key=True, unique=True)
        game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
        quarter = db.Column(db.Integer)
        time = db.Column(db.Integer)
        team_a_score = db.Column(db.Integer)
        team_b_score = db.Column(db.Integer)

        def __repr__(self):
            return f'{self.id} for game {self.game_id}'





    return (Team, Game, Line)
