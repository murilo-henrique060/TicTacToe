import numpy as np

class TicTacToe:
    def __init__(self) -> None:
        self._board : np.ndarray = np.zeros([3, 3])
        self._player : int = 1

    def getPlayerBoard(self) -> np.ndarray:
        """Return the board by the vision of the current player (actual current's moves equals to 1 and oponent's moves equals to -1)

        Returns:
            np.ndarray: Integer matrix 3x3 with values between -1 and 1.
        """
        return self._board * self._player

    def getBoard(self) -> np.ndarray:
        """Return the actual values of the board

        Returns:
            np.ndarray: Integer matrix 3x3 with values between -1 and 1.
        """
        return self._board

    def getPlayer(self) -> int:
        return self._player

    def checkWin(self) -> int | None:
        """Checks if the actual player win the game

        Returns:
            int | None: return the state of game (1: first player wins, 0: draw, -1: second player wins, None: none of the players have winned, but still playable squares)
        """
        board = self.getPlayerBoard()

        checks = []

        checks.extend(board.sum(axis=0) == 3)
        checks.extend(board.sum(axis=1) == 3)
        checks.append(board.trace() == 3)
        checks.append(np.fliplr(board).trace() == 3)

        if np.any(checks):
            return self._player

        if np.count_nonzero(board) == 9:
            return 0

    def printBoard(self) -> None:
        """Print the board on the prompt
        """
        for row in self._board:
            for item in row:
                print(f"[{'X' if item == 1 else 'O' if item == -1 else ' '}]", end="")
            print()

    def play(self, pos: int) -> int | None:
        """Set the current player value to the given pos and check if have winned

        Args:
            pos (int): Value between 0 and 8 representing the squares of the board

        Raises:
            ValueError: The "pos" parameter is outside the range

        Returns:
            int | None: return the state of game (1: first player wins, 0: draw, -1: second player wins, None: none of the players have winned, but still playable squares)
        """
        if pos < 0 or pos >= 9: # Check if its a vaid postion
            raise ValueError("pos must be in the 0-8 range")

        row, col = np.unravel_index(pos, [3, 3]) # Converting the 0-8 range to 3x3 cordinates

        if self._board[row][col] == 0:
            self._board[row][col] = self._player # Put the move on the board

        win = self.checkWin()

        if win is not None:
            return win

        self._player *= -1
