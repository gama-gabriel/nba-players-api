from flask import Flask, json, jsonify
from os.path import join
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.json.sort_keys = False 

@app.route('/')
def guia():
    return 'Set the url to /players, /player_images or /teams to get the results'

@app.route('/players/', methods = ['GET'])
@cross_origin()
def get_players():
    with open ('dados/players.json', 'r') as file:
        players = json.load(file)
        return jsonify(players)

@app.route('/player_images/', methods = ['GET'])
@cross_origin()
def get_player_images():
    with open ('dados/player_images.json', 'r') as file:
        player_images = json.load(file)
        return jsonify(player_images)
    
@app.route('/teams/', methods = ['GET'])
@cross_origin()
def get_teams():
    with open ('dados/teams.json', 'r') as file:
        player_images = json.load(file)
        return jsonify(player_images)

if __name__ == '__main__':
    app.run()