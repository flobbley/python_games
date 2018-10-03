from random import *
from classes import *
def roll_stats():
    a = randint(1,6)#creates 4 random numbers
    b = randint(1,6)
    c = randint(1,6)
    d = randint(1,6)
    s = [a,b,c,d,]#puts numbers into a list
    s = sorted(s) #sorts number list
    s = s[1:4]#removes lowest number
    total = 0
    for i in s:
        total += i #adds three remaining numbers
    return total

def stat_assign(a,b,c,d,protag):
    """
    this program takes rolled stats and assigns them into attributes
    takes: stats rolled in game
    returns: attributes with assigned stats
    """
    attributes = [a, b, c, d]
    assigned = False
    while not assigned:
        protag.stg = int(input('What would you like to use for your strength? '))
        if protag.stg not in attributes:
            print('I\'m sorry, that is not a valid stat')
        else:
            attributes.remove(protag.stg)
            assigned = True
    assigned = False
    while not assigned:
        protag.ing = int(input('What would you like to use for your intelligence? '))
        if protag.ing not in attributes:
            print('I\'m sorry, that is not a valid stat')
        else:
            attributes.remove(protag.ing)
            assigned = True
    assigned = False
    while not assigned:        
        protag.cha = int(input('What would you like to use for your charisma? '))
        if protag.cha not in attributes:
            print('I\'m sorry, that is not a valid stat')
        else:
            attributes.remove(protag.cha)
            assigned = True
    assigned = False
    while not assigned:
        protag.spd = int(input('What would you like to use for your speed? '))
        if protag.spd not in attributes:
            print('I\'m sorry, that is not a valid stat')
        else:
            attributes.remove(protag.spd)
            assigned = True
    return protag

def check(stat,difficulty):
    roll = randint(1,stat)
    if roll > difficulty:
        success = True
    else:
        success = False
    return success

    
