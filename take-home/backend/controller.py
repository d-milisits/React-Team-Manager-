from flask import Flask, jsonify, request
from flask_cors import CORS
from Coach import Coach
from Player import Player
from Team import Team

app = Flask(__name__)
CORS(app)

@app.route("/api/teams", methods=["GET"])
def view_teams():
  teams = Team.view_teams()
  return jsonify({"teams":teams})
  # Returns list of Team names obtained from SQL and sends them back to front-end in view teams tab. 

@app.route("/api/add", methods=["POST"])
def add_team():
  data = request.get_json()
  coach = data.get("coach")
  name = data.get("name")
  # Retrieves coach and name variables sent from react POST request. These variable names must match key names in React JSON post request. 
  new_coach = Coach(name=coach)
  # Create new coach for given team-- create team functions assumes you have a coach object created (as you require a coach_id (pk))
  new_coach.insert()
  coach_id = new_coach.pk
  new_team = Team(name=name, coach_id=coach_id)
  new_team.insert()
  # Create new team and insert into DB.
  return jsonify({"success":True})
  # This function obtains coach & team name from React front-end in JSON form and creates new rows in DB with inputted information. 

@app.route("/api/add_player", methods=["POST"])
def add_player():
  data = request.get_json()
  player = data.get("player")
  team = data.get("team")
  # Retrieves coach and name variables sent from react POST request. These variable names must match key names in React JSON post request. 
  team_id = Team.pk_by_name(team)
  # Player constructor assumes team already exists. Need to obtain team ID (pk) in order to create a new player. 
  # print("THE TEAM ID IS", team_id)
  new_player = Player(name=player, team_id=team_id[0])
  new_player.insert()
  return jsonify({"success":True})
  # This function obtains player & team name from React front-end in JSON form and creates new row in player DB with inputted information. 

@app.route("/api/players", methods=["POST"])
def view_players():
  data = request.get_json()
  team = data.get("team")
  team_id = Team.pk_by_name(team)
  player_list = Player.view_players(team_id[0])
  # pk_by_name returns a tuple (e.g. (1,0) and must be accessed via index values.)
  return jsonify({"players":player_list})
  # Obtains player names from database -- requires team ID (pk). Gets team name from React front-end and uses PK of team to obtain information. 

@app.route("/api/remove_player", methods=["POST"])
def remove_player():
  data = request.get_json()
  player = data.get("player")
  Player.remove_player(player)
  return jsonify({"success":True})
  # Obtains player name from front-end and removes player from db where name=input. 

if __name__ == "__main__":
  app.run(debug=True)
  # RUN FLASK ROUTE AND NPM START FRONT-END TO TEST! Must install node-modules with npm install in frontend directory as well.
  # Run schema.py as well (IN BACKEND DIRECTORY) in order to create the database file. 