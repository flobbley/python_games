from mechanics import *
from classes import *
from ps3_hangman import *
def yeti_encounter(protag):
    from random import randint
    print('You run into a yeti!')
    print('   Y    Y   ')
    print(' ( o>  <o ) ')
    print('(  vvvvvv  )')
    print(' ( ^^^^^^ ) ')
    print('3---(  )---e')
    print('    J  L    ')
    yeti_health = 5
    while yeti_health > 0:
        action = input('\nWhat do you do?? \n1. Attack! \n2. Run Away! \n')
        attack_command = ['1', 'attack', 'Attack', 'Attack!']
        run_command = ['2', 'run away', 'Run away', 'Run Away', 'Run Away!']
        if action in attack_command:
            print('you swing your fist..')
            hit = randint(1,(protag.stg//2))
            if hit >= 3:
                damage = randint(1,(protag.stg//2))
                print('and it hit it! \n')
                print('you do',damage,'damage \n')
                yeti_health -= damage
                input()
                if yeti_health <= 0:
                    print('You killed the yeti! \n')
                    print('   Y    Y   ')
                    print(' ( X>  <X ) ')
                    print('(     0    )')
                    print(' (        ) ')
                    print('3---(  )---e')
                    print('    J  L    \n')
                    input()
                    break
            else:
                print('and it missed!\n')
                input()
        elif action in run_command:
            print('you try to run away...')
            run = randint(1,(protag.spd//2))
            if run >= 5:
                yeti_health = 0
                print('and you got away!')
                print('\nbut the yeti still lurks out there somewhere...\n')
                input()
                break
            else:
                print('no luck! he caught up to you! \n')
                input()
        else:
            print('you blurt out something in a stupor... \n')
        print('The yeti swings at you in a rage! \n')
        hit = randint(1,7)
        if hit >= 3:
            damage = randint(1,4)
            print('he hits you!')
            print('you take',damage,'damage')
            input()
            protag.hlth -= damage
            print(protag.hlth,'health remaining\n')
            if protag.hlth <= 0:
                print('You have been killed...')
                break
        else:
            print('but he missed!')
    return protag

def goblin_encounter(protag, deadSlimy = False):
    from collections import OrderedDict
    from buffs import shout_buff
    goblin_tribe = OrderedDict({'slimy':[3,1], 'greg':[3,2], 'crumble':[5,3]}) #sets the enemies
    if deadSlimy:
        del goblin_tribe['slimy']
    print('As things with the goblins turn hostile, you grab a nearby rock and prepare to fight')
    input()
    shout = 0
    while len(goblin_tribe)>0: #while loop continues while fight is in progress
        golbin_alive = True
        if protag.hlth <=0:
            break
        """
        Human Turn
        """
        print('What do you do??')
        for goblin in goblin_tribe:
            print(str(goblin_tribe[goblin][1]),'. Attack', goblin)#prints options for attack, will remove defeated goblins
        action = input('\n4. Run away! \n5. Shout with fury!\n')#print non-attack option
        run_command = ['4', 'run away', 'Run away', 'Run Away', 'Run Away!']
        shout_command = ['5','Shout with fury', 'Shout', 'shout', 'Shout!', 'shout!','Shout with fury!', 'shout with fury!']
        attack = ['1','2','3']
        shout = shout_buff(shout)
        if action in attack:
            if protag.checkStg(3): #performes strength check to see if hit is successful
                hit = True
                if shout>0:
                    damage = randint(1,protag.stg//2)+3
                else:
                    damage = randint(1,protag.stg//2)
                phrase_num = randint(0,4)
                attack_phrases = ['and bash him in the eye!', 'and kick him in the groin!', 'and twist his ear!', 'and punch him in the stomach!', 'and elbow him in the face!']
                kill_phrases = ['and he goes down!', 'and he keels over!, this one is out of it', 'and he screams and crumples to the ground, you think you killed him! how I don\'t know', 'and you feel him go limp, you\'ve taken care of this one!', 'Blood spurts from his nose and he collapses!']
                if action == '1' and hit == True: #performs combat if strength check is successful
                    print('You run to the first goblin,', attack_phrases[phrase_num])
                    print('\nYou do',damage,'damage')
                    goblin_tribe['slimy'][0] -= damage #adds damage
                    if goblin_tribe['slimy'][0] <= 0: #removes killed goblins
                        print(kill_phrases[phrase_num])
                        del goblin_tribe['slimy']
                    input()
                elif action == '2' and hit == True:#performs combat if strength check is successful
                    print('You run to the second goblin,', attack_phrases[phrase_num])
                    print('\nYou do',damage,'damage')
                    goblin_tribe['greg'][0] -= damage#adds damage
                    if goblin_tribe['greg'][0] <= 0:#removes killed goblins
                        print(kill_phrases[phrase_num])
                        del goblin_tribe['greg']
                    input()
                elif action == '3' and hit == True:#performs combat if strength check is successful
                    print('You run to the third goblin,', attack_phrases[phrase_num])
                    print('\nYou do',damage,'damage')
                    goblin_tribe['crumble'][0] -= damage#adds damage
                    if goblin_tribe['crumble'][0] <= 0:#removes killed goblins
                        print(kill_phrases[phrase_num])
                        del goblin_tribe['crumble']
                    input()
            else: #prints if hit misses
                print('you swing and miss!')
                input()
                
        elif action in run_command: #performs run away routine
            run_check = protag.checkSpd(7) #performs a speed check to see if you get away
            if run_check:
                if len(goblin_tribe)==2: #checks number of remaining goblins and prints appropriate response
                    print('You manage to get away! but they\'re mad that you\'ve killed their friend, they might be planning their revenge...')
                    goblin_alive = True
                    return [protag, goblin_alive]
                elif len(goblin_tribe)==1:
                    print('You managed to get away, as you\'re running you turn back to see the last goblin fleeing in terror. You don\'t think he\'ll be coming after you any time soon')
                    goblin_alive = False
                    return [protag, goblin_alive]
                else:
                    print('You manage to get away but there are still three angry goblins looking for you')
                    input()
                    goblin_alive = True
                    return [protag, goblin_alive] 
            else: #prints if speed check fails
                print('No luck! they\'ve got you in a pinch!')
                input()
        elif action in shout_command:
            shout_check = protag.checkCha(3)
            if shout_check:
                print('You let out a mighty war cry!')
                print('The goblins seem scared, and you feel stronger!')
                print('(for 2 turns: +3 damage boost for you, -2 to hit for goblins)')
                shout = shout_buff(shout,3,True)
                input('\nPress enter to continue\n')
            else:
                print('you let out a weird yelp, the goblins look at you oddly. You feel embarassed')
                input()
        else:
            print('you freeze in a panic')

            
        for goblin in goblin_tribe:
            """
            goblins turn
            """
            action_options=['attack', 'taunt', 'misc']
            taunt_list = ['"You\'re mother looks like a deviled egg!"','"I\'ve seen smarter warts than you!"', '"You\'re acne scarring is quite terrible! maybe you should see a doctor"', '"You\'re smell is so bad it\'s violating my nostrils, and I\'m a goblin!"']
            misc_list = ['gets distracted by a weird bug he sees on the wall', 'lights a stick on fire and throws it at you','has a blister on his face burst and takes time to wipe the pus from his eyes','sharpens his dagger']
            action = randint(1,3)
            if action == 1:
                print(goblin, 'shouts, and stabs at you with his dagger')
                gob_hit = randint(1,10)
                if shout>0:
                    gob_hit -=2
                if gob_hit > 5:
                    damage = randint(1,3)
                    print('and it lands!')
                    print('you take',damage,'damage')
                    protag.hlth -= damage
                    print('health:',protag.hlth)
                    if protag.hlth <= 0:
                        print('...you have been killed')
                        break
                    input()
                else:
                    print('but you deftly dodge away!')
                    input()
            elif action == 2:
                print(goblin,'slings a taunt at you:')
                print(taunt_list[randint(0,3)])
                damage = randint(1,3)
                if damage == 3:
                    print('This insult stings particularly badly, you take 2 damage')
                    protag.hlth -= 2
                    print('health:',protag.hlth)
                    if protag.hlth <= 0:
                        print('...you have been killed')
                        break
                input()
            elif action ==3:
                misc = randint(0,3)
                print(goblin,misc_list[misc])
                if misc == 1:
                    speed_check = protag.checkSpd(4)
                    if speed_check:
                        print('but you\'re able to dive away!')
                    else:
                        print('and it hits you! you can smell some singed flesh!')
                        print('you take 4 damage')
                        protag.hlth -= 4
                    print('health:',protag.hlth)
                    if protag.hlth <= 0:
                        print('...you have been killed')
                        break
                input()
    goblin_alive = False                                                              
    return [protag, goblin_alive]
    
def goblinKingFight(protag):
    print('Slimy: alright, a fight to the death then!')
    print('you take a fighting stance, prepared to defend yourself')
    input()
    print('Crumble: Wait a minute, that\'s not how we do this Slimy, and you know it')
    print('if it was, I\'d be the leader, you said being a leader is more about smarts than strength')
    input()
    print('Greg: Yeah! You made us do that thing with the words, and if we could guess your word then we won')
    print('but we didn\'t')
    input()
    print('Slimy: Fine, fine. we\'ll do it the old way, but I don\'t want this fella trying to weasle out')
    print('You get up on the scaffold, and we\'ll put a noose around your neck.')
    print('I\'m gonna think of a word, and you have to figure out what it is. I\'ll write it on this piece of paper and show it to Crumble and Greg so you know I\'m not cheating')
    print('You can guess the letters in the word, but get too many wrong and you hang.')
    input()
    print('Nervously you step onto the platform, you hope you didn\'t make a huge mistake as the game begins')
    secretWord = chooseWord(wordlist).lower()
    won = hangman(secretWord, protag)
    if won == True:
        print('the other goblins grab Slimy and tie him up, then come over and take you down')
        print('before you have a second to think they proceed to put Slimy onto the gallows and give him a hell of a hanging')
    else:
        print('Slimy laughs maniacally')
        print('Slimy: HAHAHA! I win, you lose! I\'m smarter than you!')
        print('The goblins proceed to hang you, much to your dismay.')
    return won
        
#protag = character('John', 'Orc', 18, 18, 18, 18, 15)
#print(goblinKingFight(protag))
    
    
