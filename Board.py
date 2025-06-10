## board class

class Board:
    def __init__(self):
        self.cols = 7
        self.rows = 6
        self.gameBoard = [["-" for cols in range(7)] for rows in range(6)]
        self.playerX = True
        self.playerO  = False

        self.maxPlacements = self.cols*self.rows
        self.placements = 0

    def printBoard(self): ##redo this upside down

        print("")
        for row in range(5,-1,-1):
            print(" ".join(f"{cell:^4}" for cell in self.gameBoard[row]))
        print("")



    def playGame(self):
        gameOver = False

        self.printBoard()

        while(not(gameOver)):

            if self.playerX:
                currentPlacement = "X"
            else:
                currentPlacement = "O"


            turnMsg = f"It is Player {currentPlacement}'s turn"
            print(turnMsg)

            playCol = int(input("Enter the column to play: "))
            print("")


            if self.makeMove(playCol) == True:
                self.printBoard()
                self.placements += 1
                if self.checkWinner() == True:
                    print(f"Player {currentPlacement} wins!")
                    gameOver = True
                    break
                if self.placements == self.maxPlacements:
                    print(f"All spaces have been filled, it is a draw!")
                    gameOver = True
                    break
                self.playerX = not(self.playerX)
                self.playerO = not(self.playerO)

           
              

    def makeMove(self, column):
        CurrRow = 0
        if column < 0 or column > 6:
            print("Invalid column, please retry\n")
            return False
        if self.playerX:
            currentPlacement = "X"
        else:
            currentPlacement = "O"
        for i in range(0,6,1):
            if self.gameBoard[i][column] == "-":
                self.gameBoard[i][column] = currentPlacement
                return True
        print("Column full, please retry and select different column \n")
        return False


    def checkWinner(self):
        currentPlacement = ""
        if self.playerX:
            currentPlacement = "X"
        else:
            currentPlacement = "O"
        
        consecutivePlacements = 0

        ## first check horizontals
        for i in range(0,6,1):
            consecutivePlacements = 0
            for j in range(0,7,1):
                if j > 3 and consecutivePlacements == 0:
                    break
                if self.gameBoard[i][j] == currentPlacement:
                    consecutivePlacements += 1
                    if consecutivePlacements == 4:
                        return True
                else:
                    consecutivePlacements = 0

        ## next check verticals
        for j in range(0,7,1):
            consecutivePlacements = 0
            for i in range(0,6,1):
                if i > 2 and consecutivePlacements == 0:
                    break
                if self.gameBoard[i][j] == currentPlacement:
                    consecutivePlacements += 1
                    if consecutivePlacements == 4:
                        return True
                else:
                    consecutivePlacements = 0

        ##now check diagonals

        for i in range(0,2,1):
            for j in range(0,7,1):
                if j <= 3:
                    if currentPlacement == self.gameBoard[i][j] == self.gameBoard[i+1][j+1] == self.gameBoard[i+2][j+2] == self.gameBoard[i+3][j+3]:
                        return True
                if j >= 3:
                    if currentPlacement == self.gameBoard[i][j] == self.gameBoard[i+1][j-1] == self.gameBoard[i+2][j-2] == self.gameBoard[i+3][j-3]:
                        return True

        # ## next check diagonal going up to the right        
        # for i in range(3, 6, 1):
        #     consecutivePlacements = 0
        #     for j in range(0, i+1, 1):
        #         if i-j < 3 and consecutivePlacements == 0:
        #             break
        #         if self.gameBoard[i-j][j] == currentPlacement:
        #             consecutivePlacements += 1
        #             if consecutivePlacements == 4:
        #                 return True
        #         else:
        #             consecutivePlacements = 0
        
        # for j in range(1, 4, 1):
        #     addConst = 5
        #     consecutivePlacements = 0
        #     for i in range(5, j,-1 -1):
        #         if j+addConst-i > 3 and consecutivePlacements == 0:
        #             break
        #         if self.gameBoard[i][(j+addConst)-i] == currentPlacement:
        #             consecutivePlacements += 1
        #             if consecutivePlacements == 4:
        #                 return True
        #         else:
        #             consecutivePlacements = 0

        # ## next check diagonal going ? to the ? 

        # for i in range(3, 6, 1):
        #     consecutivePlacements = 0
        #     for j in range(0, 6-i-1, 1):
        #         if j-(6-i) < 3 and consecutivePlacements == 0:
        #             break
        #         if self.gameBoard[j-(6-i)][j] == currentPlacement:
        #             consecutivePlacements += 1
        #             if consecutivePlacements == 4:
        #                 print(f"Player {currentPlacement} wins!")
        #                 return True
        #         else:
        #             consecutivePlacements = 0
            
        # for j in range(5, 2, -1):
        #     subConst = 5
        #     consecutivePlacements = 0
        #     for i in range(5, j,-1 -1):
        #         if (j-subConst)+i < 3 and consecutivePlacements == 0:
        #             break
        #         if self.gameBoard[i][(j-subConst)+i] == currentPlacement:
        #             consecutivePlacements += 1
        #             if consecutivePlacements == 4:
        #                 print(f"Player {currentPlacement} wins!")
        #                 return True
        #         else:
        #             consecutivePlacements = 0
        
        return False
        
