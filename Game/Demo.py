from TicTacToe import TicTacToe
import os


def cls(): # Thanks to
    os.system('cls' if os.name=='nt' else 'clear')

game = TicTacToe()

state = None

while state is None:
    cls()
    game.printBoard()
    print("=" * 40)
    move = int(input("Your move: "))
    state = game.play(move)

print(state)