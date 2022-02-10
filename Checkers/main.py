'''
Tiffany Lastimosa
CS 5001, Fall 2020

This program is the driver that will let the user play checkers with the
computer.
'''
import turtle
from gamestate import *


def main():

    #  turtle set-up window
    turtle.setup(window_size, window_size)
    turtle.screensize(board_size, board_size)
    turtle.bgcolor(BKG_COLOR)

    #  turns of the turtle animation
    turtle.tracer(0, 0)
    turtle.penup()

    #  hides the turtle cursor
    turtle.hideturtle()

    #  keeps turtle open
    screen = turtle.Screen()

    #  initializes checkers
    board = GameState()

    #  provides coordinates when click made on the window
    screen.onclick(board.click_handler)

    turtle.mainloop()
    turtle.done()


if __name__ == "__main__":
    main()
