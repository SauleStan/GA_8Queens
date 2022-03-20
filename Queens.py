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
