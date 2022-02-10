from gamestate import *


def test_play_move():
    gamestate = GameState(False)
    gamestate.state = [
            ["X", Piece(B, 0, 1, False), "X", Piece(B, 0, 3, False), "X",
                Piece(B, 0, 5, False), "X", Piece(B, 0, 7, False)],
            [Piece(B, 1, 0, False), "X", Piece(B, 1, 2, False), "X",
                Piece(B, 1, 4, False), "X", Piece(B, 1, 6, False), "X"],
            ["X", Piece(B, 2, 1, False), "X", Piece(B, 2, 3, False), "X",
                Piece(B, 2, 5, False), "X", Piece(B, 2, 7, False)],
            [Piece(A, 3, 0, False), "X", Piece(A, 3, 2, False), "X",
                Piece(A, 3, 4, False), "X", Piece(A, 3, 6, False), "X"],
            ["X", Piece(A, 4, 1, False), "X", Piece(A, 4, 3, False), "X",
                Piece(A, 4, 5, False), "X", Piece(A, 4, 7, False)],
            [Piece(R, 5, 0, False), "X", Piece(R, 5, 2, False), "X",
                Piece(R, 5, 4, False), "X", Piece(R, 5, 6, False), "X"],
            ["X", Piece(R, 6, 1, False), "X", Piece(R, 6, 3, False), "X",
                Piece(R, 6, 5, False), "X", Piece(R, 6, 7, False)],
            [Piece(R, 7, 0, False), "X", Piece(R, 7, 2, False), "X",
                Piece(R, 7, 4, False), "X", Piece(R, 7, 6, False), "X"]
            ]
    #  noncapture move black
    gamestate.selected_piece = gamestate.state[2][3]
    assert(gamestate.state[2][3].color == B)
    assert(gamestate.state[3][4].color == A)
    gamestate.play_move([[2, 3], [3, 4]])
    assert(gamestate.state[2][3].color == A)
    assert(gamestate.state[3][4].color == B)

    gamestate = GameState(False)
    gamestate.state = [
        ["X", Piece(B, 0, 1, False), "X", Piece(B, 0, 3, False), "X",
            Piece(B, 0, 5, False), "X", Piece(B, 0, 7, False)],
        [Piece(B, 1, 0, False), "X", Piece(B, 1, 2, False), "X",
            Piece(B, 1, 4, False), "X", Piece(B, 1, 6, False), "X"],
        ["X", Piece(B, 2, 1, False), "X", Piece(A, 2, 3, False), "X",
            Piece(B, 2, 5, False), "X", Piece(B, 2, 7, False)],
        [Piece(A, 3, 0, False), "X", Piece(A, 3, 2, False), "X",
            Piece(B, 3, 4, False), "X", Piece(A, 3, 6, False), "X"],
        ["X", Piece(A, 4, 1, False), "X", Piece(A, 4, 3, False), "X",
            Piece(R, 4, 5, False), "X", Piece(A, 4, 7, False)],
        [Piece(R, 5, 0, False), "X", Piece(R, 5, 2, False), "X",
            Piece(R, 5, 4, False), "X", Piece(A, 5, 6, False), "X"],
        ["X", Piece(R, 6, 1, False), "X", Piece(R, 6, 3, False), "X",
            Piece(A, 6, 5, False), "X", Piece(A, 6, 7, False)],
        [Piece(R, 7, 0, False), "X", Piece(R, 7, 2, False), "X",
            Piece(R, 7, 4, False), "X", Piece(R, 7, 6, False), "X"]
        ]

    #  capture move black
    gamestate.selected_piece = gamestate.state[3][4]
    assert(gamestate.state[3][4].color == B)
    assert(gamestate.state[4][5].color == R)
    assert(gamestate.state[5][6].color == A)
    gamestate.play_move([[3, 4], [4, 5], [5, 6]])
    assert(gamestate.state[3][4].color == A)
    assert(gamestate.state[4][5].color == A)
    assert(gamestate.state[5][6].color == B)
    assert(gamestate.num_red_pieces == 11)


def test_noncapture_move():
    gamestate = GameState(False)
    state = [
            ["X", Piece(B, 0, 1, False), "X", Piece(B, 0, 3, False), "X",
                Piece(B, 0, 5, False), "X", Piece(B, 0, 7, False)],
            [Piece(B, 1, 0, False), "X", Piece(B, 1, 2, False), "X",
                Piece(B, 1, 4, False), "X", Piece(B, 1, 6, False), "X"],
            ["X", Piece(B, 2, 1, False), "X", Piece(B, 2, 3, False), "X",
                Piece(B, 2, 5, False), "X", Piece(B, 2, 7, False)],
            [Piece(A, 3, 0, False), "X", Piece(A, 3, 2, False), "X",
                Piece(A, 3, 4, False), "X", Piece(A, 3, 6, False), "X"],
            ["X", Piece(A, 4, 1, False), "X", Piece(A, 4, 3, False), "X",
                Piece(A, 4, 5, False), "X", Piece(A, 4, 7, False)],
            [Piece(R, 5, 0, False), "X", Piece(R, 5, 2, False), "X",
                Piece(R, 5, 4, False), "X", Piece(R, 5, 6, False), "X"],
            ["X", Piece(R, 6, 1, False), "X", Piece(R, 6, 3, False), "X",
                Piece(R, 6, 5, False), "X", Piece(R, 6, 7, False)],
            [Piece(R, 7, 0, False), "X", Piece(R, 7, 2, False), "X",
                Piece(R, 7, 4, False), "X", Piece(R, 7, 6, False), "X"]
            ]
    #  move list for black piece position 2, 3
    piece = state[2][3]
    move_list = [[[2, 3], [3, 2]], [[2, 3], [3, 4]]]
    assert(gamestate.noncapture_move(state, piece) == move_list)


def test_capture_move():
    gamestate = GameState(False)
    state = [
        ["X", Piece(B, 0, 1, False), "X", Piece(B, 0, 3, False), "X",
            Piece(B, 0, 5, False), "X", Piece(B, 0, 7, False)],
        [Piece(B, 1, 0, False), "X", Piece(B, 1, 2, False), "X",
            Piece(B, 1, 4, False), "X", Piece(B, 1, 6, False), "X"],
        ["X", Piece(B, 2, 1, False), "X", Piece(A, 2, 3, False), "X",
            Piece(B, 2, 5, False), "X", Piece(B, 2, 7, False)],
        [Piece(A, 3, 0, False), "X", Piece(A, 3, 2, False), "X",
            Piece(B, 3, 4, False), "X", Piece(A, 3, 6, False), "X"],
        ["X", Piece(A, 4, 1, False), "X", Piece(R, 4, 3, False), "X",
            Piece(R, 4, 5, False), "X", Piece(A, 4, 7, False)],
        [Piece(R, 5, 0, False), "X", Piece(A, 5, 2, False), "X",
            Piece(R, 5, 4, False), "X", Piece(R, 5, 6, False), "X"],
        ["X", Piece(R, 6, 1, False), "X", Piece(R, 6, 3, False), "X",
            Piece(A, 6, 5, False), "X", Piece(A, 6, 7, False)],
        [Piece(R, 7, 0, False), "X", Piece(R, 7, 2, False), "X",
            Piece(R, 7, 4, False), "X", Piece(R, 7, 6, False), "X"]
        ]
    #  move list for black piece position 2, 3
    piece = state[3][4]
    move_list = [[[3, 4], [4, 3], [5, 2]]]
    assert(gamestate.capture_move(state, piece) == move_list)


def test_all_noncapture():
    gamestate = GameState(False)
    gamestate.state = [
            ["X", Piece(B, 0, 1, False), "X", Piece(B, 0, 3, False), "X",
                Piece(B, 0, 5, False), "X", Piece(B, 0, 7, False)],
            [Piece(B, 1, 0, False), "X", Piece(B, 1, 2, False), "X",
                Piece(B, 1, 4, False), "X", Piece(B, 1, 6, False), "X"],
            ["X", Piece(B, 2, 1, False), "X", Piece(B, 2, 3, False), "X",
                Piece(B, 2, 5, False), "X", Piece(B, 2, 7, False)],
            [Piece(A, 3, 0, False), "X", Piece(A, 3, 2, False), "X",
                Piece(A, 3, 4, False), "X", Piece(A, 3, 6, False), "X"],
            ["X", Piece(A, 4, 1, False), "X", Piece(A, 4, 3, False), "X",
                Piece(A, 4, 5, False), "X", Piece(A, 4, 7, False)],
            [Piece(R, 5, 0, False), "X", Piece(R, 5, 2, False), "X",
                Piece(R, 5, 4, False), "X", Piece(R, 5, 6, False), "X"],
            ["X", Piece(R, 6, 1, False), "X", Piece(R, 6, 3, False), "X",
                Piece(R, 6, 5, False), "X", Piece(R, 6, 7, False)],
            [Piece(R, 7, 0, False), "X", Piece(R, 7, 2, False), "X",
                Piece(R, 7, 4, False), "X", Piece(R, 7, 6, False), "X"]
            ]
    non_capture_dictionary = {}
    non_capture_dictionary[gamestate.state[2][1]] = \
        [[[2, 1], [3, 0]], [[2, 1], [3, 2]]]
    non_capture_dictionary[gamestate.state[2][3]] = \
        [[[2, 3], [3, 2]], [[2, 3], [3, 4]]]
    non_capture_dictionary[gamestate.state[2][5]] = \
        [[[2, 5], [3, 4]], [[2, 5], [3, 6]]]
    non_capture_dictionary[gamestate.state[2][7]] = \
        [[[2, 7], [3, 6]]]
    assert(gamestate.all_noncapture() == non_capture_dictionary)


def test_all_capture():
    gamestate = GameState(False)
    gamestate.state = [
        ["X", Piece(B, 0, 1, False), "X", Piece(B, 0, 3, False), "X",
            Piece(B, 0, 5, False), "X", Piece(B, 0, 7, False)],
        [Piece(B, 1, 0, False), "X", Piece(B, 1, 2, False), "X",
            Piece(B, 1, 4, False), "X", Piece(B, 1, 6, False), "X"],
        ["X", Piece(B, 2, 1, False), "X", Piece(A, 2, 3, False), "X",
            Piece(B, 2, 5, False), "X", Piece(B, 2, 7, False)],
        [Piece(A, 3, 0, False), "X", Piece(A, 3, 2, False), "X",
            Piece(B, 3, 4, False), "X", Piece(A, 3, 6, False), "X"],
        ["X", Piece(A, 4, 1, False), "X", Piece(R, 4, 3, False), "X",
            Piece(R, 4, 5, False), "X", Piece(A, 4, 7, False)],
        [Piece(R, 5, 0, False), "X", Piece(A, 5, 2, False), "X",
            Piece(R, 5, 4, False), "X", Piece(R, 5, 6, False), "X"],
        ["X", Piece(R, 6, 1, False), "X", Piece(R, 6, 3, False), "X",
            Piece(A, 6, 5, False), "X", Piece(A, 6, 7, False)],
        [Piece(R, 7, 0, False), "X", Piece(R, 7, 2, False), "X",
            Piece(R, 7, 4, False), "X", Piece(R, 7, 6, False), "X"]
        ]
    capture_dictionary = {}
    capture_dictionary[gamestate.state[3][4]] = \
        [[[3, 4], [4, 3], [5, 2]]]
    assert(gamestate.all_capture() == capture_dictionary)


def test_switch_turn():
    #  black piece turn
    state = GameState(False)
    state.turn = R
    state.switch_turn()
    assert(state.turn == B)
