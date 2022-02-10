from piece import *


def test_copy():
    black_piece = Piece(B, 5, 2, False)
    assert((black_piece.copy().equal(black_piece)))
    red_piece = Piece(R, 3, 4, False)
    red_piece.isKing = True
    assert((red_piece.copy().equal(red_piece)))
    assert((red_piece.copy().equal(black_piece)) is False)


def test_king_piece():
    #  test black king pieces
    black_piece = Piece(B, 7, 2, False)
    assert(black_piece.isKing is False)
    black_piece.king_piece()
    assert(black_piece.isKing is True)

    #  test black pieces
    black_piece = Piece(B, 6, 1, False)
    assert(black_piece.isKing is False)
    black_piece.king_piece()
    assert(black_piece.isKing is False)

    #  test red king pieces
    red_piece = Piece(R, 0, 1, False)
    assert(red_piece.isKing is False)
    red_piece.king_piece()
    assert(red_piece.isKing is True)

    #  test red pieces
    red_piece = Piece(R, 1, 0, False)
    assert(red_piece.isKing is False)
    black_piece.king_piece()
    assert(red_piece.isKing is False)


def test_move_piece():
    #  test black piece
    black_piece = Piece(B, 4, 3, False)
    black_piece.move_piece(5, 4)
    assert(black_piece.x == 5)
    assert(black_piece.y == 4)

    #  test black king piece
    black_piece = Piece(B, 6, 1, False)
    assert(black_piece.isKing is False)
    black_piece.move_piece(7, 2)
    assert(black_piece.x == 7)
    assert(black_piece.y == 2)
    black_piece.king_piece()
    assert(black_piece.isKing is True)
