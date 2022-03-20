from random import randrange
import random

from torch import chunk

from Fitness import fitness

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

# Function to perform crossover on the parents.
# Since crossover results in two new individuals, 
# the returned list is twice the size of initial
def crossover(parents):
    children = []
    pairs = []

    individualLen = len(parents[0])
    parentsLen = len(parents)
    # Crossover point will be a 1/4th of an individual
    crossover_point = int(individualLen/4)

    for i in range(parentsLen):
        for j in range(i+1, parentsLen):
            pairs.append([parents[i], parents[j]])
    
    for pair in pairs:
        # Slice up the parents
        p1_chunk_1 = pair[0][:crossover_point:]
        p1_chunk_2 = pair[0][crossover_point: :]
        p2_chunk_1 = pair[1][:crossover_point:]
        p2_chunk_2 = pair[1][crossover_point: :]
        
        # Cross the chunks
        children.append(p1_chunk_1+p2_chunk_2)
        children.append(p1_chunk_2+p2_chunk_1)

    return children

# Function to lower population count to initial generation size
# This is to preserve memory
# Returns the best fit children
def population_reduction(generation, fitness, gen_size):
    # Merge lists
    gen_fit = []
    for i, individual in enumerate(generation):
        gen_fit.append([individual, fitness[i]])
    
    # Sort the list based on fitness score
    sorted_gen_fit = sorted(gen_fit, key = lambda x: x[1],reverse=True)

    culled_gen = sorted_gen_fit[:gen_size:]
    
    # Splits culled_gen into generation and fitness list and returns them
    return map(list, zip(*culled_gen))

# Function to mutate individuals
# Returns a mutated individual
def mutation(individual, mutation_rate):
    pass