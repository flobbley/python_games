import sys
from random import randint
from encounter import *
from classes import *
from cave import *
from mechanics import *
def part_1():
    print('+++++++++++++++++++++++++++++++++\n')
    print('Adventure on Wilderness Mountain!\n')
    print('+++++++++++++++++++++++++++++++++\n')
    input('\nPress ENTER to continue\n')
    print('You awaken, finding your airplane crashed into the side of a mountain')
    print('You are dazed but unhurt, you look next to you. Your co-pilot is dead...')
    print('You look off into the distance, you can see a cave, barely visible through the \nsnow')
    print('You decided to head towards it, but first... who are you?')
    protag = character(1,1,1,1,1,1,15)
    protag.name = str(input('\nWhat is your name? '))
    race = str(input('\nWhat race are you? \nHuman \nOrc \nElf \n\n'))
    if race == 'human' or race == 'Human':
        protag.race = 'Human'
    elif race == 'orc' or race == 'Orc':
        protag.race = 'Orc'
    elif race == 'elf' or race == 'Elf':
        protag.race = 'Elf'
    else:
        protag.race = race
        print('I\'m sorry I don\'t recognize that..')
    if protag.race == 'Human':
        x = 'a'
    else:
        x = 'an'
    print('\nok, you\'re',x,protag.race)
        
    input('now you need to roll your stats, You have: \n\nStrength \nIntelligence \nCharisma \nand \nSpeed \n\nPress enter to roll')
    a = roll_stats()
    b = roll_stats()
    c = roll_stats()
    d = roll_stats()
    attributes = [a, b, c, d]
    print('\nYour stats are: \n',a,'\n',b, '\n',c, '\n',d)

    protag = stat_assign(a, b, c, d, protag)

    print('\nGreat,',protag.name, 'your stats are: \n\nStrength:',protag.stg, '\nIntelligence:',protag.ing, '\nCharisma:', protag.cha, '\nSpeed:', protag.spd)
    if protag.race == 'Human':
        protag.cha += 1
        a = 'you get plus one to charisma!'
    elif protag.race == 'Orc':
        protag.stg += 1
        a = 'you get plus one to strength!'
    elif protag.race == 'Elf':
        protag.spd +=1
        a = 'you get plus one to speed!'
    else:
        protag.ing += 1
        a = '... actually I don\'t know anything about them, but you seem pretty smart!'
    print('\nAnd since you\'re',x,protag.race,',',a,' \nOh and your health is 15')
    input('\nPress enter to continue\n')
    print('very well, we know who you are now... but you\'re still cold, and bit scared')
    print('you are able to unfasten your seatbelt and climb from the wreckage')
    print('you look from side to side.. it\'s nothing but snow and rock as far as the eye can see')
    print('as you drop down from the airplane cockpit, you hear the wind howl strangely')
    print('at least... you hope that\'s what it is.\n')
    print('you begin fighting your way through the blowing snow towards the cave you can barely see in the distance...')
    input()
    alive = True
    encounter_indicator = randint(1,3)
    if encounter_indicator <= 3:
        protag = yeti_encounter(protag)
        if protag.hlth <= 0:
            return
    if encounter_indicator <= 3:
        print('After your terrifying encounter, you finally arrive at the cave')
        protag = cave(protag)
    else:
        print('After what seems like forever, you finally arrive \nAt the relative warmth of the cave')
        protag = cave(protag)
        if protag.hlth <=0:
            return
    return protag


