import numpy as np


def generate_board():
    return np.full((3, 3), ".")


def put_item_on_board(board, coordinates, mark):
    if mark not in ["x", "o"]:
        return board, False

    if coordinates[0] < 0 or coordinates[0] > 2 or coordinates[1] < 0 or coordinates[1] > 2:
        return board, False

    if board[coordinates] != ".":
        return board, False

    # ... itd.

    board[coordinates] = mark

    return board, True


def check_if_game_over(board):
    for mark in ["x", "o"]:
        if np.all(board.diagonal() == mark) or np.all(np.fliplr(board).diagonal() == mark):
            return True

        for axis in [0, 1]:
            if np.any(np.all(board == mark, axis=axis)):
                return True

    if "." not in board:
        return True

    return False


def get_coordinates_from_player(player):
    while True:
        input_text = f"{'Krzyżyk' if player in ['x', 'X'] else 'Kółko'}: podaj współrzędne w formacie (y,x): "
        raw_input = input(input_text)

        if raw_input[0].isnumeric() and raw_input[2].isnumeric():
            break

    return int(raw_input[0]), int(raw_input[2])
