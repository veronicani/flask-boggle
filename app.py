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

@app.post("/api/score-word")
def score_word():
    """"""
    # AJAX request, contains body JSON w/ game id and word
    # access the game id and word from the request body
    request_data = request.get_json()
    print('request_data: ', request_data)
    
    game_id = request_data.get("gameId")
    word = request_data.get("word")
    print('game_id: ', game_id, "word: ", word)
    # debugger()

    #check if the word is legal
        # check if word is in word list
        # check if word is in the board
    current_game = games[game_id]
    # TODO: split into separate if statements
    if (current_game.is_word_in_word_list(word) and 
        current_game.check_word_on_board(word)):
        # return jsonify({result: "ok"})
    # if not on board: {result: "not-on-board"}
    # if a valid word: {result: "ok"}

    # {gameId: "5b07d99f-3611-45c8-b88f-f2b06e3e47c4", 
    #  word: "CAT"}