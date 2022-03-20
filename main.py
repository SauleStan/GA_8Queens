from calendar import c
from board import Board
from Queens import *
from Fitness import *

if __name__ == "__main__":
    boardLength = 8
    gen_size = 10
    gen_count = 1
    board = Board(boardLength)
    mutation_rate = 0.1

    # Get max amount of non-attacking pairs of queens
    max_fitness = maxFitness(boardLength)

    # Initial generation
    generation = initGen(boardLength, gen_size)

    # Get fitness matrix of the initial gen
    fitness_matrix = fitness(generation, max_fitness)

    # While solution is not found, proceed to new generation    
    while(True):
        gen_count+=1
        parents = selection(generation, fitness_matrix, max_fitness)
        children = crossover(parents, mutation_rate, boardLength)
        fitness_children = fitness(children, max_fitness)
        generation, fitness_matrix = population_reduction(children, fitness_children, gen_size)
        if(max_fitness in fitness_matrix):
            solution = generation[fitness_matrix.index(max_fitness)]
            board.displayBoard(solution)
            print("Generation count: ", gen_count)
            break