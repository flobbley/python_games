"""
Tic Tac Toe
"""
from random import *

def playerInput(availableGuesses):
    valid = False
    while not valid:
        print('Where would you like to go?\n')
        guessPrint = []
        for i in range(1,10):
            if i in availableGuesses:
                guessPrint.append(str(i))
            else:
                guessPrint.append(' ')
        print(' '+guessPrint[6],'|',guessPrint[7],'|',guessPrint[8],'\n-----------\n'
        ,guessPrint[3],'|',guessPrint[4],'|',guessPrint[5],'\n-----------\n'
        ,guessPrint[0],'|',guessPrint[1],'|',guessPrint[2])
        print()
        print('available moves are:', availableGuesses)
        pos = int(input())
        goodGuess = isValid(pos, availableGuesses)
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
    for i in availableGuesses:
        pos_copy = position[:]
        pos_copy[i-1] = 2
        if isWon(pos_copy, 2) == True:
            return i
        
    for i in availableGuesses:
        pos_copy = position[:]
        pos_copy[i-1] = 1
        if isWon(pos_copy, 1) == True:
            return i

    if rnd == 0:
        if position[4] == 0:
            return 5
        else:
            choose = choice([1,3,7,9])
            return choose
        
    elif rnd == 1:
        if position[0]==1 and position[8]==1:
            choose = choice([2,4,6,8])
            return choose
        elif position[6] == 1 and position[2] == 1:
            choose = choice([2,4,6,8])
            return choose
        else:
            valid = False
            while not valid:
                choose = choice([1,3,7,9])
                if choose in availableGuesses:
                    return choose
    else:
        return compGuessEasy(availableGuesses)
        
def compGuessMedium(availableGuesses, position):
    """
    computer will check if the player is about to win, and block if so
    computer will check if it can win, and win if so
    otherwise, computer will play spaces randomly
    """
    for i in availableGuesses:
        pos_copy = position[:]
        pos_copy[i-1] = 2
        if isWon(pos_copy, 2) == True:
            return i
        
    for i in availableGuesses:
        pos_copy = position[:]
        pos_copy[i-1] = 1
        if isWon(pos_copy, 1) == True:
            return i
    else:
        i = len(availableGuesses)-1
        j = randint(0,i)
        guess = availableGuesses[j]
        return guess

def compGuessEasy(availableGuesses):
    """
    computer plays spaces randomly, won't even play space to win if it has the opportunity
    """
    i = len(availableGuesses)-1
    j = randint(0,i)
    guess = availableGuesses[j]
    return guess

def guessRemover(guess, availableGuesses):
    availableGuesses.remove(guess)
    print()
    return availableGuesses

def isWon(pos, pla):
    """
    checks if spaces needed to win are occupied by the specified player (pla)
    """
    if pos[0] == pla and pos[1]==pla and pos[2]==pla:
        won = True
    elif pos[3] ==pla and pos[4]==pla and pos[5]==pla:
        won = True
    elif pos[6] ==pla and pos[7]==pla and pos[8]==pla:
        won = True
    elif pos[0] ==pla and pos[3]==pla and pos[6]==pla:
        won = True
    elif pos[1]==pla and pos[4]==pla and pos[7]==pla:
        won = True
    elif pos[2]==pla and pos[5]==pla and pos[8]==pla:
        won = True
    elif pos[0]==pla and pos[4] ==pla and pos[8]==pla:
        won = True
    elif pos[6]==pla and pos[4] == pla and pos[2]==pla:
        won = True
    else:
        won = False
    return won

def isValid(guess, availableGuesses):
    if guess in availableGuesses:
        return True
    else:
        return False

def ticPrint(position):
    """
    prints the tic-tac-toe board as guesses are made
    """
    position_mark = []
    for i in position:
        if i == 0:
            position_mark.append(' ')
        elif i == 1:
            position_mark.append('X')
        elif i == 2:
            position_mark.append('O')
    print(' '+position_mark[6],'|',position_mark[7],'|',position_mark[8],'\n-----------\n'
          ,position_mark[3],'|',position_mark[4],'|',position_mark[5],'\n-----------\n'
          ,position_mark[0],'|',position_mark[1],'|',position_mark[2])
    return ''

def diffSelect():
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
    valid = False
    while not valid:
        print("Who goes first?")
        order = input('1. Me\n2. Computer\n')
        if order == '1':
            return 0
        elif order == '2':
            return 1

def playerTurn(availableGuesses, position):
    #player turn
    pos1 = playerInput(availableGuesses)
    position[pos1-1] = 1
    availableGuesses = guessRemover(pos1, availableGuesses)
    won = isWon(position, 1)
    print('Your move:')
    print(ticPrint(position))
    return availableGuesses, position, won

def computerTurn(availableGuesses, position, difficulty, rnd):
    #computer turn
    print('Computer plays:')
    if difficulty == 2:
        pos2 = compGuessMedium(availableGuesses, position)
    elif difficulty == 1:
        pos2 = compGuessEasy(availableGuesses)
    elif difficulty == 3:
        pos2 = compGuessImpossible(availableGuesses, position, rnd)
    position[pos2-1] = 2
    availableGuesses = guessRemover(pos2, availableGuesses)
    won = isWon(position, 2)
    print(ticPrint(position))
    return availableGuesses, position, won

def ticTacToe():
    playing = True
    while playing:
        print('+++++++++++++++++++++++++++++++')
        print()
        print('Welcome to Tic-Tac-Toe!')
        print()
        print('+++++++++++++++++++++++++++++++')
        availableGuesses = [1,2,3,4,5,6,7,8,9]
        position = [0,0,0,0,0,0,0,0,0]
        difficulty = diffSelect()
        print(ticPrint(position))
        order = playOrder()
        rnd = 0
        availableGuesses = [1,2,3,4,5,6,7,8,9]
        position = [0,0,0,0,0,0,0,0,0]
        won = False
        while not won:
            
            if order == 0:                
                availableGuesses, position, won = playerTurn(availableGuesses, position)
                if won == True:
                    print('You win!\n')
                    break
                if len(availableGuesses) == 0:
                    print('Stalemate!\n')
                    break
                
            else:
                availableGuesses, position, won = computerTurn(availableGuesses, position, difficulty, rnd)
                if won == True:
                    print('The computer wins this round!\n')
                    break
                if len(availableGuesses) == 0:
                    print('Stalemate!\n')
                    break

            order = 1 - order
            rnd+=1
            
            input('Press ENTER to continue\n')
                
        print('Would you like to play again? y/n')
        game = input()
        if game == 'n':
            playing = False
            print('\nGoodbye!')
            input()
    return ''



