import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.zeros([3, 3], dtype=np.int16)
        self.player = 1

    def check_win():
        # Win Conditions
        pass

    def play(self, pos: int):
        if pos < 0 or pos >= 9: # Check if its a vaid postion
            raise ValueError("pos must be in the 0-8 range")

        row, col = np.unravel_index(pos, [3, 3]) # Converting the 0-8 range to 3x3 cordinates

        if self.board[row][col] == 0:
            self.board[row][col] = self.player # Put the move on the board

        else:
            # Win Condition?
            pass


        self.player *= -1 # Change player turn

game = TicTacToe()
