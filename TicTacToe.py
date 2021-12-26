"""
Created on 2021-12-26

@author: judyr
"""
"""
declare global variables 
"""
runtimes = 0

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

player = "X"

win_loss_stats = {"X": 0, "O": 0, "tie": 0}

def board_visual():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(" -- -- -- ")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(" -- -- -- ")
    print(board[6] + " | " + board[7] + " | " + board[8])


def is_valid_slot(userinput):
    if (board[int(userinput) - 1] == "X" or board[int(userinput) - 1] == "O"):
        return False
    else:
        return True

"""
    try:
        slot = input("Which slot would you like to move to?")
    except IndexError or ValueError:
        print("Not a valid number. Please select another value.")
"""

def userinput_number():


    slot = input("Which slot would you like to move to?")

    while not (is_valid_slot(slot)):

        slot = input("That slot has already been taken. Which slot would you "
                     "like to move to?")

    return slot


"""
pass in userinput_number into slotnumber parameter, and player into whichplayer
"""
def create_updated_board(slotnumber, whichplayer):

    global board
    board[int(slotnumber) - 1] = whichplayer

    return board

"""

"""


def switchTurns():

    global player

    if player == "X":
        player = "O"
    else:
        player = "X"

def check_who_won(player):
    #top row
    if (player == board[0]) and (board[0] == board[1] == board[2]):
        return player
    #second row
    if (player == board[3]) and (board[3] == board[4] == board[5]):
        return player
    #third row
    if (player == board[6]) and (board[6] == board[7] == board[8]):
        return player
    #left column
    if (player == board[0]) and (board[0] == board[3] == board[6]):
        return player
    # middle column
    if (player == board[1]) and (board[1] == board[4] == board[7]):
        return player
    # right column
    if (player == board[2]) and (board[2] == board[5] == board[8]):
        return player
    #diagonal, starting from top left
    if (player == board[0]) and (board[0] == board[4] == board[8]):
        return player
    #diagonal, starting from top right
    if (player == board[2]) and (board[2] == board[4] == board[6]):
        return player
    #check for tie at the end of the game
    if runtimes == 8:
        return "tie"
    else:
        return "continue"



def runGame():

    global win_loss_stats, runtimes, board

    # show board for the first time (for subsequent times code will be
    # written at bottom)
    print("Hey there! Welcome to tic-tac-toe for two.")

    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    runtimes = 0

    board_visual()

    who_won = "continue"

    while who_won == "continue":
        #indicate whose turn it is

        print("It is " + player + "'s turn.")

        #take player's selection, update board

        create_updated_board(userinput_number(), player)

        board_visual()

        #switch turns

        who_won = check_who_won(player)

        switchTurns()

        runtimes += 1

    if who_won == "X":
        win_loss_stats["X"] += 1
        return "X won!"
    if who_won == "O":
        win_loss_stats["O"] += 1
        return "O won!"
    else:
        win_loss_stats["tie"] += 1
        return "It's a tie!"


if __name__ == '__main__':

    onemoregame = 'yes'

    while onemoregame == 'yes':
        game_result = runGame()
        print(game_result)
        onemoregame = input("Do you want to play again? yes or no>")

    print("Thanks for playing tic-tac-toe!" + game_result)
    print("X won " + str(win_loss_stats["X"]) + " games; O won " + str(
        win_loss_stats["0"]) + " games; There were " + str(win_loss_stats[
                                                                                                                                  "tie"]) + " ties.")