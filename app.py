from flask import Flask, request, render_template, jsonify
from uuid import uuid4

from boggle import BoggleGame

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id
games = {}


@app.get("/")
def homepage():
    """Show board."""

    return render_template("index.html")


@app.post("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}."""

    # get a unique string id for the board we're creating
    game_id = str(uuid4())
    game = BoggleGame()
    games[game_id] = game

    # needs to return a JSON
    game_info = {"gameId": game_id, "board": game.board}
    # print('gameId', game_id, "board-game", game.board)

    # print('json newgame:', jsonify(game_info))
    return jsonify(game_info)

    # what we are returning
    # game_id 5b07d99f-3611-45c8-b88f-f2b06e3e47c4
    # board-game [['S', 'F', 'O', 'N', 'N'],
    #            ['I', 'T', 'A', 'N', 'O'],
    #            ['X', 'L', 'S', 'J', 'E'],
    #            ['R', 'U', 'F', 'E', 'X'],
    #            ['O', 'T', 'F', 'E', 'R']]