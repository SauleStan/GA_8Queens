from board import Board
from Queens import initGen

if __name__ == "__main__":
    boardLength = 8
    board = Board(boardLength)

    generation = initGen(boardLength, 10)
    print(generation)
    print("\n")