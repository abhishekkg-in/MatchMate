from flask import request, jsonify
from flask_restful import Resource
from app import db
from flasgger import swag_from
from app.models import Team, Player, Match, Area
import datetime

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
                            'country': {'type': 'string'},
                            'logo': {'type': 'string'}  # Include logo in the schema
                        }
                    }
                }
            }
        }
    })
    def get(self):
        teams = Team.query.all()
        return jsonify([{"id": team.id, "name": team.name, "country": team.country, "logo": team.logo} for team in teams])

    @swag_from({
        'parameters': [
            {
                'in': 'body',
                'name': 'body',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'team_name': {'type': 'string', 'description': 'Name of the team'},
                        'country': {'type': 'string', 'description': 'Country of the team'},
                        'logo': {'type': 'string', 'description': 'URL of the team logo'}
                    },
                    'required': ['team_name', 'country', 'logo'] # Make all fields required
                }
            }
        ],
        'responses': {
            201: {  # Use 201 Created for successful POST requests
                'description': 'Team added successfully',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string'},
                        'team': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'name': {'type': 'string'},
                                'country': {'type': 'string'},
                                'logo': {'type': 'string'}
                            }
                        }
                    }
                }
            },
            400: {
                'description': 'Bad Request. Missing required fields or invalid data.'
            }
        }
    })
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "No data provided"})

            team_name = data.get("team_name")
            country = data.get("country")
            logo = data.get("logo")

            if not team_name or not country or not logo: # Check all required fields
                return jsonify({"error": "team_name, country and logo are required"})

            new_team = Team(name=team_name, country=country, logo=logo)
            db.session.add(new_team)
            db.session.commit()

            return jsonify({"message": "Team added successfully", 'team': {'id': new_team.id, 'name': new_team.name, 'country': new_team.country, 'logo': new_team.logo}})

        except Exception as e:
            return jsonify({"error": str(e)}), 500 # Handle exceptions and return 500

   
class TeamResouceUpdateDelete(Resource):
    @swag_from({
        'parameters': [
            {
                'in': 'path',
                'name': 'team_id',
                'type': 'integer',
                'required': True,
                'description': 'ID of the team to update'
            },
            {
                'in': 'body',
                'name': 'body',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'team_name': {'type': 'string', 'description': 'Name of the team'},
                        'country': {'type': 'string', 'description': 'Country of the team'}
                    }
                }
            }
        ],
        'responses': {
            200: {
                'description': 'Team updated successfully',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string'},
                        'team': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'name': {'type': 'string'},
                                'country': {'type': 'string'}
                            }
                        }
                    }
                }
            },
            404: {
                'description': 'Team not found'
            },
            400: {
                'description': 'Bad Request. Invalid data provided.'
            }
        }
    })
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
            }), 200
        except Exception as e:
            return jsonify({"error": str(e)})

    @swag_from({
        'parameters': [
            {
                'in': 'path',
                'name': 'team_id',
                'type': 'integer',
                'required': True,
                'description': 'ID of the team to delete'
            }
        ],
        'responses': {
            200: {
                'description': 'Team deleted successfully',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string'}
                    }
                }
            },
            404: {
                'description': 'Team not found'
            }
        }
    })
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
        'parameters': [
            {
                'in': 'query',
                'name': 'name',
                'type': 'string',
                'description': 'Name of the player to search'
            }
        ],
        'responses': {
            200: {
                'description': 'List of players',
                'schema': {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer'},
                            'name': {'type': 'string'},
                            'position': {'type': 'string'},
                            'club': {'type': 'string'},
                            'nationality': {'type': 'string'},
                            'avatar': {'type': 'string'}
                        }
                    }
                }
            },
            500: {
                'description': 'Internal Server Error. Some team details not found.'
            }
        }
    })
    def get(self):
        try:
            name_param = request.args.get('name')
            players = Player.query

            if name_param and name_param.strip():
                players = players.filter(Player.name.like(f"%{name_param}%"))

            players = players.all()

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
                    return jsonify({"error": "Some team details not found"})

            return jsonify(player_list)

        except Exception as e:
            print(f"Error in get method: {str(e)}")
            return jsonify({"error": str(e)})

    @swag_from({
        'parameters': [
            {
                'in': 'body',
                'name': 'body',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'name': {'type': 'string', 'description': 'Name of the player'},
                        'team_id': {'type': 'integer', 'description': 'ID of the player\'s team'},
                        'position': {'type': 'string', 'description': 'Position of the player'},
                        'avatar': {'type': 'string', 'description': 'URL of the player\'s avatar'}
                    },
                    'required': ['name', 'team_id']
                }
            }
        ],
        'responses': {
            201: {
                'description': 'Player added successfully',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string'},
                        'player': {
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
            },
            400: {
                'description': 'Bad Request. Missing required fields.'
            },
            500: {
                'description': 'Internal Server Error.'
            }
        }
    })
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "No data provided"})

            name = data.get("name")
            team_id = data.get("team_id")
            position = data.get("position")
            avatar = data.get("avatar")

            if not name or not team_id:
                return jsonify({"error": "Name and team_id are required"})

            new_player = Player(name=name, team_id=team_id, position=position, avatar=avatar)
            db.session.add(new_player)
            db.session.commit()

            return jsonify({"message": "Player added successfully", 'player': {'id': new_player.id, 'name': new_player.name, 'team_id': new_player.team_id, 'position': new_player.position, 'avatar': new_player.avatar}})

        except Exception as e:
            return jsonify({"error": str(e)})

    
class PlayerResourceUpdateDelete(Resource):
    @swag_from({
        'parameters': [
            {
                'in': 'path',
                'name': 'player_id',
                'type': 'integer',
                'required': True,
                'description': 'ID of the player to update'
            },
            {
                'in': 'body',
                'name': 'body',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'name': {'type': 'string', 'description': 'Name of the player'},
                        'team_id': {'type': 'integer', 'description': 'ID of the player\'s team'},
                        'position': {'type': 'string', 'description': 'Position of the player'},
                        'avatar': {'type': 'string', 'description': 'URL of the player\'s avatar'}
                    }
                }
            }
        ],
        'responses': {
            200: {
                'description': 'Player updated successfully',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string'},
                        'player': {
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
            },
            404: {
                'description': 'Player not found'
            },
            500: {
                'description': 'Internal Server Error.'
            }
        }
    })
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
            }), 200

        except Exception as e:
            return jsonify({"error": str(e)})

    @swag_from({
        'parameters': [
            {
                'in': 'path',
                'name': 'player_id',
                'type': 'integer',
                'required': True,
                'description': 'ID of the player to delete'
            }
        ],
        'responses': {
            200: {
                'description': 'Player deleted successfully',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string'}
                    }
                }
            },
            404: {
                'description': 'Player not found'
            },
            500: {
                'description': 'Internal Server Error.'
            }
        }
    })
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
                'description': 'List all matches',
                'schema': {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer'},
                            'homeTeam': {'type': 'string'},
                            'awayTeam': {'type': 'string'},
                            'homeLogo': {'type': 'string'},
                            'awayLogo': {'type': 'string'},
                            'score': {'type': 'string'},
                            'date': {'type': 'string', 'format': 'date'},  # Specify date format
                            'stadium': {'type': 'string'},
                            'status': {'type': 'string'}
                        }
                    }
                }
            },
            500: {
                'description': 'Internal Server Error. Some team details not found.'
            }
        }
    })
    def get(self):
        try:
            matches = Match.query.all()
            match_list = []

            for match in matches:
                home_team = Team.query.get(match.home_team)
                away_team = Team.query.get(match.away_team)

                if home_team and away_team:
                    match_data = {
                        "id": match.id,
                        "homeTeam": home_team.name,
                        "awayTeam": away_team.name,
                        "homeLogo": home_team.logo,
                        "awayLogo": away_team.logo,
                        "score": match.score if match.score else "-",
                        "date": match.date.strftime("%Y-%m-%d") if match.date else None,
                        "stadium": match.location,
                        "status": match.status.capitalize() if match.status else None
                    }
                    match_list.append(match_data)
                else:
                    print(f"Error: Team not found for match ID {match.id}")
                    return jsonify({"error": "Some team details not found"}), 500

            return jsonify(match_list)

        except Exception as e:
            print(f"Error in get method: {str(e)}")
            return jsonify({"error": str(e)}), 500

    @swag_from({
        'parameters': [
            {
                'in': 'body',
                'name': 'body',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'home_team': {'type': 'integer', 'description': 'ID of the home team'},
                        'away_team': {'type': 'integer', 'description': 'ID of the away team'},
                        'date': {'type': 'string', 'format': 'date', 'description': 'Date of the match (ISO format)'},
                        'location': {'type': 'string', 'description': 'Location of the match'},
                        'status': {'type': 'string', 'description': 'Status of the match'},
                        'score': {'type': 'string', 'description': 'Score of the match'}
                    },
                    'required': ['home_team', 'away_team', 'date']
                }
            }
        ],
        'responses': {
            201: {
                'description': 'Match added successfully',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string'},
                        'match': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'home_team': {'type': 'integer'},
                                'away_team': {'type': 'integer'},
                                'date': {'type': 'string', 'format': 'date'},
                                'location': {'type': 'string'},
                                'status': {'type': 'string'},
                                'score': {'type': 'string'}
                            }
                        }
                    }
                }
            },
            400: {
                'description': 'Bad Request. Missing required fields or invalid data.'
            },
            500: {
                'description': 'Internal Server Error.'
            }
        }
    })
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "No data provided"}), 400

            home_team = data.get("home_team")
            away_team = data.get("away_team")
            date = data.get("date")
            location = data.get("location")
            status = data.get("status")
            score = data.get("score")

            if not home_team or not away_team or not date:
                return jsonify({"error": "home_team, away_team, and date are required"}), 400

            date_obj = datetime.datetime.fromisoformat(date.replace("Z", "+00:00"))

            new_match = Match(home_team=home_team, away_team=away_team, date=date_obj, location=location, status=status, score=score)
            db.session.add(new_match)
            db.session.commit()

            return jsonify({"message": "Match added successfully", 'match': {'id': new_match.id, 'home_team': new_match.home_team, 'away_team': new_match.away_team, 'date': new_match.date.isoformat(), 'location': new_match.location, 'status': new_match.status, 'score': new_match.score}}), 201

        except Exception as e:
            return jsonify({"error": str(e)}), 500
    

class MatchResourceUpdateDelete(Resource):
    @swag_from({
        'parameters': [
            {
                'in': 'path',
                'name': 'match_id',
                'type': 'integer',
                'required': True,
                'description': 'ID of the match to update'
            },
            {
                'in': 'body',
                'name': 'body',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'home_team': {'type': 'integer', 'description': 'ID of the home team'},
                        'away_team': {'type': 'integer', 'description': 'ID of the away team'},
                        'date': {'type': 'string', 'format': 'date', 'description': 'Date of the match (ISO format)'},
                        'location': {'type': 'string', 'description': 'Location of the match'},
                        'status': {'type': 'string', 'description': 'Status of the match'},
                        'score': {'type': 'string', 'description': 'Score of the match'}
                    }
                }
            }
        ],
        'responses': {
            200: {
                'description': 'Match updated successfully',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string'},
                        'match': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'home_team': {'type': 'integer'},
                                'away_team': {'type': 'integer'},
                                'date': {'type': 'string', 'format': 'date'},
                                'location': {'type': 'string'},
                                'status': {'type': 'string'},
                                'score': {'type': 'string'}
                            }
                        }
                    }
                }
            },
            404: {
                'description': 'Match not found'
            },
            400: {
                'description': 'Bad Request. Invalid data provided.'
            },
            500: {
                'description': 'Internal Server Error.'
            }
        }
    })
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
            }), 200

        except Exception as e:
            return jsonify({"error": str(e)})

    @swag_from({
        'parameters': [
            {
                'in': 'path',
                'name': 'match_id',
                'type': 'integer',
                'required': True,
                'description': 'ID of the match to delete'
            }
        ],
        'responses': {
            200: {
                'description': 'Match deleted successfully',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string'}
                    }
                }
            },
            404: {
                'description': 'Match not found'
            },
            500: {
                'description': 'Internal Server Error.'
            }
        }
    })
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
    api.add_resource(TeamResource, '/teams')
    api.add_resource(TeamResouceUpdateDelete, '/teams/<int:team_id>')
    api.add_resource(PlayerResource, '/players')
    api.add_resource(PlayerResourceUpdateDelete,'/players/<int:team_id>')
    api.add_resource(MatchResource, '/matches')
    api.add_resource(MatchResourceUpdateDelete,'/matches/<int:team_id>')
    api.add_resource(AreaResource, '/areas')
