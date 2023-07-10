from flask_sqlalchemy import SQLAlchemy

from .models import create_models


# def create_db(app):
class DataBase():
    def __init__(self, app):
        self.db = SQLAlchemy(app)
        self.Team, self.Game, self.Line = create_models(self.db)

    def get_models(self):
        models = {
            'Team': self.Team,
            'Game': self.Game,
            'Line': self.Line,
        }
        return models


    """ Section for team related functions"""
    def add_team(self, teamname):
        team = self.Team(name=teamname, wins=0, losses=0, ties=0, new_wins=0, new_losses=0, new_ties=0, difference=0)
        self.db.session.add(team)
        self.db.session.commit()
        print(f'Created team {teamname}')
        return team
    
    def search_team(self, teamname):
        team = self.Team.query.filter_by(name=teamname).first()
        print('Read Teams')
        return team

    def update_team(self, old_teamname, new_teamname):
        user = self.User.query.filter_by(name=old_teamname).first()
        user.name = str(new_teamname)
        self.db.session.add(user)
        self.db.session.commit()
        print('Updated Users')
        return user.username

    def delete_team(self, teamname):
        deleted_name = teamname
        user = self.User.query.filter_by(name=teamname).first()
        self.db.session.delete(user)
        self.db.session.commit()
        print('Deleted Users')
        return deleted_name
    

    """ Section for Game related functions"""
    def add_game(self, code, team_a_name, team_b_name, original_a_score, original_b_score):
        season, week, number = code.split('.')
        game = self.Game(code=code, season=season, week=week, number=number, team_a=team_a_name, team_b=team_b_name, original_score_a=original_a_score, original_score_b = original_b_score, new_score_a=0, new_score_b=0, different_result=False)
        self.db.session.add(game)
        self.db.session.commit()
        print(f'Created team {id}')
        return game
    
    def search_game(self, teamname):
        team = self.Team.query.filter_by(name=teamname).first()
        print('Read Teams')
        return team

    def update_game(self, old_teamname, new_teamname):
        user = self.User.query.filter_by(name=old_teamname).first()
        user.name = str(new_teamname)
        self.db.session.add(user)
        self.db.session.commit()
        print('Updated Users')
        return user.username

    def delete_game(self, teamname):
        deleted_name = teamname
        user = self.User.query.filter_by(name=teamname).first()
        self.db.session.delete(user)
        self.db.session.commit()
        print('Deleted Users')
        return deleted_name

    def reset_tables(self):
        self.db.drop_all()
        self.db.create_all()
        print('Reset Tables')


def create_db(app):
    db = DataBase(app)
    return db