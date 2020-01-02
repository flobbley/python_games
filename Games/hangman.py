# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import os

global clearVar
syst = os.name
if syst == 'nt':
    clearVar = "cls"
else:
    clearVar = "clear"

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    guessed = True
    for letter in secretWord:
        if letter not in lettersGuessed:
            guessed = False
    return guessed



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    currentGuess = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            currentGuess += letter
        else:
            currentGuess += '_ '
    return currentGuess



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    availableLetters = ''
    for letter in alphabet:
        if letter not in lettersGuessed:
            availableLetters += letter
    return availableLetters
            
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('I am thinking of a word that is',len(secretWord),'letters long')
    lettersGuessed = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    numGuesses = 8
    while numGuesses > 0:
        input()
        os.system(clearVar)
        valid = False
        while not valid:
            print(hungMan(numGuesses))
            print(getGuessedWord(secretWord, lettersGuessed))
            print('you have',numGuesses,'guesses left\n')
            print('Available letters:',getAvailableLetters(lettersGuessed))
            if len(lettersGuessed)>0:
                print('You\'ve already guessed:',lettersGuessed)
            guess = input('\nPlease guess a letter: ')
            guessLower = guess.lower()
            if guessLower not in lettersGuessed and guessLower in alphabet: 
                lettersGuessed += guessLower
                valid = True
                if guessLower in secretWord:
                    print('\nGood guess:',getGuessedWord(secretWord, lettersGuessed))
                else:
                    print('\nThat letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
                    numGuesses -= 1
            elif guessLower in alphabet:
                print('\nYou\'ve already guessed that letter:',getGuessedWord(secretWord, lettersGuessed))
            else:
                print('\nthat is not a valid input')
        
        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!\nThe man is saved!')
            break
        elif numGuesses == 0:
            print('Oh no! You Lose! The word was:',secretWord)
    return ''
            
        
def hungMan(numGuesses):
    if numGuesses == 8:
        print('   ___ ')
        print('  |   | ')
        print('  |     ')
        print('  |     ')
        print('  |     ')
        print('  |     ')
        print(' ------ ')
    elif numGuesses == 7:
        print('   ___ ')
        print('  |   | ')
        print('  |   O ')
        print('  |     ')
        print('  |     ')
        print('  |     ')
        print(' ------ ')
    elif numGuesses == 6:
        print('   ___ ')
        print('  |   | ')
        print('  |  \\O')
        print('  |     ')
        print('  |     ')
        print('  |     ')
        print(' ------ ')
    elif numGuesses == 5:
        print('   ___ ')
        print('  |   | ')
        print('  |  \\O/')
        print('  |     ')
        print('  |     ')
        print('  |     ')
        print(' ------ ')
    elif numGuesses == 4:
        print('   ___ ')
        print('  |   | ')
        print('  |  \\O/')
        print('  |   | ')
        print('  |     ')
        print('  |     ')
        print(' ------ ')
    
    elif numGuesses == 3:
        print('   ___ ')
        print('  |   | ')
        print('  |  \\O/')
        print('  |   | ')
        print('  |  /  ')
        print('  |     ')
        print(' ------ ')
    elif numGuesses == 2:
        print('   ___ ')
        print('  |   | ')
        print('  |  \\O/')
        print('  |   | ')
        print('  |  / \\')
        print('  |     ')
        print(' ------ ')
    elif numGuesses == 1:
        print('   ___ ')
        print('  |   | ')
        print('  |  \\O/')
        print('  |   | ')
        print('  |  / \\')
        print('  |     ')
        print(' ------ ')
        print('He\'s about to drop!')
    elif numGuesses == 0:
        print('   ___ ')
        print('  |   | ')
        print('  |   |')
        print('  |  O| ')
        print('  |  /|\\')
        print('  |  / \\')
        print(' ------ ')
    return ''
            
        
    
    






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

def runHangman():
    print('+++++++++++++++++++\n')
    print('Welcome to Hangman!\n')
    print('+++++++++++++++++++\n')
    while True:
        secretWord = chooseWord(wordlist).lower()
        print(hangman(secretWord))
        print('Would you like to play again? y/n')
        again = input()
        if again == 'n':
            break
    return ''
