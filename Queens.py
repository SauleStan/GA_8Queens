from random import randrange
import random

# Initializes random first generation
# board_length is for the size of an individual
# gen_size is for the amount of individuals in one generation
# Returns initial generation with randomized individuals
def initGen(board_length, gen_size):
    generation = []
    for n in range(gen_size):
        individual = []
        for i in range(board_length):
            initVal = randrange(0, board_length-1)
            individual.append(initVal)
        generation.append(individual)
    
    return generation

# Function to select parents from generation
# Returns a list of parents
def selection(generation, fitness, max_fitness):
    probabilities = []
    # Normalize fitness to probabilities
    for score in fitness:
        probabilities.append((score*100)/max_fitness)

    # Pick half of the population for crossover    
    parent_count = int(len(generation)/2)
    # Select k parents based on probability of their occurence
    parents = choices_no_repetition(generation, probabilities, k=parent_count)
    
    return parents

# Function to get parents without repetition
def choices_no_repetition(generation, weights, k=1):
    generation = list(generation)
    weights = list(weights)    
    result = []
    for n in range(k):
        pos = random.choices(
            range(len(generation)), 
            weights,
            k=1
        )[0]
        result.append(generation[pos])
        del generation[pos], weights[pos]
    return result