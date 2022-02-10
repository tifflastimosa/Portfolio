'''
Tiffany Lastimosa
CS 5001, Fall 2020

This file contains constants used in piece.py, gamestate.py, and main.py.
'''
import turtle

# provides dimensions
NUM_SQUARES = 8  # number of rows and columns
SQUARE_OFFSET = NUM_SQUARES - 1
TURTLE_OFFSET = NUM_SQUARES // 2
SQUARE = 60  # size of one side of square
RIGHT_ANGLE = 90
RADIUS = SQUARE // 2  # Radius = 30
board_size = NUM_SQUARES * SQUARE  # size of the board = 8 * 60
window_size = board_size + SQUARE  # creates window
CORNER = -board_size / 2
SQUARE_BOUNDARY = 240
CORNER_X = -210
CORNER_Y = 180
KING_OFFSET = CORNER_Y + 15
KING_CIRCLE = RADIUS / 2

# colors
SQUARE_COLOR = "grey"  # color of the valid squares
B = "black"  # user color
R = "red"  # AI, computer color
A = "grey"  # Available Spot
WHITE = "white"
BKG_COLOR = "white"  # bkg color
