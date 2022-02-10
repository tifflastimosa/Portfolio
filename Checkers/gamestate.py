'''
Tiffany Lastimosa
CS 5001, Fall 2020

This program provides the current state of the board.
'''
import turtle
import time
import random
from piece import *

#  turn off turtle animation for test_play_move
turtle.tracer(0, 0)


class GameState:
    '''
        Class -- GameState
            This class provides the state of the board during the game.
        Attributes:
            selected_piece -- Piece under consideration.
            selected_piece_move_list -- Provides a list of move for the
                selected piece.
            num_black_pieces -- Provides the number of black pieces on the
                board.
            num_red_pieces -- provides the number of red pieces on the board.
            turn -- Keeps track of turns dependedent on piece color.
            state -- Store the state of the current state of the board..
                Uses Piece class from piece.py to create piece objects.
                Refer to Piece class for attributes of a piece.
                "X" represents invalid squares a piece cannot move to.
        Methods:
            draw_square --
                Uses turtle to draw a square.
            draw_board --
                Draws the board to play checkers.
            play_move --
                Plays a noncapturing move or capturing move.  Updates the state
                of the board when a move is played.
            follow_on_move --
                Evaluates if the selected piece can make a second capture.
            noncapture_move --
                Calculates all valid noncapture moves for a single piece.
            capture_move --
                Calculates all valid capture moves for a single piece.
            all_noncapture --
                Iterates through state to find all noncapture moves that can
                be played for player's turn.
            all_capture --
                Iterates through state to find all capture moves that can be
                played for player's turn.
            click --
                Allows user to select a piece and play a move.
            click_handler --
                Provides the x, y coordinates when a valid click is made on the
                board.
            switch_turn --
                Switches turn after a piece is moved.
            red_turn --
                Random move is played when it is red piece's turn.
            highlight_square --
                Draws the highlighted square.
            game_won --
                Determines the winner of the game.
    '''

    def __init__(self, draw=True):
        '''
            Constructor --
                Creates a new instance of the board.
            Parameters:
                self -- the current board object.
        '''
        self.selected_piece = None

        self.selected_piece_move_list = []

        self.num_black_pieces = 12

        self.num_red_pieces = 12

        self.turn = B

        if draw:
            self.draw_board()
            self.state = [
                ["X", Piece(B, 0, 1), "X", Piece(B, 0, 3), "X", Piece(B, 0, 5),
                    "X", Piece(B, 0, 7)],
                [Piece(B, 1, 0), "X", Piece(B, 1, 2), "X", Piece(B, 1, 4), "X",
                    Piece(B, 1, 6), "X"],
                ["X", Piece(B, 2, 1), "X", Piece(B, 2, 3), "X", Piece(B, 2, 5),
                    "X", Piece(B, 2, 7)],
                [Piece(A, 3, 0), "X", Piece(A, 3, 2), "X", Piece(A, 3, 4), "X",
                    Piece(A, 3, 6), "X"],
                ["X", Piece(A, 4, 1), "X", Piece(A, 4, 3), "X", Piece(A, 4, 5),
                    "X", Piece(A, 4, 7)],
                [Piece(R, 5, 0), "X", Piece(R, 5, 2), "X", Piece(R, 5, 4), "X",
                    Piece(R, 5, 6), "X"],
                ["X", Piece(R, 6, 1), "X", Piece(R, 6, 3), "X", Piece(R, 6, 5),
                    "X", Piece(R, 6, 7)],
                [Piece(R, 7, 0), "X", Piece(R, 7, 2), "X", Piece(R, 7, 4), "X",
                    Piece(R, 7, 6), "X"]
                ]

    def draw_square(self, size):
        '''
            Method -- draw_square
                Uses turtle to draw a square.
            Parameters:
                self -- the current state of the game.
                size -- the length of each side of the square.
            Return:
                Nothing.
        '''
        turtle.begin_fill()
        turtle.pendown()
        for side in range(4):
            turtle.forward(size)
            turtle.left(RIGHT_ANGLE)
        turtle.end_fill()
        turtle.penup()

    def draw_board(self):
        '''
            Method -- draw_board
                Draws the board to play checkers.
            Parameters:
                self -- the current state of the board.
            Return:
                Nothing.
        '''
        #  sets the turtle position to draw the checkerboard
        turtle.setposition(CORNER, CORNER)

        #  draws the checkerboard
        turtle.color(B, WHITE)
        self.draw_square(board_size)
        turtle.color(B, SQUARE_COLOR)
        for number in range(NUM_SQUARES):
            for row in range(NUM_SQUARES):
                if number % 2 != row % 2:
                    turtle.setposition(CORNER + SQUARE * number,
                                       CORNER + SQUARE * row)
                    self.draw_square(SQUARE)

    def play_move(self, move):
        '''
            Method -- play_move
                This function will play the move, either noncapturing or
                capturing move.
                Updates the state of the board when a move is played.
                Moves a selected piece on the board.
                Switches the turn and calculates if another capture can be made
                if it exists.
                Checks if the game is won.
            Parameters:
                self -- the current state of the game.
                move -- the move to be played.
            Return:
                None.
        '''
        #  conditional for a noncapture move
        if len(move) == 2:
            initial = move[0]
            final = move[1]

            #  state of the board updated
            #  available piece object created in place of played piece
            self.state[initial[0]][initial[1]] = \
                Piece(A, initial[0], initial[1])

            #  x, y values changed for the selected piece object
            #  selected piece moves to new position
            self.selected_piece.move_piece(final[0], final[1])

            #  state of the board updated
            self.state[final[0]][final[1]] = \
                self.selected_piece

            if self.game_won():
                return None

            #  turn changes
            self.switch_turn()

            #  selected_piece is set back to none for the next move
            self.selected_piece = None

            #  removes the highlight of piece move options
            for move in self.selected_piece_move_list:
                final = move[-1]
                self.highlight_square(final[0], final[1], "black")

            self.selected_piece_move_list = []

        #  conditional for capture move
        else:
            initial = move[0]
            remove_piece = move[1]
            final = move[2]

            #  state of the board updated
            #  available piece object created in place of played piece
            self.state[initial[0]][initial[1]] = \
                Piece(A, initial[0], initial[1])

            #  available piece object created in place of captured piece
            self.state[remove_piece[0]][remove_piece[1]] = \
                Piece(A, remove_piece[0], remove_piece[1])

            #  x, y values changed for the selected piece object
            self.selected_piece.move_piece(final[0], final[1])

            #  state of the board updated for played piece
            self.state[final[0]][final[1]] = \
                self.selected_piece

            #  conditional to update number of pieces when piece is captured
            if self.selected_piece.color == B:
                self.num_red_pieces -= 1
            elif self.selected_piece.color == R:
                self.num_black_pieces -= 1

            #  determines if another capture move can be played
            self.follow_on_move()
            if self.selected_piece_move_list == []:
                if self.game_won():
                    return None
                self.switch_turn()
                self.selected_piece = None

    def follow_on_move(self):
        '''
            Method -- follow_on_move
                Evaluates if the selected piece can make a second capture.
                For a black piece it highlights the second capture.
                For a red piece it plays the second capture.
            Parameters:
                self -- the current state of the game or board.
            Return:
                None.
        '''
        #  removes highlight
        for move in self.selected_piece_move_list:
            final = move[-1]
            self.highlight_square(final[0], final[1], "black")

        self.selected_piece_move_list = \
            self.capture_move(self.state[:], self.selected_piece.copy())

        # highlights to where the piece can move to
        for move in self.selected_piece_move_list:
            #  black piece turn
            if self.turn == B:
                final = move[-1]
                self.highlight_square(final[0], final[1])
            #  red piece turn
            else:
                random_move = random.choice(self.selected_piece_move_list)
                self.play_move(random_move)

    def noncapture_move(self, state, piece):
        '''
            Method -- noncapture move
                Calculates all valid noncapture moves for a single piece.
            Parameters:
                self -- the current state of the game or board.
                state -- list defining the board.
                piece -- the piece that we are calculating noncapturing moves
                for.
            Return:
                move_list - a list of all valid noncapture moves for piece.
        '''
        initial = [piece.x, piece.y]
        move_list = []

        #  conditional for black piece
        if piece.color == B:

            #  if piece is a black piece and is a king pice
            if piece.isKing:

                #  stops piece from going below, off the board
                if piece.x >= 1:

                    #  stops piece from going left, off the board
                    if piece.y >= 1:

                        #  moves down 1 row, moves left 1 column
                        if state[piece.x - 1][piece.y - 1].color == A:
                            move_list.append([initial,
                                             [piece.x - 1, piece.y - 1]])

                    #  stops piece from going right, off the board
                    if piece.y <= 6:

                        #  moves down 1 row, moves right 1 column
                        if state[piece.x - 1][piece.y + 1].color == A:
                            move_list.append([initial,
                                             [piece.x - 1, piece.y + 1]])

            #  conditional for moving forward, black piece is king or not
            #  stops from from moving up, off the board
            if piece.x <= 6:

                #  stops piece from going left, off the board
                if piece.y >= 1:

                    #  moves up 1 row, moves left 1 column
                    if state[piece.x + 1][piece.y - 1].color == A:
                        move_list.append([initial,
                                         [piece.x + 1, piece.y - 1]])

                #  stops piece from going right, off the board
                if piece.y <= 6:

                    #  moves up 1 row, moves right 1 column
                    if state[piece.x + 1][piece.y + 1].color == A:
                        move_list.append([initial,
                                         [piece.x + 1, piece.y + 1]])

        #  conditional for red piece
        elif piece.color == R:

            #  if piece is a black piece and a king piece
            if piece.isKing:

                #  stops piece from going up, off the board
                if piece.x <= 6:

                    #  stops piece from going left, off the board
                    if piece.y >= 1:

                        #  moves up 1 row, moves left 1 column
                        if state[piece.x + 1][piece.y - 1].color == A:
                            move_list.append([initial,
                                             [piece.x + 1, piece.y - 1]])

                    #  stops piece from going right, off the board
                    if piece.y <= 6:

                        #  moves up 1 row, moves right 1 column
                        if state[piece.x + 1][piece.y + 1].color == A:
                            move_list.append([initial,
                                             [piece.x + 1, piece.y + 1]])

            #  stops piece from going down, off the board
            if piece.x >= 1:

                #  stops piece from going left, off the board
                if piece.y >= 1:

                    #  moves down 1 row, moves left 1 column
                    if state[piece.x - 1][piece.y - 1].color == A:
                        move_list.append([initial,
                                         [piece.x - 1, piece.y - 1]])

                #  stops piece from going right, off the board
                if piece.y <= 6:

                    #  moves down 1 row, moves right 1 column
                    if state[piece.x - 1][piece.y + 1].color == A:
                        move_list.append([initial,
                                         [piece.x - 1, piece.y + 1]])

        return move_list

    def capture_move(self, state, piece):
        '''
            Method -- capture move
                Calculates all valid capture moves for a single piece.
            Parameters:
                self -- the current state of the game or board.
                state -- list defining the board.
                piece -- the piece that we are calculating capturing moves
                for.
            Return:
                move_list - a list of all valid capture moves for piece.
        '''
        move_list = []

        #  piece is black and capturing red
        if piece.color == B:

            #  black piece captures up
            #  conditional stops piece from capturing up and off the board
            if piece.x <= 5:

                #  conditional stops piece from capture up-left off the board
                if piece.y >= 2:

                    #  conditional if piece up-left is red and available
                    if state[piece.x + 1][piece.y - 1].color == R and \
                            state[piece.x + 2][piece.y - 2].color == A:
                        move_list.append([[piece.x, piece.y],
                                         [piece.x + 1, piece. y - 1],
                                         [piece.x + 2, piece.y - 2]])

                #  conditional stops piece from capture up-right off the board
                if piece.y <= 5:

                    #  conditional if piece up-right is red and available
                    if state[piece.x + 1][piece.y + 1].color == R and \
                            state[piece.x + 2][piece.y + 2].color == A:
                        move_list.append([[piece.x, piece.y],
                                          [piece.x + 1, piece.y + 1],
                                          [piece.x + 2, piece.y + 2]])

            #  conditional stops from capturing down-right off the board
            if piece.x >= 2 and piece.y <= 5:

                #  conditional if black piece is a king piece
                #  conditional if piece down-right is red and available
                if piece.isKing and \
                    state[piece.x - 1][piece.y + 1].color == R and \
                        state[piece.x - 2][piece.y + 2].color == A:
                    move_list.append([[piece.x, piece.y],
                                     [piece.x - 1, piece.y + 1],
                                     [piece.x - 2, piece.y + 2]])

            #  conditional stops from capturing down-left off the board
            if piece.x >= 2 and piece.y >= 2:

                #  conditional if black piece is a king piece
                #  conditional if piece down-left is red and available
                if piece.isKing and \
                    state[piece.x - 1][piece.y - 1].color == R and \
                        state[piece.x - 2][piece.y - 2].color == A:
                    move_list.append([[piece.x, piece.y],
                                     [piece.x - 1, piece.y - 1],
                                     [piece.x - 2, piece.y - 2]])

        #  piece is red and capturing black
        elif piece.color == R:

            #  stops piece from capturing down, off the board
            if piece.x >= 2:

                #  stops piece from capturing down-left off the board
                if piece.y >= 2:

                    #  conditional if piece down-left is black and available
                    if state[piece.x - 1][piece.y - 1].color == B and \
                            state[piece.x - 2][piece.y - 2].color == A:
                        move_list.append([[piece.x, piece.y],
                                         [piece.x - 1, piece.y - 1],
                                         [piece.x - 2, piece.y - 2]])

                #  stops piece from capturing down-right off the board
                if piece.y <= 5:

                    #  conditional if piece down-right is black and available
                    if state[piece.x - 1][piece.y + 1].color == B and \
                            state[piece.x - 2][piece.y + 2].color == A:
                        move_list.append([[piece.x, piece.y],
                                         [piece.x - 1, piece.y + 1],
                                         [piece.x - 2, piece.y + 2]])

            #  stops piece from capturing up-right off the board
            if piece.x <= 5 and piece.y <= 5:

                #  conditional if red piece is king
                #  conditional if piece up-right is black and available spot
                if piece.isKing and \
                    state[piece.x + 1][piece.y + 1].color == B and \
                        state[piece.x + 2][piece.y + 2].color == A:
                    move_list.append([[piece.x, piece.y],
                                     [piece.x + 1, piece.y + 1],
                                     [piece.x + 2, piece.y + 2]])

            #  stops piece from capturing up-left off the board
            if piece.x <= 5 and piece.y >= 2:

                #  conditional if red piece is king
                #  conditional if piece up-left is black and available spot
                if piece.isKing and \
                    state[piece.x + 1][piece.y - 1].color == B and \
                        state[piece.x + 2][piece.y - 2].color == A:
                    move_list.append([[piece.x, piece.y],
                                     [piece.x + 1, piece.y - 1],
                                     [piece.x + 2, piece.y - 2]])

        return move_list

    def all_noncapture(self):
        '''
            Method -- all_noncapture
                Iterates through state to find all noncapture moves that can
                be played for player's turn.
            Parameters:
                self -- the current state of the game or board.
            Return:
                non_capture_dictionary - a dictionary of noncapturing moves.
        '''
        #  copy of the current state of the game or board
        state = self.state[:]

        #  creating dictionay of piece and moves
        non_capture_dictionary = {}
        for row in state:
            for piece in row:
                if piece != "X" and piece.color == self.turn:
                    non_capture_list = \
                        self.noncapture_move(state, piece.copy())
                    if non_capture_list != []:
                        non_capture_dictionary[piece] = non_capture_list

        return non_capture_dictionary

    def all_capture(self):
        '''
            Method -- all_capture
                Iterates through state to find all capture moves that can
                be played for player's turn.
            Parameters:
                self -- the current state of the game or board.
            Return:
                capture_dictionary - a dictionary of capturing moves.
        '''
        #  copy of the current state of the game or board
        state = self.state[:]

        #  creating dictionary of piece and moves
        capture_dictionary = {}
        for row in state:
            for piece in row:
                if piece != "X" and piece.color == self.turn:
                    capture_list = self.capture_move(state, piece.copy())
                    if capture_list != []:
                        capture_dictionary[piece] = capture_list

        return capture_dictionary

    def click(self, x, y):
        '''
            Method -- click
                Allows user to select a piece and play a move.
            Parameters:
                self -- the current state of the game or board.
                x -- provides the row of the checkerboard on which the user
                clicked.
                y -- provides the column of the checkerboard on which the user
                clicked.
            Return:
                None.
        '''
        #  provides position of a piece in the current state of the board
        piece = self.state[x][y]

        #  if piece is black and it is black piece's turn
        if piece.color == B and self.turn == B:

            #  dictionary of all pieces that can move
            move_dictionary = self.all_capture()

            #  move_dictionary empty, then move_dictionary is noncapture moves
            if move_dictionary == {}:
                move_dictionary = self.all_noncapture()

            #  if the position of a piece is in the dictionary
            if piece in move_dictionary.keys():

                #  iterates through self.selected_piece_move_list
                for move in self.selected_piece_move_list:
                    final = move[-1]
                    #  removes  highlight from square
                    self.highlight_square(final[0], final[1], "black")

                #  selected piece is equal to piece
                self.selected_piece = piece
                self.selected_piece_move_list = \
                    move_dictionary[self.selected_piece]

                #  iterates through self.selected_piece_move_list
                for move in self.selected_piece_move_list:
                    final = move[-1]
                    #  adds highlight to square to where piece will move
                    self.highlight_square(final[0], final[1])

        #  if available spot and selected piece
        elif piece.color == A and self.selected_piece:

            #  iterates through move list of selected piece
            for move in self.selected_piece_move_list:

                #  next position of the piece is the last item of move list
                next_position = move[-1]

                #  plays the move  when condition is met
                if next_position[0] == piece.x and next_position[1] == piece.y:
                    self.play_move(move)

    def click_handler(self, y, x):
        '''
            Function -- click_handler
                This provides the x, y coordinates when a click is made on the
                board.
            Parameters:
                self -- the current state of the game or board.
                x -- provides turtle x-coordinates.
                y -- provides turtle y-coordinates.
            Return:
                None.
        '''
        #  conditional when user clicks outside of board
        if x < -SQUARE_BOUNDARY or x > SQUARE_BOUNDARY or \
                y < -SQUARE_BOUNDARY or y > SQUARE_BOUNDARY:
            print("out of bounds")
            x, y = None, None

        else:

            #  calculates the row, column
            #  allows to click anywhere in the square to return same value
            x = int((x // SQUARE) + TURTLE_OFFSET)
            y = int((y // SQUARE) + TURTLE_OFFSET)
            print(f"x-value {x}, y-value {y}")

            #  invalid click if user clicks on a white square
            if (x % 2 == 0 and y % 2 == 0) or \
                    (x % 2 != 0 and y % 2 != 0):
                print("invalid click")
                x, y = None, None

            if (x is not None) and (y is not None):
                self.click(x, y)

    def switch_turn(self):
        '''
            Function -- switch_turn
                Switches turn after a piece is moved.
            Parameters:
                self -- the current state of the game or board.
            Return:
                None.
        '''
        if self.turn == B:
            self.turn = R
            turtle.setposition(0, -255)
            turtle.color("white")
            turtle.write("Black Turn",
                         font=("Arial", 12, "normal"), align="center")
            turtle.color(B)
            turtle.write("Red Turn",
                         font=("Arial", 12, "normal"), align="center")
            turtle.undo()
            time.sleep(2)
            self.red_turn()
        else:
            self.turn = B
            print("Black Turn")
            turtle.setposition(0, -255)
            turtle.color(B)
            turtle.write("Black Turn",
                         font=("Arial", 12, "normal"), align="center")
            time.sleep(2)

    def red_turn(self):
        '''
            Function -- red_turn
                Plays move when it is red piece's turn.  Computer randomly
                picks a valid move.
            Parameters:
                self -- the current state of the game or board.
            Return:
                None.
        '''
        #  removes existing highlighted squares on the board
        for move in self.selected_piece_move_list:
            final = move[-1]
            self.highlight_square(final[0], final[1], "black")

        #  dictionary of all red pieces that make a capture move
        move_dictionary = self.all_capture()

        #  if no capture can be made, provides dictionary of noncapture move
        if move_dictionary == {}:
            move_dictionary = self.all_noncapture()

        #  randomly selects move from list for red piece to play
        self.selected_piece = random.choice(list(move_dictionary.keys()))
        self.selected_piece_move_list = move_dictionary[self.selected_piece]
        random_move = random.choice(move_dictionary[self.selected_piece])
        self.play_move(random_move)

    def highlight_square(self, x, y, color="yellow"):
        '''
            Method -- highlight_square
                Draws the highlighted square.
            Parameters:
                self -- the current state of the game or board.
                x -- x-coordinate for square to highlight.
                y -- y -coordinate for square to highlight.
                color -- color of the outline of the square.
            Return:
                None.
        '''
        turtle.penup()
        turtle.setposition(CORNER + SQUARE * y, CORNER + SQUARE * x)
        turtle.pendown()
        turtle.color(color)
        for side in range(4):
            turtle.forward(SQUARE)
            turtle.left(RIGHT_ANGLE)
        turtle.penup()

    def game_won(self):
        '''
            Method -- game_won
                Determines the winner of the game.
            Parameters:
                self -- current state of the board.
            Return:
                Returns True if there is a winner of the game.
                Returns False if there is no winner fo the game.
        '''
        print("black pieces", self.num_black_pieces,
              "red pieces", self.num_red_pieces)
        turtle.setposition(0, 0)

        #  determines winner of the game if piece count is 0
        if self.num_black_pieces == 0:
            turtle.color("green")
            turtle.write("Game Over!\n  Red Won!",
                         font=("Arial", 60, "normal"), align="center")
            print("RED WON", self.num_black_pieces)
            return True
        elif self.num_red_pieces == 0:
            turtle.color("green")
            turtle.write("Game Over!\n Black Won!",
                         font=("Arial", 60, "normal"), align="center")
            print("BLACK WON", self.num_red_pieces)
            return True

        #  determines winner of the game if piece cannot move
        move_dictionary = self.all_capture()

        if move_dictionary == {}:
            move_dictionary = self.all_noncapture()
            if move_dictionary == {}:
                turtle.color("green")
                if self.turn == R:
                    turtle.write("Game Over!\n Black Won!",
                                 font=("Arial", 60, "normal"), align="center")
                elif self.turn == B:
                    turtle.write("Game Over!\n  Red Won!",
                                 font=("Arial", 60, "normal"), align="center")
                return True

        return False
