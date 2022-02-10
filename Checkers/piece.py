'''
Tiffany Lastimosa
CS 5001, Fall 2020

This program is a class for pieces.  With class Piece, piece objects are
created in checkers.
'''
import turtle
from constants import *


class Piece:
    '''
        Class -- Piece
            This class creates a piece object in grey, red, and black.
        Attributes:
            color -- the color of the piece.  For this project it is black,
                red, and grey.  When the piece is grey, the position on the
                board is available.
            isKing -- boolean attribute that determines if the piece is a king
                or not.
            x -- the x-value of the piece, or the row the piece object is in.
            y -- the y-value of the piece, or the column the piece object is
                in.
            draw_piece -- draws a piece object when class Piece is called.
        Methods:
            copy -- creates a copy of the piece with matching attributes.
            draw_piece -- uses turtle to draw a piece.
            draw_king_piece -- uses turtle to draw a king piece.
            king_piece -- provides the conditional, when conditional met, then
                king piece is drawn and boolean for self.isKing is True.
            move_piece -- updates the current position of the piece to the
                x, y position that the piece will move to.
    '''

    def __init__(self, color, x, y, draw=True):
        '''
            Constructor --
                Creates a new instance of a piece.
            Parameters:
                self -- the current piece object.
                color -- the color of the object.
                x -- the current x-value of the object.
                y -- the current y-value of the object.
        '''
        self.color = color
        self.isKing = False
        self.x = x
        self.y = y
        self.draw = draw
        if draw:
            self.draw_piece()

    # def __str__(self):
    #     return "\n Piece " + str(self.color) + \
    #         " (" + str(self.x) + "," + str(self.y) + ") " + str(self.isKing)

    def equal(self, other):
        return (self.color == other.color) and \
                    (self.isKing == other.isKing) and \
                    (self.x == other.x) and \
                    (self.y == other.y)

    def copy(self):
        '''
            Method --
                Creates a copy of the piece with matching attributes.
            Parameters:
                self -- the current piece object.
            Returns:
                Returns a copy of the piece.
        '''
        copy = Piece(self.color, self.x, self.y, draw=False)
        copy.isKing = self.isKing
        return copy

    def draw_piece(self):
        '''
            Method -- draw_piece
                Function draws a piece from self.color.
            Parameters:
                self -- the current piece object.
        '''
        turtle.color(self.color, self.color)
        turtle.setposition(CORNER_X + (SQUARE * self.y),
                           CORNER_Y - (SQUARE * (SQUARE_OFFSET - self.x)))
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(RADIUS)
        turtle.penup()
        turtle.end_fill()

    def draw_king_piece(self):
        '''
            Method -- draw_king_piece
                Draws a king piece.
            Parameters:
                self -- the current piece object.
        '''
        #  draws regular piece
        turtle.color(self.color, self.color)
        turtle.setposition(CORNER_X + (SQUARE * self.y),
                           CORNER_Y - (SQUARE * (SQUARE_OFFSET - self.x)))
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(RADIUS)
        turtle.penup()
        turtle.end_fill()

        #  draws a smaller circle on top of regular piece to make a king piece
        turtle.color(WHITE, self.color)
        turtle.setposition(CORNER_X + (SQUARE * self.y),
                           KING_OFFSET - (SQUARE * (SQUARE_OFFSET - self.x)))
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(KING_CIRCLE)
        turtle.penup()
        turtle.end_fill()

    def king_piece(self):
        '''
            Method --
                If black piece reaches end of the board or red piece reaches
                the end of the board, self.isKing is True.
            Parameters:
                self -- the current piece object.
        '''
        if (self.color == B and self.x == 7) or \
                (self.color == R and self.x == 0):
            self.isKing = True

    def move_piece(self, x, y):
        '''
            Method --
                Updates the self.x and self.y value to where the piece will be
                moved to.
            Parameters:
                self -- the current piece object.
                x -- x provides the row or x-value of the position the
                    current piece object will move to.
                y -- y provides the column or y-value of the position the
                    current piece object will move to.
        '''
        self.x = x
        self.y = y
        self.king_piece()
        if self.isKing and self.draw:
            self.draw_king_piece()
        elif self.draw:
            self.draw_piece()
