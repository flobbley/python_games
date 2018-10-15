from mechanics import *
from encounter import *
from mini_games import *
from classes import *
def cave(protag):
    """
    Begins the cave section of the game, needs all stats and race
    """
    print('As you enter the cave you feel all of the exhaustion of your ordeal come over you')
    print('All you can think about is sleep, and you want to lie down.. but what if there is something else in here?...')
    input('\nPress enter to continue\n')
    act1_response = ['1','Lie down and rest','lie down and rest']
    act2_response = ['2','Explore the cave','explore the cave']
    valid = False
    goblins_alive = True
    while not valid: #while loop makes sure responses are valid, will cycle through until a valid response is recieved
        print('What would you like to do?')
        action = input('1. Lie down and rest (restores health)\n2. Explore the cave\n')
        if action in act1_response: #checks if user input is to rest
            print('You decide it\'s best to get some rest... if there is anything in the cave')
            print('you would not be able to do anything about it today anyway...\n')
            print('As you begin to fall asleep you notice a small light in one of the tunnels')
            input('\nPress enter to continue\n')
            int_check = protag.checkIng(6) #performs in check to see if goblins are discovered, then enters results into following if statement
            if int_check:
                print('Thanks to you\'re quick wit you instantly realize whats going on..')
                print('it\'s Goblins! they\'re all over these mountains and must live in these caves!')
                protag = int_check_goblins(protag)
            else:
                print('but your eyes are too heavy, and can\'t do anything about it, within seconds you are asleep')
                protag.hlth = 15
                opponent_eaten = sleep(protag)
                if opponent_eaten:
                    print('With the goblins gone you have time to work yourself out of the cage, it\'s not exactly the sturdiest construction, and with some effort you manage to break the door hinges')
                    print('With no where else to go you cautiously decide to enter the Dark Cave')
                    protag = exploreDarkCave(protag, True, 0)
                
            valid = True
        elif action in act2_response: #checks if user input is to explore cave
            valid = True
            print('Begrudgingly, you enter deeper into the cave, your legs begging you to stop')
            print('as you approach the back of the first chamber, you see two tunnels. One is dark, and empty\n in the other you think you see a faint light in the distance growing brighter, and what sound like they could be voices')
            input('\nPress enter to continue\n')
            int_check = protag.checkIng(6)#performs in check to see if goblins are discovered, then enters results into following if statement
            if int_check:
                print('Thanks to you\'re quick wit you instantly realize whats going on..')
                print('it\'s Goblins! they\'re all over these mountains and must live in these caves!')
                input()
                protag = int_check_goblins(protag)
            else: #if user fails int check, gives options for exploration
                act1_response = ['1','Enter the dark tunnel','enter the dark tunnel']
                act2_response = ['2', 'Enter the lighted tunnel', 'enter the lighted tunnel']
                act3_response = ['3', 'Go back and go to sleep', 'go back and go to sleep']
                valid2 = False
                while not valid2:#while loop makes sure respones are valid, will cycle through until a valid response is recieved
                    print('What would you like to do?')
                    action = input('\n1. Enter the dark tunnel\n2. Enter the lighted tunnel\n3. Go back and sleep\n')
                    if action in act1_response:
                        protag = exploreDarkCave(protag, True, 0)
                        valid2 = True
                    elif action in act2_response:
                        print('You enter the lighted tunnel, there might be some people here that can help you, and sure enough soon you hear voices!')
                        print('Slimy: They cut me! I can\'t have them cutting me every night when we go to sleep!')
                        input()
                        print('Crumble: Aww it\'s not that bad, a little cut ain\'t nothing')
                        input()
                        print('Greg: it\'s not the cuts Crumble, it\'s how dirty they are, it\'ll cause an infection')
                        input()
                        print('Slimy: Wait, what\'s that up ahead? it\'s another person!')
                        input()
                        print('Greg: let\'s get him! we\'ll have breakfast and dinner tomorrow!')
                        input()
                        print('All too late you realize it\'s not people in these caves, but goblins! and now they\'ve got you cornered, eager to feast on your bones')
                        results = goblin_encounter(protag)#temporary to check compatibility
                        protag = results[0]
                        if protag.hlth <= 0:
                            sys.exit()
                        goblins_alive = results[1]
                        if goblins_alive == False:
                            protag = safeSleep(protag, False)
                        else:
                            print('\nYou flee the only way you can! Towards the dark cave\n')
                            input()
                            protag = exploreDarkCave(protag, True, 0)
                        valid2 = True
                    elif action in act3_response:
                        print('You look at tunnels and feel overwhelming exhaustion, you decide it\'s best to just head back and find a place to sleep')
                        print('You lie down near the entrance of the cave, pulling your legs in close for warmth. Without even realizing it, you\'ve drifted off to sleep')
                        input()
                        opponent_eaten = sleep(protag)
                        if opponent_eaten:
                            print('With the goblins gone you have time to work yourself out of the cage, it\'s not exactly the sturdiest construction, and with some effort you manage to break the door hinges')
                            protag = safeSleep(protag, True)
                        else:
                            print('check if goblins alive from encounter, then print appropriate explore module')
                        valid2 = True
                    else:
                        print('invalid input\n')
        else:
            print('invalid input\n')
    return(protag)

def sleep(protag):
    print('\nAfter what feels like an eternity, you slowly open your eyes. You dont know how long it\'s been since you needed a night of sleep so badly')
    print('But as you take in your surroundings you realize something is terribly wrong')
    print('You find yourself in a wooden cage, a man is in a wooden cage next to you, and in front of you stand three short goblins, one much fatter than the others')
    input('\nPress enter to continue\n')
    print('Crumble: But I\'m Staaaarving, let\'s just pick one.')
    input()
    print('Slimy: Fine, but I can\'t pick, let\'s have them rock paper scissors for it')
    input()
    print('Greg: Now thats a fine idea!')
    input()
    print('Slimy: Alright you two, RPS, loser gets eaten')
    valid = False
    reps = 0
    convince = 0
    while not valid:
        print('What do you do??')
        print('1. RPS')
        if convince == 0:
            print('2. [Charisma] Convince them to make you their king')
        print('3. [Strength] Try to break out of the cage')
        action = input()
        if action == '1':
            print('You turn to the man in the cage next to you and hold out a fist sitting on an open palm')
            print('Begrudgingly, he does the same')
            valid = True
            success = rps(protag)
            if success:
                print('The goblins open the stranger\'s cage and drag him out, clawing and screaming')
                print('You see them drag him to another chamber deeper into the cave... You sense that now is your chance to escape')
                return True
            else:
                print('The goblins drag you from your cage, but you manage to kick one hard enough to get yourself free\n')
                results = goblin_encounter(protag)
                protag = results[0]
                if protag.hlth <=0:
                    sys.exit()
                goblins_alive = results[1]
                if goblins_alive == False:
                    results = exploreLightCaveGA(protag, goblins_alive, True)
                    protag = results[0]
                    companion = results[1]
                    print('With no where else to go, you cautiously enter the Dark Tunnel')
                    protag = exploreDarkCave(protag, goblins_alive, companion)
        elif action == '2' and convince == 0:
            if protag.race == 'Orc':
                char_check = True
            else:
                char_check = protag.checkCha(7)
            if char_check:
                print('I\'m your king now!')
                results = goblinKing(protag)
                if not results:
                    break
                else:
                    protag = results[0]
                    if protag.hlth <=0:
                        sys.exit()
                    companion = results[1]
                    protag = exploreDarkCave(protag, goblins_alive, companion)
                    valid = True
            else:
                print('The goblins laugh at you')
                convince += 1
        elif action == '3':
            if reps < 4:
                print('You ram your shoulder against the cage door in an attempt to break free')
                input()
                strength_check = protag.checkStg(9)
                if strength_check:
                    valid = True
                    print('and you smash right through! but the goblins are less than happy to say the least')
                    results = goblin_encounter(protag)
                    protag = results[0]
                    if protag.hlth <=0:
                        sys.exit()
                    goblins_alive = results[1]
                    if goblins_alive == False:
                        results = exploreLightCaveGA(protag, goblins_alive, True)
                        protag = results[0]
                        companion = results[1]
                        print('With no where else to go, you cautiously enter the Dark Tunnel')
                        protag = exploreDarkCave(protag, goblins_alive, companion)
                    else:
                        protag = exploreDarkCave(protag, goblins_alive, 0)
                else:
                    print('but you flop feebly against the wood, your shoulder hurts. You think this will leave a bruise. Health -1')
                    reps += 1
                    protag.hlth -=1
                    print('health:',protag.hlth)
                    if protag.hlth <= 0:
                        print('and you somehow manage to kill yourself')
                        break
            else:
                print('You try, but you can\'t bring youself to try and hit the door again, you\'ve hurt yourself too much')

def int_check_goblins(protag):
    valid = False
    while not valid:
        print('What do you do??')
        print('1. [Speed] Attempt to hide\n2. Enter the dark corridor \n3. charge at the goblins')
        action = input()
        if action == '1':
            valid = True
            valid2 = False
            while not valid2:
                print('You look around for a place to hide, you see:')
                print('1. A large rock\n2. A shadowy nook')
                action = input('where would you like to hide?\n')
                if action == '1':
                    valid2 = True
                    speed_check = protag.checkSpd(7)
                    if speed_check:
                        print('It seems like they\'re passing by without noticing you, heading towards the dark tunnel. As they get close you overhear them talking:')
                        print('\nSlimy: And that\'s why we gotta start trimming your toe nails crumble')
                        input()
                        print('\nCrumble: I\'m staaaarving, can\'t we just go back and eat that man we caught?')
                        input()
                        print('Greg: No! for the last time we\'re saving him for breakfast, besides we have to find a way into the map room')
                        input()
                        print('Crumble: I hope there\'s some fresh meat from that plane that crashed earlier, let\'s go check it out tomorrow, if that Yeti is gone that is')
                        input()
                        print('The goblins pass into the dark corridor, the last thing you hear is them discussing that they\'ll be down there until late morning')
                        input()
                        print('You feel safe sleeping now, or you can explore the lighted tunnel that they came from')
                        action = input('\n1. Go to sleep [health restored]\n2. Explore the lighted tunnel')
                        valid3 = False
                        while not valid3:
                            if action == '1':
                                valid3 = True
                                protag.hlth = 15
                                protag = safeSleep(protag)
                            elif action == '2':
                                valid3 = True
                                results = exploreLightCaveGA(protag, True)
                                protag = results[0]
                                companion = results[1]
                                print('With no where else to go, you cautiously enter the Dark Tunnel')
                                protag = exploreDarkCave(protag, True, companion)
                            else:
                                print('\nInvalid response, please enter the number of the action you would like to do\n')                        
                    else:
                        print('No good! the goblins have spotted you and come charging over, weapons drawn. There\'s nowhere to run!\n')
                        results = goblin_encounter(protag)
                        protag = results[0]
                        if protag.hlth <=0:
                            sys.exit()
                        goblins_alive = results[1]
                        if goblins_alive == False:
                            protag = safeSleep(protag, False)
                elif action == '2':
                    valid2 = True
                    speed_check = protag.checkSpd(4)
                    if speed_check:
                        print('It seems like they\'re passing by without noticing you, heading towards the dark tunnel. As they get close you overhear them talking:')
                        print('\nSlimy: And that\'s why we gotta start trimming your toe nails crumble')
                        input()
                        print('Crumble: I\'m staaaarving, can\'t we just go back and eat that man we caught?')
                        input()
                        print('Greg: No! for the last time we\'re saving him for breakfast, besides we have to find a way into the map room')
                        input()
                        print('Crumble: I hope there\'s some fresh meat from that plane that crashed earlier, let\'s go check it out tomorrow, if that Yeti is gone that is')
                        input()
                        print('The goblins pass into the dark corridor, the last thing you hear is them discussing that they\'ll be down there until late morning')
                        print('You feel safe sleeping now, or you can explore the lighted tunnel that they came from:')
                        action = input('\n1. Go to sleep [health restored]\n2. Explore the lighted tunnel\n')
                        valid3 = False
                        while not valid3:
                            if action == '1':
                                valid3 = True
                                protag = safeSleep(protag, True)
                            elif action == '2':
                                valid3 = True
                                results = exploreLightCaveGA(protag, True)
                                protag = results[0]
                                companion = results[1]
                                print('With no where else to go, you cautiously enter the Dark Tunnel')
                                protag = exploreDarkCave(protag, True, companion)
                            else:
                                print('\nInvalid response, please enter the number of the action you would like to do\n')
                    else:
                        print('No good! the goblins have spotted you and come charging over, weapons drawn. There\'s nowhere to run!\n')
                        results = goblin_encounter(protag)
                        protag = results[0]
                        if protag.hlth <=0:
                            sys.exit()
                        goblins_alive = results[1]
                        if goblins_alive == False:
                            protag = safeSleep(protag, False)
                        else:
                            print('You run the only clear direction, toward the light cave')
                            results = exploreLightCaveGA(protag, True)
                            protag = results[0]
                            companion = results[1]
                            print('With no where else to go, you cautiously enter the Dark Tunnnel')
                            protag = exploreDarkCave(protag, True, companion)
                else:
                    print('\nInvalid response, please enter the number of the action you would like to do\n')
        elif action == '2':
            protag = exploreDarkCave(protag, True, 0)
            valid = True
        elif action == '3':
            valid = True
            print('Greg: hey, what\'s that?')
            input()
            print('Crumble: it\'s a person! Quick, let\'s get him!')
            results = goblin_encounter(protag)
            protag = results[0]
            if protag.hlth <=0:
                sys.exit()
            goblins_alive = results[1]
            if goblins_alive == False:
                protag = safeSleep(protag, False)
    return protag
                    
                
def goblinKing(protag):
    print('The goblins shudder at the sound of your thunderous voice')
    print('After a moment, the shortest goblin speaks')
    input()
    print('Slimy: That\'s where you\'re wrong, I\'M the leader of this bunch, and you\'d have to kill me to take it')
    input()
    print('At that moment, the other goblins turned to look at him as he realized his mistake')
    print('Greg: Alright then! Crumble! let the prisoner out, it\'s a dual to the death!')
    input()
    print('The goblins open the cage door and stand you infront of your opponent')
    won = goblinKingFight(protag)
    if won == True:
        print('After taking care of Slimy, the two remaining goblins come to talk to you')
        input()
        print('Greg: Alright sir, you\'re our leader now. To bring you up to speed...')
        input()
        print('Crumble: I\'m still STAAARVING, I can\'t do anything until we eat. Now let\'s get our meal going')
        input()
        print('It is clear that the goblins intend to eat the remaining prisoner and are about to take him out of his cage')
        valid = False
        while not valid:
            print('What do you do??')
            action = input('1. Let the goblins eat the man \n2. Let the goblins eat the man, and take a few bites yourself \n3. Refuse to let the goblins eat the man\n')
            if action == '1':
                valid = True
                print('The goblins proceed the cook the man over the fire and have a delicious, nutritious meal of him. ')
                input()
                print('Crumble: Uggghhh....')
                input()
                print('Greg: Now like I was saying Boss, we\'ve been trying to get into the map room in the other chamber, the map in there is supposed to lead to unimaginable treasure')
                print('but there\'s a puzzle we need to solve to get in, and we just haven\'t been able to do it. But with big smart you with us now, I\'m sure we\'ll solve it')
                input()
                print('After their "dinner" the three of you head into the dark chamber...')
                protag = exploreDarkCave(protag, True, 2)
            elif action == '2':
                valid = True
                print('The goblins proceed the cook the man over the fire and have a delicious, nutritious meal of him. After a few bites you realize it\'s pretty tasty and already you\'re feeling reinvigorated. You didn\'t realize how hungry you were before.')
                print('your health is restored to 15')
                input()
                print('Crumble: Uggghhh....')
                input()
                print('Greg: Now like I was saying Boss, we\'ve been trying to get into the map room in the other chamber, the map in there is supposed to lead to unimaginable treasure')
                print('but there\'s a puzzle we need to solve to get in, and we just haven\'t been able to do it. But with big smart you with us now, I\'m sure we\'ll solve it')
                input()
                print('After you have your dinner, the three of you head into the dark chamber...')
                protag.hlth = 15
                protag = exploreDarkCave(protag, True, 2)
            elif action == '3':
                print('\nYou: No. You are not eating him, that\'s barbaric')
                input()
                print('Greg: Listen Bub, you might be in charge now, but we\'re starving and we\'ve got to eat something. It can be him, or it can be you. What do you say?')
                valid2 = False
                while not valid2:
                    print('What do you do??')
                    action2 = input('1. Let them eat him\n2. Stop them')
                    if action2 == '1':
                        print('The goblins proceed the cook the man over the fire and have a delicious, nutritious meal of him. ')
                        input()
                        print('Crumble: Uggghhh....')
                        input()
                        print('Greg: Now like I was saying Boss, we\'ve been trying to get into the map room in the other chamber, the map in there is supposed to lead to unimaginable treasure')
                        print('but there\'s a puzzle we need to solve to get in, and we just haven\'t been able to do it. But with big smart you with us now, I\'m sure we\'ll solve it')
                        input()
                        print('After their "dinner" the three of you head into the dark chamber...')
                        protag = exploreDarkCave(protag, True, 2)
                    elif action2 == '2':
                        print('You: I don\'t care, if you want to eat him you\'ll have to go through me')
                        input()
                        print('You hear an inhumane sound as you see crumble charge madly toward you')
                        print('Crumble: I need to EEEEEAAAAAAT')
                        results = goblin_encounter(protag, True)
                        protag = results[0]
                        if protag.hlth <=0:
                            sys.exit()
                        goblins_alive = results[1]
                        if goblins_alive == False:
                            print('after taking a minute to catch your breath, you turn to face the man in the cage')
                            results = exploreLightCaveGA(protag, False, True)
                            protag = results[0]
                            companion = results[1]
                            print('With no where else to go you cautiously enter the Dark tunnel')
                            protag = exploreDarkCave(protag, False, companion)
                        else:
                            print('You flee from the goblins the only way you can. Towards the Dark Tunnel')
                            protag = exploreDarkCave(protag,True, 0)
    else:
        print()
        return False
def prisoner_convo(protag, saved, done, map_knowledge):
    if done == False:
        print('You: What are you doing in these caves?')
    input()
    if saved == True and done == False:
        charisma_check = protag.checkCha(4)
        if charisma_check:
            map_knowledge = True
            print('Man: Alright Pal, you saved me. Normally I wouldn\'t tell you this but I guess I owe you one')
            print('This isn\'t any ordinary cave, this cave is the hiding place for a special map.')
            print('A map that is supposed to lead to immeasurable wealth, I discovered it while doing research at the University')
            print('That\'s what I do, I\'m a researcher')
            input()
            print('so I tell you what, let\'s team up, I\'m no fighter but we can back each other up, and you won\'t be able to find that map without my help')
        else:
            map_knowledge = False
            print('Man: I\'m a reseacher at the University, I found some interesting things about this place during my studies and decided to come check it out for myself')
            print('But as you can see I\'ve found myself in a bit of a predicament.')
            print('so I tell you what, let\'s team up, I\'m no fighter but we can back each other up, and maybe we can both make it out alive')
    elif saved == False:
        charisma_check = protag.checkCha(8)
        if charisma_check:
            map_knowledge = True
            print('Man: Alright Pal, Clearly I need your help. Normally I wouldn\'t tell you this but I guess I have')
            print('This isn\'t any ordinary cave, this cave is the hiding place for a special map.')
            print('A map that is supposed to lead to immeasurable wealth, I discovered it while doing research at the University')
            print('That\'s what I do, I\'m a researcher')
            input()
            print('so I tell you what, let\'s team up, I\'m no fighter but we can back each other up, and you won\'t be able to find that map without my help')
            return map_knowledge
        else:
            map_knowledge = False
            print('Man: I\'m a reseacher at the University, I found some interesting things about this place during my studies and decided to come check it out for myself')
            print('But as you can see I\'ve found myself in a bit of a predicament.')
            input()
            print('so I tell you what, let\'s team up, I\'m no fighter but we can back each other up, and maybe we can both make it out alive\n')
    elif saved == True and done == True:
        if map_knowledge == True:
            print('Now let\'s go find that map. It should be in the other chamber somewhere')
        else:
            print('Now let\'s find our way out of this place. I think It\'s through that dark chamber')
    return map_knowledge            

def exploreLightCaveGA(protag, goblins_alive, captured = False):
    if captured == False:
        print('As you enter the the large cavern at the end of the lit tunnel you see a horrifying scene')
        input()
        print('A pile of bones lays in the corner, a small fire burns in the middle, and a gallows at the far side.')
        print('But most unusual of all, a man stands in a small wooden cage, barely big enough for him to fit')
        print('As you stand dumbfounded, the man speaks, and you come to your senses')
    print('Man: well are you gonna let me out of here or what?\n')
    input()
    valid = False #ensures proper answer to question
    done = False #checks if conversation option has been chosen
    attempt = 0
    leave = 0
    map_knowledge = False
    while not valid: #continues until valid response is given
        print('What do you do??') 
        print('\n1. Try to break him out [strength]')
        if done == False: #only gives option if conversation hasn't already happened
            print('2. Ask him what he\'s doing there [charisma]')
        if leave == 0 and goblins_alive == True:
            print('3. Leave him there, the goblins will notice if he\'s gone and try to find you')
        elif leave == 0 and goblins_alive == False:
            print('3. Leave him there, you don\'t know if you can trust him')
        else:
            print('3. Change your mind and leave him')
        action = input()
        if action == '1': # runs through break open cage routine
            print('You get a running start and kick the wooden door as hard as you can')
            if captured == False:
                strength_check = protag.checkStg(4)
            else:
                strength_check = True
            if strength_check and leave ==0: #checks if other options have been chose befor this one and proceed accordingly
                input()
                print('and it gives! the door breaks from it\'s frame allowing the prisoner to step forward')
                print('Man: Thanks Pal, I really don\'t know what would have happened to me if you hadn\'t shown up')
                map_knowledge = prisoner_convo(protag, True, done, map_knowledge)
                valid = True
                companion = 1
                protag = exploreDarkCave(protag, goblins_alive, companion)
            elif strength_check and leave != 0: #checks if you have chosen option 3 before
                input()
                print('and it gives! the door breaks from it\'s frame allowing the prisoner to step forward')
                input()
                print('\nMan: Thanks Pal, I really don\'t know what would have happened to me if you hadn\'t shown up')
                print('ok, here\'s what I know, This isn\'t any ordinary cave, this cave is the hiding place for a special map.')
                input()
                print('\nA map that is supposed to lead to immeasurable wealth, I discovered it while doing research at the University')
                print('That\'s what I do, I\'m a researcher')
                input()
                print('\nso I tell you what, let\'s team up, I\'m no fighter but we can back each other up, and you won\'t be able to find that map without my help')
                input()
                companion = 1
                map_knowledge = True
                valid = True
                protag = exploreDarkCave(protag, goblins_alive, companion)
            else:
                if attempt == 0:
                    input()
                    print('and you flub feebly against the bars, hurting your leg in the process')
                    print('you take 1 damage')
                else:
                    input()
                    print('and once again you flub feebly agains\'t the bars, hurting your leg even more')
                    print('you take another 1 damage')
                protag.hlth -= 1
                if protag.hlth <= 0:
                    print('and you somehow manage to kill yourself')
                    break                    
        if action == '2' and done == False: #runs through convo routine
            if leave != 0:
                print('You: What are you doing in these caves?')
                input()
                print('Man: uh uh, no way, not until you get me out of this cage')
                input()
            else:
                map_knowledge = prisoner_convo(protag, False, False, False)
                companion = 1
                protag = exploreDarkCave(protag, goblins_alive, companion)
            done = True
        if action == '3': #runs through leaving routine
            if done == False: #checks if you have had the conversation with the prisoner
                print('You: I\'m sorry but I\'ve got to look out for myself')
                print('If the goblins come back and you\'re gone, they\'ll come looking for me')
                input()
                print('as you begin to talk away you hear the prisoner shout at you')
                print('Man: Wait! I have information you might want! let me out and I\'ll tell you')
                print('\nWhat do you do??')
                valid2 = False
                while valid2 == False: #prisoner baits you with info, 
                    action = input('1. Go back and try to get him out \n2. Still leave him\n')
                    if action == '1':
                        valid2 = True
                        leave += 1
                    if action == '2':
                        valid = True
                        valid2 = True
            elif done == True and leave ==0: #if you have had the conversation and haven't tried to leave yet, you get this option
                print('You: I\'m sorry but I\'ve got to look out for myself')
                if goblins_alive == True:
                    print('If the goblins come back and you\'re gone, they\'ll come looking for me')
                elif goblins_alive == False:
                    print('I don\'t know you, you could murder me when I let you out')
                input()
                print('as you begin to talk away you hear the prisoner shout at you')
                if map_knowledge == False: #checks to see if you have obtained the map knowledge yet, if you haven't the prisoner baits you with it
                    print('Man: Wait! I have information you might want! let me out and I\'ll tell you')
                    print('\nWhat do you do??')
                    valid2 = False
                    while valid2 == False:
                        action = input('1. Go back and try to get him out \n2. Still leave him\n')
                        if action == '1':
                            valid2 = True
                            leave += 1
                        if action == '2':
                            valid = True
                            valid2 = True
                else:
                    print('Man: You can\'t leave me! I told you everything I know! this isn\'t fair, you can\'t....')
                    print('his voice trails off as you continue to walk back towards the main chamber')
                    valid = True
                    companion = 0
            elif done == True and leave != 0: #allows you to leave if you have all the info and have already tried to leave before
                print('After some deliberation, you decide that it\'s best to just leave the man')
                companion = 0
                valid = True
    return [protag, companion]

def exploreDarkCave(protag, goblins_alive, companion, map_knowledge =  False):
    """
    a companion of 0 means the player is travelling alone, a companion of 1 means the player rescued the prisoner, a companion of 2 means the player teamed with the goblins'
    """
    if companion >0:
        while True:
            print('Who should enter the dark tunnel first?')
            print('1. You')
            if companion == 1:
                print('2. The prisoner')
            else:
                print('2. The goblins')
            order = int(input()) #determines who goes first into dark tunnel, 1 if protagonist, 2 if companions
            if order == 1 or order == 2:
                break
            else:
                print('Invalid input')
    print('You enter the dark tunnel, it is hard to see anything. You keep your hand against the wall to know where you are going, but a deep chasm runs along the left side of the path')
    encounter = randint(1,5)
    if encounter < 3: #spider encounter
        print('You\'ve been walking for a while but it\'s too dark, you can\'t see more than a few feet in front of you.')
        input()
        if companion == 1:
            print('your companion shouts to you "wow I can\'t see a thing!"')
            if order == 1:
                print('You turn back to look at him, and behind him you see two giant glowing eyes.')
                print('slowly it comes into focus, the front legs, the fangs dripping with poison.')
                input()
                while True:
                    print('What do you do??')
                    print('1. Let the spider take him')
                    print('2. Shout to warn him')
                    action = int(input())
                    if action ==1 or action ==2:
                        break
                    else:
                        print('Invalid input')
                if action == 1:
                    print('You decide to let the spider take him. Better him than you.')
                    print('"YEEEARGHHH!!" he yells and screams in pain, striking at the beast with his fist, but it has no effect. The spider drags him off')
                    input()
                    companion = 0
                else:
                    print('"Behind you!" you shout.')
                    input()
                    print('He turns and sees the foul beast, just as it lunges at him.')
                    print('You wish you could help him but there is just not enough room on the path')
                    survive = randint(1,3)
                    if survive > 1:
                        print('He grabs the spiders fangs and manages to keep them from stabbing into him')
                        input()
                        print('You notice that the spider is putting most of it\'s weight on a loose pile of rocks near the edge of the chasm')
                        input()
                        print('You pick up a rock and throw it at the pile...')
                        input()
                        print('and it hits!, the pile of rocks goes tumbling, along with the spider')
                        input()
                        if protag.checkIng(8):
                            print('[Intelligence Check Success] You realize that you should check if the spider left a line securing it, that it could use to climb back up')
                            input()
                            print('Sure enough, when you go to check there is a thick strand of spider silk attached to the chasm wall, and down below you can already see the glowing eyes climbing back to you')
                            print('\nYou grab a nearby rock and bash at the soil around the line until it gives way, and you see the eyes fall into the abyss\n')
                            input()

                    else:
                        print('"YEEEARGHHH!!" he yells and screams in pain, striking at the beast with his fist, but it has no effect. The spider drags him off')
                        input()
                        companion = 0
            else:
                print('suddenly you feel a presence behind you. You turn and see two glowing eyes, attached to two huge fangs dripping with poison')
                print('it\'s a giant spider!')
                protag = giantSpider(protag, order, companion)
                
        if companion == 2:
            print('you don\'t know how the goblins are doing it but they seem to be navigating the darkness with no problem at all')
            if order == 1:
                print('"What\'s the hold up??" you hear greg shout forward, "I thought an',protag.race,'was sposed to be all better than us goblins"')
                input()
                print('You turn back to look at him, and behind him you see two giant glowing eyes.')
                print('slowly it comes into focus, the front legs, the fangs dripping with poison.')
                input()
                print('before you can react you see the giant spider lash out, and sink its fangs deep into Greg')
                print('"YEEEARGHHH!!" he yells and screams in pain, striking at the beast with his fist, but it has no effect. The spider drags him off')
                input()
                print('you find yourself grateful the you decided to lead the pack, and just hope that greg is enough to satisfy the spider')
                input()
                companion = 3 #indicates 1 goblin remaining
            else:
                print('suddenly you feel a presence behind you. You turn and see two glowing eyes, attached to two huge fangs dripping with poison')
                print('it\'s a giant spider!')
                protag = giantSpider(protag, order, companion)

        if companion == 0:
            print('suddenly you feel a presence behind you. You turn and see two glowing eyes, attached to two huge fangs dripping with poison')
            print('it\'s a giant spider!')
            protag = giantSpider(protag, order, companion)
            
    print('after a few minutes, you approach what appears to be a rickity rope bridge over a deep chasm')
    if companion == 2:
        print('Crumble shouts, "Don\'t worry boss, we put this bridge up. Sturdy as can be"')
    if encounter == 3: #Bridge Encounter
        if companion == 0 and goblins_alive == True:
            print('As you approach the bridge, you kick the roap to test it\'s strength. It doesn\'t seem terribly sturdy. One quick hit to one of the stake holding it down might send it tumbling')
            input()
            print('Suddenly, you here a commotion behind you. "Hey! Who\'s that up ahead!"')
            print('it\'s golbins!')
            while True:
                print('What do you do??')
                print('1. Stand and fight')
                print('2. Run across the bridge')
                action = int(input())
                if action == 1 or action == 2:
                    break
                else:
                    print('Invalid input')
            if action == 1:
                results = goblin_encounter(protag, True)
                protag = results[0]
                if protag.hlth <=0:
                    sys.exit()
            else:
                print('You dash across the bridge.. somehow it manages to stay intact. But the goblins are close behind you')
                while True:
                    print('What do you do??')
                    print('1. Try to knock down the bridge [Strength]')
                    print('2. Keep running!')
                    action = int(input())
                    if action ==1 or action ==2:
                        break
                    else:
                        print('Invalid input')
                if action ==1:
                    print('As the goblins pour onto the bridge you kick one the stakes holding it as hard as you can')
                    input()
                    str_check = protag.checkStg(7)
                    if str_check:
                        print('And it gives! The goblins go tumbling into the abyss!')
                        input()
                    else:
                        print('But it\'s no good! The stake budges but doesn\'t come free!')
                        print('Before you have a chance to do anything else the goblins are on you!')
                        results = goblin_encounter(protag, True)
                        protag = results[0]
                        if protag.hlth <=0:
                            sys.exit()
        if companion == 1 and goblins_alive == True:
            print('As you approach the bridge, you kick the roap to test it\'s strength. It doesn\'t seem terribly sturdy. One quick hit to one of the stake holding it down might send it tumbling')
            input()
            print('Suddenly, you here a commotion behind you. "Hey! Who\'s that up ahead!"')
            print('it\'s golbins!')
            input()
            if order == 2:
                print('Your companion sees the goblins and shouts "Quick, run!"')
                print('As he runs across the bridge, his foot catches on a loose board, and before he can catch himself he tumbles over into the abyss')
                while True:
                    print('What do you do??')
                    print('1. Stand and fight')
                    print('2. Run across the bridge')
                    action = int(input())
                    if action == 1 or action == 2:
                        break
                    else:
                        print('Invalid input')
                if action == 1:
                    results = goblin_encounter(protag, True)
                    protag = results[0]
                    if protag.hlth <=0:
                        sys.exit()
                else:
                    print('You dash across the bridge.. somehow it manages to stay intact. But the goblins are close behind you')
                    while True:
                        print('What do you do??')
                        print('1. Try to knock down the bridge [Strength]')
                        print('2. Keep running!')
                        action = int(input())
                        if action ==1 or action ==2:
                            break
                        else:
                            print('Invalid input')
                    if action ==1:
                        print('As the goblins pour onto the bridge you kick one the stakes holding it as hard as you can')
                        input()
                        str_check = protag.checkStg(7)
                        if str_check:
                            print('And it gives! The goblins go tumbling into the abyss!')
                            input()
                        else:
                            print('But it\'s no good! The stake budges but doesn\'t come free!')
                            print('Before you have a chance to do anything else the goblins are on you!')
                            results = goblin_encounter(protag, True)
                            protag = results[0]
                            if protag.hlth <=0:
                                sys.exit()
            else:
                while True:
                    print('"What should we do??" Your companion shouts')
                    print('1. "Stand and fight!"')
                    print('2. "Stand and fight!"[Lie][Charisma]')
                    print('3. "Run!" [Speed]')
                    action = int(input())
                    if action in [1,2,3]:
                        break
                    else:
                        print('Invalid input')
                if action == 1:
                    print('"Good idea!" But as you turn around he bolts across the bridge')
                    print('But his foot catches on a loose board, and before he can catch himself he tumbles over into the abyss')
                    results = goblin_encounter(protag, True)
                    protag = results[0]
                    if protag.hlth <=0:
                        sys.exit()
                elif action == 2:
                    cha_check = protag.checkCha(6)
                    if cha_check:
                        print('"Good idea!" he shouts and turns to face the goblins')
                        print('But as he does you bolt across the bridge. He turns and looks at you with a face of betrayal as the goblins attack him')
                        print('It seems like the goblins will be occupied with him for at least a few moments.')
                        attempts = 0
                        while attempts < 3:
                            print("What do you do??")
                            print('1. Run')
                            print('2. Try to knock down the bridge [strength]')
                            action2 = int(input())
                            if action2 == 1:
                                print('You decide it\'s best to get as far away from the situation as possible and keep running down the path')
                                attempts = 3
                            elif action2 == 2:
                                print('You kick at the stake holding one of the ropes in place..')
                                input()
                                str_check = protag.checkStg(7)
                                if str_check:
                                    print('And it gives! The bridge goes tumbling into the chasm! there\'s no way for the goblins to reach you now!')
                                    input()
                                    attempts = 3
                                else:
                                    if attempts < 2:
                                        print('But it\'s no good! The stake moves but doesn\'t give. But the goblins are occupied and there might be time to try again')
                                        attempts += 1
                                    else:
                                        print('But it\'s no good! and you\'re out of time! the goblins are on you!')
                                        attempts = 3
                                        results = goblin_encounter(protag, True)
                                        protag = results[0]
                                        if protag.hlth <=0:
                                            sys.exit()
                else:
                    spd_check = protag.checkSpd(5)
                    print('"Run!" you shout, and you both bolt across the bridge')
                    input()
                    if spd_check:
                        print('and you\'re able to lose them! but they\'re sill behind you somewhere..')
                    else:
                        print('But your companion trips on a board, and goes tumbling into the abyss! Even the split second you take to turn and look is too long, and the goblins are one you!')
                        results = goblin_encounter(protag, True)
                        protag = results[0]
                        if protag.hlth <=0:
                            sys.exit()
    return protag

def safeSleep(protag, goblins_alive):
    if goblins_alive == False:
        print('With the goblins taken care of you succumb to your exhaustion, you make your way back to the chamber and have a good nights rest')
        input()
    print('The next morning you feel rested and ready to explore the cave')
    protag.htlh = 15
    valid = False
    while not valid:
        print('What would you like to do??')
        action = input('1. Explore the Light Cave\n2. Explore the Dark Cave')
        if action == '1':
            results = exploreLightCaveGA(protag, goblins_alive)
            protag = results[0]
            companion = results[1]
            valid = True
        elif action == '2':
            valid = True
            results = exploreDarkCave(protag, goblins_alive, 0)
        else:
            print('Invalid response, please enter the number of the action you would like to perform.')
    return protag

##protag = character('John', 'Orc', 18, 18, 0, 18, 15)
##print(exploreDarkCave(protag,1,1))
