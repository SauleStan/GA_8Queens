from random import randrange

# Initializes random first generation
# boardLength is for the size of an individual
# genSize is for the amount of individuals in one generation
# Returns initial generation with randomized individuals
def initGen(boardLength, genSize):
    generation = []
    for n in range(genSize):
        individual = []
        for i in range(boardLength):
            initVal = randrange(0, boardLength-1)
            individual.append(initVal)
        generation.append(individual)
    
    return generation

def maxFitness(boardLength):
    res = 1
    # Every queen can have boardLength * (boardLength-1) of non-attacking queens 
    res = boardLength * (boardLength-1)
    # Divide by two cause we take pairs of queens
    return int(res/2)

# Function to calculate the fitness of each individual in the generation
# Returns an array of fitness values 
def fitness(generation):
    fitnessMatrix = []
    for individual in generation:
        pass