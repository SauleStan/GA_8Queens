class Board:
    def __init__(self, boardLength):
        self.boardLength = boardLength
        self.board = self.emptyBoard(self.boardLength)

    def emptyBoard(self, boardLength):
        boardMatrix = [[0 for i in range(boardLength)] for j in range(boardLength)]
        return boardMatrix
    
    def displayBoard(self, individual=None):
        if individual is not None:
            print("Individual:")
            print(individual, "\n")
            index = 0
            for i in self.board:
                i[individual[index]] = 1
                index+=1
        print("Board:")
        for i in range(self.boardLength):
            print(self.board[i])