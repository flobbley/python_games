"""
Tic Tac Toe
"""
from random import *
import os

global clearVar
syst = os.name
if syst == 'nt':
    clearVar = "cls"
else:
    clearVar = "clear"

def playerInput(availableGuesses):
    valid = False
    while not valid:
        print('Where would you like to go?\n')
        guessPrint = []
        for i in range(1,10):
            if i in availableGuesses:
                guessPrint.append(str(i)) #creates list of guesses available to the player
            else:
                guessPrint.append(' ')
        print(' '+guessPrint[6],'|',guessPrint[7],'|',guessPrint[8],'\n-----------\n'
        ,guessPrint[3],'|',guessPrint[4],'|',guessPrint[5],'\n-----------\n'
        ,guessPrint[0],'|',guessPrint[1],'|',guessPrint[2]) #Prints grid of available guesses and associated number input
        print()
        print('available moves are:', availableGuesses)
        pos = int(input())
        goodGuess = isValid(pos, availableGuesses) #makes sure the player guess is in the available guesses
        if goodGuess == True:
            valid = True
            return pos
        
def compGuessImpossible(availableGuesses, position, rnd):
    """
    computer cannot lose
    in first round, computer checks if middle square is taken. if middle square is taken, computer marks space to block eventual player win.
    in second round, computer checks which additional space is taken and will play accordingly to block player win
    computer will check if the player is about to win, and block if so
    computer will check if it can win, and win if so
    otherwise, computer will play spaces randomly
    """
    for i in availableGuesses: #checks if the computer can win by "playing" all the available guesses and checking if they win
        pos_copy = position[:]
        pos_copy[i-1] = 2
        if isWon(pos_copy, 2) == True:
            return i
        
    for i in availableGuesses: #checks if the player can win by "playing" all the available guesses and checking if they win
        pos_copy = position[:]
        pos_copy[i-1] = 1
        if isWon(pos_copy, 1) == True:
            return i

    if rnd == 0: #if it's the first round, the computer will try to play the middle space, if it's taken it will play a corner space
        if position[4] == 0:
            return 5
        else:
            choose = choice([1,3,7,9])
            return choose
        
    elif rnd == 1: # in the second round, the computer will play to block player win (if it can't win)
        if position[0]==1 and position[8]==1: #checks if opposite corners are taken by the player and if so, plays a side space
            choose = choice([2,4,6,8])
            return choose
        elif position[6] == 1 and position[2] == 1:
            choose = choice([2,4,6,8])
            return choose
        else: #If opposite corners are not taken by player, plays a corner space
            valid = False
            while not valid:
                choose = choice([1,3,7,9])
                if choose in availableGuesses:#will continue to guess corner spaces until it guesses a corner space that is not occupied
                    return choose
    else:
        return compGuessEasy(availableGuesses)#if the above conditions are not met, guesses randomly
        
def compGuessMedium(availableGuesses, position):
    """
    computer will check if the player is about to win, and block if so
    computer will check if it can win, and win if so
    otherwise, computer will play spaces randomly
    """
    for i in availableGuesses: #checks if the computer can win by "playing" all the available guesses and checking if they win
        pos_copy = position[:]
        pos_copy[i-1] = 2
        if isWon(pos_copy, 2) == True:
            return i
        
    for i in availableGuesses: #checks if the player can win by "playing" all the available guesses and checking if they win
        pos_copy = position[:]
        pos_copy[i-1] = 1
        if isWon(pos_copy, 1) == True:
            return i
    else:
        return compGuessEasy(availableGuesses) #if the above conditions are not met, guesses randomly

def compGuessEasy(availableGuesses):
    """
    computer plays spaces randomly, won't even play space to win if it has the opportunity
    """
    i = len(availableGuesses)-1 #returns a random value from the list of available guesses
    j = randint(0,i)
    guess = availableGuesses[j]
    return guess

def guessRemover(guess, availableGuesses):
    """
    removes guessed spaces from the list of available guesses
    """
    availableGuesses.remove(guess)
    print()
    return availableGuesses

def isWon(pos, pla):
    """
    checks if spaces needed to win are occupied by the specified player (pla)
    """
    if pos[0] == pla and pos[1]==pla and pos[2]==pla: #checks bottom row
        won = True
    elif pos[3] ==pla and pos[4]==pla and pos[5]==pla: #checks middle row
        won = True
    elif pos[6] ==pla and pos[7]==pla and pos[8]==pla: #checks top row
        won = True
    elif pos[0] ==pla and pos[3]==pla and pos[6]==pla: #checks left column
        won = True
    elif pos[1]==pla and pos[4]==pla and pos[7]==pla: #checks middle column
        won = True
    elif pos[2]==pla and pos[5]==pla and pos[8]==pla: #checks right column
        won = True
    elif pos[0]==pla and pos[4] ==pla and pos[8]==pla: #checks forward diagonal
        won = True
    elif pos[6]==pla and pos[4] == pla and pos[2]==pla: #checks backward diagonal
        won = True
    else:
        won = False
    return won

def isValid(guess, availableGuesses):
    """
    determines if a guess is in the available guesses
    """
    if guess in availableGuesses:
        return True
    else:
        return False

def ticPrint(position):
    """
    prints the tic-tac-toe board as guesses are made
    """
    position_mark = []
    for i in position: #fills the "position_mark" list with the appropriate marker depending on who occupies a space
        if i == 0: #0 represents an unoccupied space
            position_mark.append(' ')
        elif i == 1: #1 represents a space occupied by the player
            position_mark.append('X')
        elif i == 2: #2 represents a space occupied by the computer
            position_mark.append('O')
    print(' '+position_mark[6],'|',position_mark[7],'|',position_mark[8],'\n-----------\n' #Prints the Tic Tac Toe board with the marked spaces
          ,position_mark[3],'|',position_mark[4],'|',position_mark[5],'\n-----------\n'
          ,position_mark[0],'|',position_mark[1],'|',position_mark[2])
    return ''

def diffSelect():
    """
    Allows the player to select the difficulty they would like to play
    """
    valid = False
    while not valid:
        print("\nWhat difficulty would you like?")
        diff = input('1. Easy\n2. Medium\n3. Impossible\n')
        if diff == '1':
            return 1
        elif diff == '2':
            return 2
        elif diff == '3':
            return 3
        else:
            print('Invalid Option')

def playOrder():
    """
    Determines the play order
    """
    valid = False
    while not valid:
        print("Who goes first?")
        order = input('1. Me\n2. Computer\n')
        if order == '1':
            return 0
        elif order == '2':
            return 1

def playerTurn(availableGuesses, position):
    """
    player turn
    """
    os.system(clearVar)
    print(ticPrint(position))
    pos1 = playerInput(availableGuesses) #asks the player for a guess
    position[pos1-1] = 1 #places a player marker in the space chosen
    availableGuesses = guessRemover(pos1, availableGuesses) #removes guessed space from available guesses
    won = isWon(position, 1) #checks if the player won in this round
    os.system(clearVar)
    print('Your move:')
    print(ticPrint(position))
    return availableGuesses, position, won

def computerTurn(availableGuesses, position, difficulty, rnd):
    """
    Computer turn, plays according to difficulty selected
    """
    os.system(clearVar)
    print('Computer plays:')
    if difficulty == 2:
        pos2 = compGuessMedium(availableGuesses, position)
    elif difficulty == 1:
        pos2 = compGuessEasy(availableGuesses)
    elif difficulty == 3:      
        pos2 = compGuessImpossible(availableGuesses, position, rnd)
        rnd+=1
    position[pos2-1] = 2
    availableGuesses = guessRemover(pos2, availableGuesses)
    won = isWon(position, 2)
    print(ticPrint(position))
    return availableGuesses, position, won, rnd

def ticTacToe():
    while True:
        print('+++++++++++++++++++++++++++++++')
        print()
        print('Welcome to Tic-Tac-Toe!')
        print()
        print('+++++++++++++++++++++++++++++++')
        availableGuesses = [1,2,3,4,5,6,7,8,9] #fills the available guess positions
        position = [0,0,0,0,0,0,0,0,0] #blanks the board
        difficulty = diffSelect()
        order = playOrder() #determines play order, 0 is player first, 1 is computer first
        rnd = 0
        won = False
        while not won:
            if order == 0: #when "order" is 0 it is the player's turn             
                availableGuesses, position, won = playerTurn(availableGuesses, position)
                if won == True:
                    print('You win!\n')
                    break
                if len(availableGuesses) == 0:
                    print('Stalemate!\n')
                    break
                
            else: #when "order" is not 0 it is the computer's turn
                availableGuesses, position, won, rnd = computerTurn(availableGuesses, position, difficulty, rnd)
                if won == True:
                    print('The computer wins this round!\n')
                    break
                if len(availableGuesses) == 0:
                    print('Stalemate!\n')
                    break

            order = 1 - order #changes the turn
            
            input('Press ENTER to continue\n')
                
        print('Would you like to play again? y/n') #play again prompt
        game = input()
        if game == 'n':
            print('\nGoodbye!')
            input()
            break
    return ''

