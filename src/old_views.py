import datetime

from flask import Blueprint, jsonify, render_template, request


views = Blueprint('views', __name__, template_folder='templates')

@views.route('/overview')
def view_overview():
    return render_template('overall.html')


@views.route('/season/<int:season_id>')
def view_season(season_id):
    return render_template('season.html')


@views.route('/team/<int:team_id>')
def view_team(team_id):
    return render_template('team.html')


@views.route('/game/<int:game_id>')
def view_game(game_id):
    game = int(game_id)
    # game = db.find_game(game_id)
    return render_template('game.html', game=game)


@views.route('/upload', methods=['POST'])
def view_upload():
    return render_template('upload.html')


@views.route('/score')
def view_score():
    return render_template('score.html')