## connect 4 main file

import Board

def main():

    gameOn = True

    print("\nWelcome to Connect 4!")

    while(gameOn):
        playInp = input("Would you to play a game of Connect 4? (y/n): ")
        
        while playInp != "y" and playInp != "n":
            playInp = input("\nInvalid Input. Would you to play a game of Connect 4? (y/n): ")

        if playInp == "y":
            playBoard = Board.Board()
            playBoard.playGame()
        elif playInp == "n":
            print("\nOk then, goodbye!\n")
            gameOn = False
            break

if __name__ == "__main__":
    main()