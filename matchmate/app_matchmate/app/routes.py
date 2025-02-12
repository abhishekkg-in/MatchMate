from flask import request, jsonify
from flask_restful import Resource
from app import db
from flasgger import swag_from
from app.models import Team, Player, Match, Area

class TeamResource(Resource):
    @swag_from({
        'responses': {
            200: {
                'description': 'List all teams',
                'schema': {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer'},
                            'name': {'type': 'string'},
                            'country': {'type': 'string'}
                        }
                    }
                }
            }
        }
    })
    def get(self):
        teams = Team.query.all()
        # return jsonify({"Working": "hhhhhh"})
        return jsonify([{"id": team.id, "name": team.name, "country": team.country, "logo": team.logo} for team in teams])

    
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "No data provided"})
            
            team_name = data.get("team_name")
            country = data.get("country")
            logo = data.get("logo")

            new_team = Team(name=team_name, country=country, logo=logo)
            db.session.add(new_team)
            db.session.commit()

            if not team_name:
                return jsonify({"error": "team_name is required"})
            
            print(new_team.logo)
            
            return jsonify({"message": "Team added successfully", 'team': {'id': new_team.id, 'name': new_team.name, 'country': new_team.country, 'logo': new_team.logo}})
        except:
            return jsonify({"message": data})

    
    def put(self, team_id):
        try:
            team = Team.query.get(team_id)
            if not team:
                return jsonify({"error": "Team not found"})

            data = request.get_json()
            team.name = data.get("team_name", team.name)
            team.country = data.get("country", team.country)

            db.session.commit()

            return jsonify({
                "message": "Team updated successfully", 
                "team": {'id': team.id, 'name': team.name, 'country': team.country}
            })
        except Exception as e:
            return jsonify({"error": str(e)})

    def delete(self, team_id):
        try:
            team = Team.query.get(team_id)
            if not team:
                return jsonify({"error": "Team not found"})

            db.session.delete(team)
            db.session.commit()

            return jsonify({"message": "Team deleted successfully"})
        except Exception as e:
            return jsonify({"error": str(e)})


class PlayerResource(Resource):
    @swag_from({
        'responses': {
            200: {
                'description': 'List all players',
                'schema': {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer'},
                            'name': {'type': 'string'},
                            'team_id': {'type': 'integer'},
                            'position': {'type': 'string'},
                            'avatar': {'type': 'string'}
                        }
                    }
                }
            }
        }
    })
    def get(self):
        try:
            name_param = request.args.get('name')  # Get the 'name' query parameter
            players = Player.query  # Start with the base query

            if name_param:  # If a name parameter is provided
                if name_param.strip(): # Check if the name parameter is not empty or just spaces
                    players = players.filter(Player.name.like(f"%{name_param}%"))  # Filter by name (case-insensitive)
                #else: #if name param is empty string return all the players
                    #players = Player.query.all()
            
            players = players.all() # Execute the query after filtering

            player_list = []
            for player in players:
                team = Team.query.get(player.team_id)

                if team:
                    player_data = {
                        "id": player.id,
                        "name": player.name,
                        "position": player.position,
                        "club": team.name,
                        "nationality": team.country,
                        "avatar": player.avatar
                    }
                    player_list.append(player_data)
                else:
                    print(f"Error: Team not found for player ID {player.id}")
                    return jsonify({"error": "Some team details not found"}), 500

            return jsonify(player_list)

        except Exception as e:
            print(f"Error in get method: {str(e)}")
            return jsonify({"error": str(e)}), 500
    # def get(self):
        # team_id = request.args.get('team_id')
        # query = Player.query
        # if team_id:
        #     query = query.filter_by(team_id=team_id)
        # players = query.all()
        # return jsonify([{"id": player.id, "name": player.name, "position": player.position, "team": player.team_id, "avatar":player.avatar} for player in players])
    
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "No data provided"})

            name = data.get("name")
            team_id = data.get("team_id")
            position = data.get("position")
            avatar = data.get("avatar")

            if not name or not team_id:  # Important: Validate required fields
                return jsonify({"error": "Name and team_id are required"})

            new_player = Player(name=name, team_id=team_id, position=position, avatar=avatar)
            db.session.add(new_player)
            db.session.commit()

            return jsonify({"message": "Player added successfully", 'player': {'id': new_player.id, 'name': new_player.name, 'team_id': new_player.team_id, 'position': new_player.position, 'avatar': new_player.avatar}})
        except Exception as e:
            return jsonify({"error": str(e)})  # Better error handling
    
    def put(self, player_id):
        try:
            player = Player.query.get(player_id)
            if not player:
                return jsonify({"error": "Player not found"})

            data = request.get_json()
            player.name = data.get("name", player.name)
            player.team_id = data.get("team_id", player.team_id)
            player.position = data.get("position", player.position)
            player.avatar = data.get("avatar", player.avatar)

            db.session.commit()

            return jsonify({
                "message": "Player updated successfully",
                "player": {'id': player.id, 'name': player.name, 'team_id': player.team_id, 'position': player.position, 'avatar': player.avatar}
            })
        except Exception as e:
            return jsonify({"error": str(e)})
    
    def delete(self, player_id):
        try:
            player = Player.query.get(player_id)
            if not player:
                return jsonify({"error": "Player not found"})

            db.session.delete(player)
            db.session.commit()

            return jsonify({"message": "Player deleted successfully"})
        except Exception as e:
            return jsonify({"error": str(e)})
        

class MatchResource(Resource):
    @swag_from({
        'responses': {
            200: {
                'description': 'List all players',
                'schema': {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer'},
                            'name': {'type': 'string'},
                            'team_id': {'type': 'integer'},
                            'position': {'type': 'string'},
                            'avatar': {'type': 'string'}
                        }
                    }
                }
            }
        }
    })
    def get(self):
        try:
            matches = Match.query.all()  # Get all matches from the database
            match_list = []

            for match in matches:
                home_team = Team.query.get(match.home_team)  # Get home team details
                away_team = Team.query.get(match.away_team)  # Get away team details

                if home_team and away_team: # Check if both teams exist
                    match_data = {
                        "id": match.id,
                        "homeTeam": home_team.name,
                        "awayTeam": away_team.name,
                        "homeLogo": home_team.logo,
                        "awayLogo": away_team.logo,
                        "score": match.score if match.score else "-", # Handle cases where score might be None
                        "date": match.date.strftime("%Y-%m-%d") if match.date else None,  # Format date
                        "stadium": match.location,
                        "status": match.status.capitalize() if match.status else None # Capitalize status if it exists
                    }
                    match_list.append(match_data)
                else:
                    # Handle the case where a team is not found (e.g., log an error)
                    print(f"Error: Team not found for match ID {match.id}")
                    return jsonify({"error": "Some team details not found"}), 500 #return error with 500 status code

            return jsonify(match_list)

        except Exception as e:
            print(f"Error in get method: {str(e)}") # Print for debugging
            return jsonify({"error": str(e)}), 500  # Return a 500 Internal Server Error
        # area_id = request.args.get('area_id')
        # query = Match.query
        # if area_id:
        #     query = query.filter_by(location=area_id)
        # matches = query.all()
        # return jsonify([{"id": match.id, "home_team": match.home_team, "away_team": match.away_team, "date": match.date, "location": match.location, "status": match.status, "score": match.score} for match in matches])
    
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "No data provided"})

            home_team = data.get("home_team")
            away_team = data.get("away_team")
            date = data.get("date") # Expecting ISO format string
            location = data.get("location")
            status = data.get("status")
            score = data.get("score")

            if not home_team or not away_team or not date:
                return jsonify({"error": "home_team, away_team, and date are required"})

            import datetime  # Import datetime for parsing
            date_obj = datetime.datetime.fromisoformat(date.replace("Z", "+00:00"))  # Parse ISO date

            new_match = Match(home_team=home_team, away_team=away_team, date=date_obj, location=location, status=status, score=score)
            db.session.add(new_match)
            db.session.commit()

            return jsonify({"message": "Match added successfully", 'match': {'id': new_match.id, 'home_team': new_match.home_team, 'away_team': new_match.away_team, 'date': new_match.date.isoformat(), 'location': new_match.location, 'status': new_match.status, 'score': new_match.score}})
        except Exception as e:
            return jsonify({"error": str(e)})

    def put(self, match_id):
        try:
            match = Match.query.get(match_id)
            if not match:
                return jsonify({"error": "Match not found"})

            data = request.get_json()
            match.home_team = data.get("home_team", match.home_team)
            match.away_team = data.get("away_team", match.away_team)
            date_str = data.get("date")
            if date_str:
                date_obj = datetime.datetime.fromisoformat(date_str.replace("Z", "+00:00"))
                match.date = date_obj
            match.location = data.get("location", match.location)
            match.status = data.get("status", match.status)
            match.score = data.get("score", match.score)

            db.session.commit()

            return jsonify({
                "message": "Match updated successfully",
                "match": {'id': match.id, 'home_team': match.home_team, 'away_team': match.away_team, 'date': match.date.isoformat(), 'location': match.location, 'status': match.status, 'score': match.score}
            })
        except Exception as e:
            return jsonify({"error": str(e)})

    def delete(self, match_id):
        try:
            match = Match.query.get(match_id)
            if not match:
                return jsonify({"error": "Match not found"})

            db.session.delete(match)
            db.session.commit()

            return jsonify({"message": "Match deleted successfully"})
        except Exception as e:
            return jsonify({"error": str(e)})

class AreaResource(Resource):
    def get(self):
        areas = Area.query.all()
        return jsonify([{"id": area.id, "name": area.name} for area in areas])

def register_routes(api):
    api.add_resource(TeamResource, '/teams', '/teams/<int:team_id>')
    api.add_resource(PlayerResource, '/players', '/players/<int:team_id>')
    api.add_resource(MatchResource, '/matches', '/matches/<int:team_id>')
    api.add_resource(AreaResource, '/areas')
