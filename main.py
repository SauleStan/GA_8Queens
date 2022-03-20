from calendar import c
from board import Board
from Queens import *
from Fitness import *

if __name__ == "__main__":
    boardLength = 8
    gen_size = 10
    board = Board(boardLength)

    generation = initGen(boardLength, gen_size)
    print(generation)

    # Get max amount of non-attacking pairs of queens
    max = maxFitness(boardLength)

    # Provide the current generation and max possible fitness score
    fitnessMatrix = fitness(generation, max)
    print(fitnessMatrix)
    
    parents = selection(generation, fitnessMatrix, max)
    children = crossover(parents)
    fitness_children = fitness(children, max)
    generation, fitness_matrix = population_reduction(children, fitness_children, gen_size)
    print(generation)
    print(fitness_matrix)

