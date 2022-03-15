from board import Board
from Queens import *

if __name__ == "__main__":
    boardLength = 8
    board = Board(boardLength)

    generation = initGen(boardLength, 10)
    # generation = [[3, 2, 4, 1, 2, 3, 5, 1]]
    print(generation)
    print("\n")
    board.displayBoard(generation[0])

    # Get max amount of non-attacking pairs of queens
    max = maxFitness(boardLength)

    # Provide the current generation and max possible fitness score
    fitnessMatrix = fitness(generation, max)
    print(fitnessMatrix)