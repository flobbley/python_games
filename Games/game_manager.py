import os
from blackJack import *
from Part_1 import *
from hangman import *
from ticTacToe import *
from ps4b import *
from snake import *
from blue import *

global clearVar
syst = os.name
if syst == 'nt':
    clearVar = "cls"
else:
    clearVar = "clear"
    
playing = True
while playing:
    os.system(clearVar)
    print('FLOBBLETECH GAME CENTER')
    print('\nWhat would you like to play?')
    print('1. RPG Adventure')
    print('2. Pokemon Red/Blue')
    print('3. Black Jack')
    print('4. Hangman')
    print('5. Tic-Tac-Toe')
    print('6. Word Finder')
    print('7. Snake')
    print('8. Exit')
    game = input()
    if game == '1':
        os.system(clearVar)
        print(part_1())
    if game == '2':
        os.system(clearVar)
        print(pokemon())
    if game == '3':
        os.system(clearVar)
        print(blackJack())
    if game == '4':
        os.system(clearVar)
        print(runHangman())
    if game == '5':
        os.system(clearVar)
        print(ticTacToe())
    if game == '6':
        os.system(clearVar)
        print(runWords())
    if game == '7':
        os.system(clearVar)
        print(snake())
    if game == '8':
        print('Goodbye!')
        input()
        playing = False
