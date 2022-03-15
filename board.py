class Board:
    def __init__(self, boardLength):
        self.boardLength = boardLength
        self.board = self.emptyBoard(self.boardLength)

    def emptyBoard(self, boardLength):
        boardMatrix = [[0 for i in range(boardLength)] for j in range(boardLength)]
        return boardMatrix
    
    def displayBoard(self):
        for i in range(self.boardLength):
            print(self.board[i])