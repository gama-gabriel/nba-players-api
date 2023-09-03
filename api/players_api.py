from flask import Flask, json, jsonify
from os.path import join

app = Flask(__name__)
app.json.sort_keys = False 

@app.route('/')
def guia():
    return 'Set the url to /players or /player_images to get the results'

@app.route('/players/', methods = ['GET'])
def get_players():
    with open ('dados/players.json', 'r') as file:
        players = json.load(file)
        return jsonify(players)

@app.route('/player_images/', methods = ['GET'])
def get_player_images():
    with open ('dados/player_images.json', 'r') as file:
        player_images = json.load(file)
        return jsonify(player_images)

if __name__ == '__main__':
    app.run()