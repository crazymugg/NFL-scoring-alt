from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

from src.config import config
from .db import create_db


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db = create_db(app)
    # app.register_blueprint(views)

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')
    
    @app.route('/reset')
    def reset():
        db.reset_tables()
        return redirect('/')
    
    @app.route('/team/create/<teamname>')
    def create_team(teamname):
        team = db.search_team(teamname)
        if team == None:
            team = db.add_team(teamname)
            return render_template('created.html', team=team, exist=False)
        else:
            return render_template('created.html', team=team, exist=True)

    @app.route('/game/create')
    def create_game():
        game = db.add_game(code='2022.01.01', team_a_name='ATL', team_b_name='NOR', original_a_score=27, original_b_score=29)
        return render_template('created.html', team=game, exist=False)





    @app.route('/user/<username>')
    def show_user(username):
        user = db.search(username)
        # user = User.query.filter_by(username=str(username)).first_or_404()
        return render_template('read.html', user=user)


    @app.route('/overview')
    def view_overview():
        return render_template('overall.html')


    @app.route('/season/<int:season_id>')
    def view_season(season_id):
        return render_template('season.html')


    @app.route('/team/<int:team_id>')
    def view_team(team_id):
        return render_template('team.html')


    @app.route('/game/<int:game_id>')
    def view_game(game_id):
        game_id = int(game_id)
        game = db.find_game(game_id)
        return render_template('game.html', game=game)


    @app.route('/upload', methods=['POST'])
    def view_upload():
        return render_template('upload.html')


    @app.route('/score')
    def view_score():
        return render_template('score.html')

    return app


if __name__ == '__main__':
    # reset_tables()
    # create_user()
    # update_user()
    # read_user()
    # delete_user()
    # create_address()
    # read_user()
    app=create_app()
    app.run()