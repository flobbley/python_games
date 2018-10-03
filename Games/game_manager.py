from blackJack import *
from Part_1 import *
from hangman import *
from ticTacToe import *
from ps4b import *
playing = True
while playing:
    print('\nWhat would you like to play?')
    print('1. RPG Adventure')
    print('2. Black Jack')
    print('3. Hangman')
    print('4. Tic-Tac-Toe')
    print('5. Word Finder')
    print('6. Exit')
    game = input()
    if game == '1':
        print(part_1())
    if game == '2':
        print(blackJack())
    if game == '3':
        print(runHangman())
    if game == '4':
        print(ticTacToe())
    if game == '5':
        print(runWords())
    if game == '6':
        print('Goodbye!')
        playing = False
