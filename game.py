import streamlit as st
import numpy as np

class Game:
    BLACK = -1
    WHITE = 1
    BOARD_SIZE = 15
    PIECE_RADIUS = 20

    def __init__(self, mode, ai_level=1):
        self.mode = mode
        self.ai_level = ai_level
        self.reset_game()

    def reset_game(self):
        self.turn = self.BLACK
        self.board = np.zeros((self.BOARD_SIZE, self.BOARD_SIZE), dtype=int)
        self.history = []

    def run(self):
        canvas_width = self.BOARD_SIZE * self.PIECE_RADIUS * 2
        canvas_height = self.BOARD_SIZE * self.PIECE_RADIUS * 2

        canvas = st.canvas(width=canvas_width, height=canvas_height, drawing_mode='transform')

        while True:
            # Draw board
            self.draw_board(canvas)

            # Handle user input
            if self.mode == 'Human vs. AI' and self.turn == self.WHITE:
                self.make_ai_move()
            else:
                clicked = canvas_clicked(canvas)
                if clicked:
                    x, y = clicked
                    row, col = self.get_clicked_position(x, y)
                    if self.is_valid_move(row, col):
                        self.make_move(row, col)

            # Check for end of game
            winner = self.check_for_winner()
            if winner is not None:
                self.show_winner(canvas, winner)
                if st.button('Play again'):
                    self.reset_game()
                    break

    def make_move(self, row, col):
        self.board[row][col] = self.turn
        self.history.append((row, col, self.turn))
        self.turn = -self.turn

    def is_valid_move(self, row, col):
        if row < 0 or row >= self.BOARD_SIZE or col < 0 or col >= self.BOARD_SIZE:
            return False
        if self.board[row][col] != 0:
            return False
        if self.is_ko_move(row, col):
            return False
        return True

    def is_ko_move(self, row, col):
        if len(self.history) < 2:
            return False
        last_move = self.history[-1]
        if (row, col) != last_move[:2]:
            return False
        prev_board = np.zeros((self.BOARD_SIZE, self.BOARD_SIZE), dtype=int)
        prev_board[self.board == -self.turn] = -self.turn
        prev
