from app import db

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    logo = db.Column(db.String(200))

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    position = db.Column(db.String(50))
    avatar = db.Column(db.String(300), nullable=True)
    


class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    home_team = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    away_team = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100))
    status = db.Column(db.String(50), nullable=True)
    score = db.Column(db.String(50), nullable=True)

class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
