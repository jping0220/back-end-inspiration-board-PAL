from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.board import Board
from app.models.card import Card

# example_bp = Blueprint('example_bp', __name__)
board_bp = Blueprint("boards", __name__, url_prefix="/boards")
card_bp =  Blueprint("cards", __name__, url_prefix="/cards")

def validate_item(model, item_id):
    try:
        item_id = int(item_id)
    except ValueError:
        return abort(make_response({"details": "Invalid data"}, 400))
    
    item = model.query.get(item_id)

    if not item:
        return abort(make_response({"details": f"id {item_id} not found"}, 404))
    
    return item

@board_bp.route("", methods=["POST"])
def add_boards():
    request_body = request.get_json()

    new_board = Board.from_dict(request_body)

    db.session.add(new_board)
    db.session.commit()

    return {"board": new_board.to_dict()}, 201

@board_bp.route("", methods=["GET"])
def get_all_boards():
    response = []

    all_boards = Board.query.all()

    for board in all_boards:
        response.append(board.to_dict())
    
    return jsonify(response), 200

@board_bp.route("/<board_id>", methods=["GET"])
def get_one_board(board_id):
    board = validate_item(Board, board_id)
    return {"board": board.to_dict()}, 200

@card_bp.route("", methods=["POST"])
def add_cards():
    request_body = request.get_json()

    new_card = Card.from_dict(request_body)

    db.session.add(new_card)
    db.session.commit()

    return {"card": new_card.to_dict()}, 201

@card_bp.route("", methods=["GET"])
def get_all_cards():
    response = []

    all_cards = Card.query.all()

    for card in all_cards:
        response.append(card.to_dict())
    
    return jsonify(response), 200

@card_bp.route("/<card_id>", methods=["DELETE"])
def delete_card(card_id):
    card = validate_item(Card,card_id)
    db.session.delete(card)
    db.session.commit()

    return {"details":f"Card {card_id} successfully deleted"}, 200

