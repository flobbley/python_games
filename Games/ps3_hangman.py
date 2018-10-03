# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
from classes import character
from random import randint

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
            
    

def hangman(secretWord, protag):
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
    print('Slimy: I am thinking of a word that is',len(secretWord),'letters long')
    lettersGuessed = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    numGuesses = 8
    tryAct=0
    while numGuesses > 0:
        valid = False
        while not valid:
            print('you have',numGuesses,'guesses left\n')
            print('Available letters:',getAvailableLetters(lettersGuessed))
            if len(lettersGuessed)>0:
                print('You\'ve already guessed:',lettersGuessed)
            print('What do you do??')
            
            print('\n1. Guess a letter')
            if tryAct == 0:
                print('2. Think about the word [Intelligence]\n3. Sneak a peak at the word [Speed]')
            action = input()
            valid2 = False
            tryAct = 0
            while not valid2:
                if action == '1':
                    guess = input('Which letter?')
                    valid2 = True
                    valid = True
                elif action == '2' and tryAct ==0:
                    check_int = protag.checkIng(6)
                    Guessed = False
                    while not Guessed:
                        if check_int:
                            valid2 = True
                            valid = True
                            intuitLetter = randint(0,len(secretWord))
                            guess = secretWord[intuitLetter-1]
                            guessLower = guess.lower()
                            if guessLower not in lettersGuessed:
                                print('You wrack your brain, and based on your judgement of the situation you think you know one of the letters')
                                Guessed = True
                        else:
                            print('You wrack your brain as hard as you can and you still can\'t think of the right letter. You\'re just gonna have to guess')
                            tryAct +=1
                            valid2 = True
                            Guessed = True
                elif action == '3' and tryAct == 0:
                    check_spd = protag.checkSpd(6)
                    Guessed = False
                    while not Guessed:
                        if check_spd:
                            valid2 = True
                            valid = True
                            intuitLetter = randint(0,len(secretWord))
                            guess = secretWord[intuitLetter-1]
                            guessLower = guess.lower()
                            if guessLower not in lettersGuessed:
                                Guessed = True
                                print('you riggle just enough to catch a glimpse of the word. You\'re able to make out of the letters and give your guess')
                        else:
                            print('No good, no matter how you squirm you can\'t catch a glimpse of the word. You\'re just gonna have to guess')
                            tryAct += 1
                            valid2 = True
                            Guessed = True
                else:
                    valid2 = True
                    print('Invalid response')
        guessLower = guess.lower()
        if guessLower not in lettersGuessed and guessLower in alphabet: 
            lettersGuessed += guessLower
            valid = True
            if guessLower in secretWord:
                print('\nSlimy: Good guess:',getGuessedWord(secretWord, lettersGuessed))
            else:
                print('\nSlimy: That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
                numGuesses -= 1
        elif guessLower in alphabet:
            print('\nSlimy: You\'ve already guessed that letter!:',getGuessedWord(secretWord, lettersGuessed))
        else:
            print('\nthat is not a valid input')
        print(hungMan(numGuesses))
        input('press ENTER to continue\n')
        if isWordGuessed(secretWord, lettersGuessed):
            print('Slimy: What! no, you can\'t have guessed my word, it was too good! No!')
            input('')
            won = True
            return won
        elif numGuesses == 0:
            print('Slimy: Haha! You Lose! The word was:',secretWord)
            input('')
            won = False
    return won
            
        
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

#protag = character('John', 'Orc', 18, 18, 18, 18, 15)
#secretWord = chooseWord(wordlist).lower()
#hangman(secretWord, protag)
