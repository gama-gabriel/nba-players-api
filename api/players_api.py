from flask import Flask, make_response, jsonify
from flask_cors import CORS, cross_origin
from db import Players, Player_images

app = Flask(__name__)
cors = CORS(app)
app.json.sort_keys = False 

@app.route('/players', methods = ['GET'])
@cross_origin()
def get_players():
    return make_response(jsonify(Players))

@app.route('/player_images', methods = ['GET'])
@cross_origin()
def get_player_images():
    return make_response(jsonify(Player_images))

if __name__ == '__main__':
    app.run(debug = True, port=8000)