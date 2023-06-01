from cgi import print_form
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///test.db', echo=True)
Base = declarative_base()


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    season = Column(Integer)
    week = Column(Integer)
    number = Column(Integer)
    team_a = Column(String, ForeignKey('teams.name'))
    team_b = Column(String, ForeignKey('teams.name'))
    original_score_a = Column(Integer)
    original_score_b = Column(Integer)
    new_score_a = Column(Integer)
    new_score_b = Column(Integer)
    different_result = Column(Boolean)
    rate = 600
    seconds = 0


    def read_data(self):
        pass

    def calc_score(self):
        pass

    def change_record(self):
        pass

    def get_id(self):
        pass



class Line(Base):
    __tablename__ = 'lines'
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id'))
    quarter = Column(Integer)
    time = Column(Integer)
    team_a_score = Column(Integer)
    team_b_score = Column(Integer)
    game = relationship('Game', back_populates='Lines')



Game.lines = relationship('Lines', order_by=Line.id, back_populates='game_id')

Base.metadata.create_all(engine)


# session = sessionmaker(engine)()
# game1 = Game(id=202211, season=2022, week=1, number=1, team_a='ATL', team_b='NOR', original_score_a=27, original_score_b=29, new_score_a=45, new_score_b=0, different_result=True)
# session.add(game1)
# session.commit()