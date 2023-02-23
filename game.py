import numpy as np
import torch
from PIL import Image
from io import BytesIO

class Game:
    MACHINE = 1
    USER = -1

    def __init__(self):
        self.board_size = 19
        self.board = np.zeros((self.board_size, self.board_size), dtype=np.int32)
        self.started = False
        self.turn = None
        self.winner = None
        self.machine_difficulty = 5
        self.model = None

    def start_game(self, difficulty):
        self.started = True
        self.turn = Game.USER
        self.winner = None
        self.machine_difficulty = difficulty
        self.model = torch.load("model.pt")

    def draw_board(self):
        board_img = Image.new("RGB", (512, 512), (255, 206, 158))
        stone_size = 30
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row, col] == Game.USER:
                    color = "black"
                elif self.board[row, col] == Game.MACHINE:
                    color = "white"
                else:
                    continue
                x = col * stone_size + stone_size
                y = row * stone_size + stone_size
                ImageDraw.Draw(board_img).ellipse((x - stone_size, y - stone_size, x + stone_size, y + stone_size), fill=color)
        return np.array(board_img)

    def check_game_over(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row
