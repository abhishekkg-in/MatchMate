from app import db
from app.models import Team, Player, Match
from datetime import datetime


datas = [
  {
    "home_team": 1,  
    "away_team": 6,  
    "date": "2024-03-15T15:00:00Z",
    "location": "Old Trafford",
    "status": "upcoming"
  },
  {
    "home_team": 2,  
    "away_team": 7,  
    "date": "2024-04-20T18:00:00Z",
    "location": "Santiago Bernabeu",
    "status": "upcoming"
  },
  {
    "home_team": 3, 
    "away_team": 8, 
    "date": "2024-05-05T16:30:00Z",
    "location": "Allianz Arena",
    "status": "upcoming"
  },
  {
    "away_team": 9,  
    "home_team": 4,  
    "date": "2024-03-22T19:45:00Z",
    "location": "Allianz Stadium",
    "status": "upcoming"
  },
  {
    "away_team": 10, 
    "home_team": 5,  
    "date": "2024-04-12T20:00:00Z",
    "location": "Parc des Princes",
    "status": "upcoming"
  },
    {
    "home_team": 6,  
    "away_team": 1, 
    "date": "2024-01-01T15:00:00Z", 
    "location": "Anfield",
    "status": "completed",
        "score": "2-1"
  },
  {
    "home_team": 7,  
    "away_team": 2, 
    "date": "2023-12-25T18:00:00Z",
    "location": "Camp Nou",
    "status": "completed",
        "score": "0-0"
  },
  {
    "home_team": 8, 
    "away_team": 3,  
    "date": "2023-11-10T16:30:00Z",
    "location": "Signal Iduna Park",
    "status": "completed",
        "score": "1-3"
  },
  {
    "home_team": 9,  
    "away_team": 4,  
    "date": "2023-10-28T19:45:00Z",
    "location": "San Siro",
    "status": "completed",
        "score": "2-2"
  },
  {
    "home_team": 10, 
    "away_team": 5,  
    "date": "2023-09-15T20:00:00Z",
    "location": "Stade Vélodrome",
    "status": "completed",
        "score": "0-2"
  }
]


players_data = [
  {
    "name": "Lionel Messi",
    "team_id": 7, 
    "position": "Forward",
    "avatar": "https://upload.wikimedia.org/wikipedia/commons/b/b4/Lionel-Messi-Argentina-2022.jpg" 
  },
  {
    "name": "Cristiano Ronaldo",
    "team_id": 1,  
    "position": "Forward",
    "avatar": "https://upload.wikimedia.org/wikipedia/commons/8/8c/Cristiano_Ronaldo_8x10.jpg"
  },
  {
    "name": "Kylian Mbappé",
    "team_id": 5, 
    "position": "Forward",
    "avatar": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Mbapp%C3%A9_2018.jpg/800px-Mbapp%C3%A9_2018.jpg"
  },
  {
    "name": "Erling Haaland",
    "team_id": 3, 
    "position": "Forward",
    "avatar": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Erling_Haaland_2023.jpg/800px-Erling_Haaland_2023.jpg"
  },
  {
    "name": "Kevin De Bruyne",
    "team_id": 6,  
    "position": "Midfielder",
    "avatar": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Kevin_De_Bruyne_2018.jpg/800px-Kevin_De_Bruyne_2018.jpg"
  },
  {
    "name": "Mohamed Salah",
    "team_id": 6, 
    "position": "Forward",
    "avatar": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Mohamed_Salah_2018.jpg/800px-Mohamed_Salah_2018.jpg"
  },
  {
    "name": "Neymar Jr.",
    "team_id": 5, 
    "position": "Forward",
    "avatar": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Neymar_Jr._%28cropped%29.jpg/800px-Neymar_Jr._%28cropped%29.jpg"
  },
  {
    "name": "Robert Lewandowski",
    "team_id": 7, 
    "position": "Forward",
    "avatar": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Robert_Lewandowski_2023.jpg/800px-Robert_Lewandowski_2023.jpg"
  },
    {
    "name": "Vinícius Júnior",
    "team_id": 2, 
    "position": "Forward",
    "avatar": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Vin%C3%ADcius_J%C3%BAnior_2023.jpg/800px-Vin%C3%ADcius_J%C3%BAnior_2023.jpg"
  },
    {
    "name": "Jude Bellingham",
    "team_id": 2,
    "position": "Midfielder",
    "avatar": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Jude_Bellingham_2023.jpg/800px-Jude_Bellingham_2023.jpg"
  }
]



for data in datas:
    home_team = data.get("home_team")
    away_team = data.get("away_team")
    date = data.get("date") # Expecting ISO format string
    location = data.get("location")
    status = data.get("status")
    score = data.get("score")
    print(home_team, away_team, status, score)
    new_match = Match(home_team=home_team, away_team=away_team, date=date, location=location, status=status, score=score)
    db.session.add(new_match)
    db.session.commit()

