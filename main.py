from Board import Board
from queens import *
from Fitness import *

if __name__ == "__main__":
    board_length = 8
    gen_size = 10
    board = Board(board_length)
    mutation_rate = 0.1

    # Get user input
    gen_size = int(input("Enter generation size: "))
    mutation_rate = float(input("Enter mutation rate (from 0 to 1, use . to seperate, e.g. 0.1): "))
    run_count = int(input("How many times would you like to run the program? "))
    
    for _ in range(run_count):
        # Generation counter
        gen_count = 1

        # Get max amount of non-attacking pairs of queens
        max_fit = max_fitness(board_length)

        # Initial generation
        generation = initGen(board_length, gen_size)

        # Get fitness matrix of the initial gen
        fitness_matrix = fitness(generation, max_fit)

        # While solution is not found, proceed to new generation    
        while(True):
            gen_count+=1
            parents = selection(generation, fitness_matrix, max_fit)
            children = crossover(parents, mutation_rate, board_length)
            fitness_children = fitness(children, max_fit)
            generation, fitness_matrix = population_reduction(children, fitness_children, gen_size)
            if(max_fit in fitness_matrix):
                if(run_count == 1):
                    solution = generation[fitness_matrix.index(max_fit)]
                    board.displayBoard(solution)
                    print("Generation count: ", gen_count)
                    break
                else:
                    solution = generation[fitness_matrix.index(max_fit)]
                    print("Generation count: ", gen_count, "Solution state: ", solution)
                    break