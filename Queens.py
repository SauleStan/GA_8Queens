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
def fitness(generation, nonAttackingMax):
    fitnessMatrix = []
    
    for individual in generation:
        fitnessMatrix.append(nonAttackingMax - fitnessOfIndividual(individual))
    
    return fitnessMatrix

# Function to calculate non-attacking pairs value of an individual state
def fitnessOfIndividual(individual):
    hits = 0
    # Hits on Y
    for i in range(len(individual)):
        for j in range(i+1, len(individual)):
            if individual[i] == individual[j]:
                hits+=1
    # No hits on X due to how we initiate the state?
    # Diagonal check
    diagHits = diagonalHits(individual)
    hits += diagHits
    
    return hits

# Function that checks diagonal hits for the position n in an individual
# Returns diagonal hit count
def diagonalHits(individual):
    diagHits = 0
    for index, n in enumerate(individual):
        stepLeft = 1
        stepRight = 1
        # Left diagonals
        while (index-stepLeft)>=0:
            i = index - stepLeft
            if individual[i] == n-stepLeft or individual[i] == n+stepLeft:
                diagHits+=1
            stepLeft+=1

        # Right diagonals
        while (index+stepRight)<len(individual):
            i = index + stepRight
            if individual[i] == n-stepRight or individual[i] == n+stepRight:
                diagHits+=1
            stepRight+=1

    # Pair of queens counts hits twice, divide by two
    return int(diagHits/2)