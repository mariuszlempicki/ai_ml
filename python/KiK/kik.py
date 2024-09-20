from main import generate_board, get_coordinates_from_player, put_item_on_board, check_if_game_over

board = generate_board()
print(board)

n_of_moves = 0

while True:
    # Krzyżyk
    while True:
        coordinates = get_coordinates_from_player("x")
        board, flag = put_item_on_board(board, coordinates, "x")
        if flag:
            n_of_moves += 1
            break

    print(board)

    if check_if_game_over(board):
        print("Koniec gry, wygrał krzyżyk")
        break

    if n_of_moves == board.size:
        print("Remis")
        break

    # Kółko
    while True:
        coordinates = get_coordinates_from_player("o")
        board, flag = put_item_on_board(board, coordinates, "o")
        if flag:
            n_of_moves += 1
            break

    print(board)

    if check_if_game_over(board):
        print("Koniec gry, wygrało kółko")
        break

    if n_of_moves == board.size:
        print("Remis")
        break
