# Function that calculates the maximum possible fitness of a given board length
def max_fitness(board_length):
    res = 1
    # Every queen can have boardLength * (boardLength-1) of non-attacking queens 
    res = board_length * (board_length-1)
    # Divide by two cause we take pairs of queens
    return int(res/2)

# Function to calculate the fitness of each individual in the generation
# Returns an array of fitness values 
def fitness(generation, max_fitness):
    fitness_matrix = []
    
    for individual in generation:
        fitness_matrix.append(max_fitness - fitness_of_individual(individual))
    
    return fitness_matrix

# Function to calculate non-attacking pairs value of an individual state
# There can't be any hits on X due to how we represent the state of a board:
# 1D array of positions
# Index represents the row number, the value represents column number.
def fitness_of_individual(individual):
    hits = 0
    # Hits on Y
    for i in range(len(individual)):
        for j in range(i+1, len(individual)):
            if individual[i] == individual[j]:
                hits+=1
    # Diagonal check
    diag_hits = diagonal_hits(individual)
    hits += diag_hits
    
    return hits

# Function that checks diagonal hits for the position n in an individual
# Returns diagonal hit count
def diagonal_hits(individual):
    diag_hits = 0
    for index, n in enumerate(individual):
        step_left = 1
        step_right = 1
        # Left diagonals
        while (index-step_left)>=0:
            i = index - step_left
            if individual[i] == n-step_left or individual[i] == n+step_left:
                diag_hits+=1
            step_left+=1

        # Right diagonals
        while (index+step_right)<len(individual):
            i = index + step_right
            if individual[i] == n-step_right or individual[i] == n+step_right:
                diag_hits+=1
            step_right+=1

    # Pair of queens counts hits twice, divide by two
    return int(diag_hits/2)