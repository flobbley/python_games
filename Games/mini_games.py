from random import *
from mechanics import *
from classes import *
def rps(protag):
    player_score =0
    opponent_score = 0
    cheat = 0
    print('"ok, 3 out of 5"')
    while player_score < 3 and opponent_score < 3:
        print('\n"1... 2... 3... Shoot!"')
        throw = ['rock','paper','scissors']
        valid = False
        while not valid:
            action = int(input('1. Rock\n2. Paper\n3. Scissors\n4. [Speed] Cheat\n'))
            if action == 1 or action == 2 or action == 3:
                win = randint(1,3)
                print(win)
                play_throw = throw[action-1]
                if win == 2:
                    op_throw = throw[action-2]
                    print('You throw',str(play_throw)+',','he throws', str(op_throw)+',', 'you win!')
                    player_score +=1
                    input()
                elif win == 1:
                    op_throw = throw[action-3]
                    print('You throw',str(play_throw)+',','he throws', str(op_throw)+',', 'he wins!')
                    opponent_score +=1
                    input()
                else:
                    print('you both throw',str(play_throw)+',','it\'s a tie!')
                    input()
                valid = True
            elif action == 4:
                valid = True
                speed_check = protag.checkSpd(5)
                if speed_check:
                    value = randint(0,2)
                    op_throw = throw[value]
                    play_throw = throw[value-2]        
                    print('You see him start to throw',str(op_throw)+',','so in a split second you change yours to',play_throw)
                    player_score += 1
                else:
                    print('the man spots you tring to change your throw')
                    print('\nMan: Hey you\'re trying to cheat!')
                    cheat += 1
                    if cheat < 2:
                        print('Slimy: No cheating! cheat again and we\'ll just eat you!')
                    else:
                        print('Greg: That\'s it! you\'re getting eaten!')
                        opponent_score += 3
                        input()
            else:
                print('Invalid input, please enter the number of action you would like to do.')
            print('\nscore: \nyou -', player_score,'\nhim -',opponent_score) 
    if player_score == 3:
        return True
    else:
        return False
                    
                
            
