
#to do: Add move pool

from mechanics import *

"""
Pallet Town to Viridian City
"""

def bedroom(player):
    while True:
        os.system(clearVar)
        print('You find yourself in your bedroom, there is a TV in the corner, a game system in front of it, and stairs that go down')
        print('what would you like to do?')
        print('1. Watch tv\n2. Play video games\n3. Go downstairs\n4. Menu')
        action = input()
        if menuValid(action, 4):
            action = int(action)
            if action == 1:
                print('It\'s a weather report! Bright and sunny all day!')
                input()
            elif action == 2:
                print('It\'s an older system, looks like a SNES. Who even has these anymore?')
                input()
            elif action == 3:
                print('You walk downstairs to the rest of the house')
                input()
                return 'momsHouse'
            else:
                if len(player.pokeList)==0:
                    print('You don\'t have any pokemon! there is no menu yet!')
                    input()
                else:
                    menu(player)

def momsHouse(player):
    while True:
        os.system(clearVar)
        print('You find yourself in the main room, your mom is brushing her pokemon on the couch, there are stairs that go up to your room')
        print('What would you like to do?')
        print('1. Talk to mom\n2. Go upstairs\n3. Leave\n4. Menu')
        action = input()
        if menuValid(action, 4):
            action = int(action)
            if action == 1:
                if len(player.pokeList) == 0:
                    print('Mom: "Today is the big day! if you find Professor Oak he will give you a pokemon!"')
                    input()
                else:
                    print('Mom: "I can\'t believe my child is all grown up and going on their own pokemon adventure!"')
                    print('"Why don\'t you take a rest for a bit?" (pokemon are healed)')
                    gameState.lastPokecenter = 'palletTown'
                    player.partyHeal()
                    input()
            elif action == 2:
                print('You walk upstairs')
                input()
                return 'bedroom'
            elif action == 3:
                return 'palletTown'
                input()
            else:
                if len(player.pokeList)==0:
                    print('You don\'t have any pokemon! there is no menu yet!')
                    input()
                else:
                    menu(player)
        os.system(clearVar)
            
def garysHouse(player):
    while True:
        os.system(clearVar)
        print('You walk into Gary\'s house and see his sister sitting at the table, and a map of the area on the wall')
        print('What would you like to do?')
        print('1. Talk to Gary\'s sister\n2. Look at the map\n3. Leave\n4. Menu')
        action = input()
        if menuValid(action, 4):
            action = int(action)
            if action == 1:
                print('Gary\'s sister: "Hiya',player.name+',', 'how have you been? Gary isn\'t home right now, he\'s looking for Grandpa"')
                input()
            elif action == 2:
                print('The big cities sure do look far away...')
                input()
            elif action == 3:
                os.system(clearVar)
                return 'palletTown'
            else:
                if len(player.pokeList)==0:
                    print('You don\'t have any pokemon! there is no menu yet!')
                    input()
                else:
                    menu(player)

def route29(player):
    wild = trainer('Wild', [], {}, 10, '','')
    pidgey1 = pokemonGenerator(pokedex.pidgey,5,[tackle,gust])
    pidgey2 = pokemonGenerator(pokedex.pidgey,3,[tackle,gust,])
    pidgey3 = pokemonGenerator(pokedex.pidgey,2,[tackle,gust])
    pidgey4 = pokemonGenerator(pokedex.pidgey,3,[tackle,gust])
    ratata1 = pokemonGenerator(pokedex.ratata,4,[tackle,tailWhip])
    ratata2 = pokemonGenerator(pokedex.ratata,3,[tackle,tailWhip])
    ratata3 = pokemonGenerator(pokedex.ratata,2,[tackle,tailWhip])
    encounters = [pidgey1, pidgey2, pidgey3, pidgey4, ratata1, ratata2, ratata3]
    chance = [True, False]
    patches = 3
    i = 1
    for patch in range(1,patches+1):
        if choice(chance):
            print ('You hear a rustle in patch',i,'a wild pokemon appears!')
            i+=1
            input()
            wildPoke = choice(encounters)
            wild.pokeList.append(wildPoke)
            os.system(clearVar)
            won = battle(player, wild)
            if won == False:
                return False
            wild.pokeList.remove(wildPoke)
            encounters.remove(wildPoke)
            input()
        else:
            print('No pokemon this time!')
            input()
    return True
    
def route29north(player):
    os.system(clearVar)
    if len(player.pokeList)==0:
        print('You decide it\'s time to start your journey, and take your first steps out into the long grass of Route 29 toward Viridian City')
        input()
        print('"Wait!" you hear a shout behind you, it\'s Professor Oak!')
        input()
        print('Professor Oak: "Don\'t go into the long grass without a pokemon of your own to defend yourself!')
        print('"Follow me to my lab, I\'ll give you a pokemon of your own!"')
        input()
        lab(player, False)
        return 'palletTown'
    else:
        print('you head out on Route 29 toward Viridian City, there are three patches of tall grass you have to pass through on your way there. You may encounter wild pokemon...')
        input()
        passed = route29(player)
        if passed:
            return 'viridianCity'
        else:
            return gameState.lastPokecenter

def route29south(player):
    os.system(clearVar)
    print('You head south on Route 29 toward Pallet Town, there are three patches of tall grass you have to pass through on your way there. You may encounter wild pokemon...')
    passed = route29(player)
    if passed:
        return 'palletTown'
    else:
        return gameState.lastPokecenter

def viridianCity(player):
    while True:
        os.system(clearVar)
        print('you find yourself in Viridian City. There is a Pokecenter here, as well as a Pokemart. Off to the side of town you see the local Pokemon Gym!')
        print('To the north there is a road that leads in to the Viridian Forest. There is also a path that heads of to the west.')
        action = menuSelect('Where would your like to go?',['Pokecenter','Pokemart','Pokemon Gym','Into the Viridian Forest','Path to the west','Head back on Route 29 toward Pallet Town','Menu'])
        if action == 1:
            gameState.lastPokecenter = 'viridianCity'
            pokeCenter(player)
        elif action == 2:
            itemShop(player)
        elif action == 3:
            print('As you approach the gym you notice that something feels off, the building looks like it hasn\'t been maintained in quite sometime')
            input()
            print('Old Man: "Looking at the old Pokemon Gym eh? Nobody has been there in quite some time,')
            print("the old gym leader left years ago, just an abandoned old building now")
            input()
        elif action == 4:
            return 'viridianArea1'
        elif action == 5:
            return 'victoryRoadApproachWest'
        elif action == 6:
            return 'route29south'
        else:
            menu(player)

def victoryRoadApproachWest(player):
    while True:
        os.system(clearVar)
        print('You start to head down the path, before long you come across a patch of tall grass.')
        print('It seems like you might encounter a few wild pokemon if you try to pass through')
        action = menuSelect('Where would your like to go?',['Continue through the grass','Go back','Menu'])
        if action == 1:
            passed = approachWild(player, 3)
            if passed == False:
                return gameState.lastPokecenter
            else:
                print('Phew, you made it through')
                action1 = menuSelect('What would you like to do?',['Continue on the path','Head back to Viridian City (go back through the grass)','Menu'])
                if action1 == 1:
                    return 'victoryRoadApproach'
                elif action1 == 2:
                    passed = approachWild(player, 3)
                    if passed == False:
                        return gameState.lastPokecenter
                    else:
                        return 'viridianCity'
                else:
                    menu(player)
        elif action == 2:
            return 'viridianCity'
        else:
            menu(player)

def victoryRoadApproach(player): #LEFT OFF HERE
    os.system(clearVar)
    if 'victoryRoad' in gameState.trainers.rival.gary.itemList:
        print('Ahead you see someone approaching you...')
        input()
        print('it\'s Gary!')
        input()
        print('Gary: "Trying to go to the Pokemon League, eh? Don\'t bother, the guard won\'t let you through,')
        print('"you probably don\'t even have any badges yet. Hey! let\'s see how much your pokemon have grown!"')
        garyPidgey = pokemonGenerator(pokedex.pidgey, 9, [gust, tackle, tailWhip])
        garyStarter = gameState.trainers.rival.gary.pokeList[0]
        garyStarter.addLevel(4)
        gameState.trainers.rival.gary.partyHeal()
        gameState.trainers.rival.gary.pokeList.append(garyPidgey)
        gameState.trainers.rival.gary.phrase1 = '"I bet you haven\'t even caught any new pokemon!"'
        gameState.trainers.rival.gary.phrase2 = '"What?! I need to find better pokemon"'
        won = trainerEncounter(player, gameState.trainers.rival.gary)
        gameState.trainers.rival.gary.itemList.remove('victoryRoad')
        if won == False:
            print('"I knew it, you don\'t have what it takes. Whatever, smell ya later',player.name+'!"')
            input()
        else:
            os.system(clearVar)
            print('"Well at least you\'ve been training, but it\'s gonna take a lot more than that if you ever want to challenge the pokemon league!"')
            print('"Smell ya later',player.name+'!')
            input()
        player.partyHeal()
    print('When you get to the gate you encounter a guard..')
    input()
    while True:
        os.system(clearVar)
        print('Guard: "Halt! I can only let you pass if you have all 8 pokemon badges from this region')
        action = menuSelect('What do you do?',['Show him you badges','Go back','Menu'])
        if action == 1:
            if 'Earth Badge' in player.badges:
                print('Guard: "Very well, you may pass')
                input()
                return 'victoryRoadArea1'
            else:
                print('Guard: Sorry, without all the badges I can\'t let you pass')
                input()
        elif action == 2:
            print('You decide to head to Viridian City, you\'ll need to pass through to tall grass to get there...')
            input()
            passed = approachWild(player, 3)
            if passed == False:
                return gameState.lastPokecenter
            else:
                return 'viridianCity'
        else:
            menu(player)

def approachWild(player, patches):
    wild = trainer('Wild', [], {}, 10, '', '')
    nidoranF1 = pokemonGenerator(pokedex.nidoranF,3,[tackle, leer])
    nidoranF2 = pokemonGenerator(pokedex.nidoranF,3,[tackle, leer])
    nidoranF3 = pokemonGenerator(pokedex.nidoranF,4,[scratch, leer])
    ratata1 = pokemonGenerator(pokedex.ratata,3,[tackle, tailWhip])
    ratata2 = pokemonGenerator(pokedex.ratata,3,[tackle, tailWhip])
    ratata3 = pokemonGenerator(pokedex.ratata,3,[tackle, tailWhip])
    nidoranM1 = pokemonGenerator(pokedex.nidoranM,4,[scratch, leer])
    pidgey1 = pokemonGenerator(pokedex.pidgey,3,[tackle, gust])
    encounters = [nidoranF1, nidoranF2, nidoranF3, ratata1, ratata2, ratata3, nidoranM1, pidgey1]
    chance = [True, False]
    i = 1
    for patch in range(1,patches+1):
        if choice(chance):
            print ('You hear a rustle in patch',i,'a wild pokemon appears!')
            i+=1
            input()
            wildPoke = choice(encounters)
            wild.pokeList.append(wildPoke)
            os.system(clearVar)
            won = battle(player, wild)
            if won == False:
                return False
            wild.pokeList.remove(wildPoke)
            encounters.remove(wildPoke)
            input()
        else:
            print('No pokemon this time!')
            input()
    return True
        
def palletTown(player):
    while True:
        os.system(clearVar)
        print('You find yourself standing in Pallet Town, the sleepy small town you grew up in')
        print('There is not much of note here besides you house, your rival Gary\'s house, and the world famous pokemon lab!')
        print('What would you like to do?')
        print('1. Go to my house\n2. Go to Gary\'s house\n3. Go to the pokemon lab\n4. Go on the north path toward Viridian City\n5. Menu')
        action = input()
        if menuValid(action, 5):
            action = int(action)
            if action == 1:
                return 'momsHouse'
            elif action == 2:
                return 'garysHouse'
            elif action == 3:
                return 'lab'
            elif action == 4:
                return 'route29north'
            else:
                if len(player.pokeList) == 0:
                    print('You don\'t have any pokemon! there is no menu yet!')
                    input()
                else:
                    menu(player)
            
def lab(player, pokeGot = True):
    os.system(clearVar)
    if pokeGot == False:
        print('As you walk into the lab you see Professor Oak\'s grandson, Gary, waiting')
        input()
        print('Gary: "Where ya been gramps? I\'ve been waiting all morning! you said you would give me a pokemon today!"')
        input()
        print('Professor Oak: "Oh? was that today? it must have slipped my mind. Before I forget, both of you take one of these pokedex\'s I made. They\'ll keep track of the different kinds of pokemon you catch!"')
        input()
        print('"But anyway you\'re both here now so it\'s time to pick out your first pokemon!"')
        print('"'+player.name, 'why don\'t you pick first?"')
        input()
        print('Gary: "Aw come on gramps that\'s so unfair!"')
        input()
        os.system(clearVar)
        print('Professor Oak: "Now now Gary, you\'ll get your turn, now which pokemon would you like',player.name+'?"')
        
        gary = gameState.trainers.rival.gary
        gary.money += 500
        squirtle = pokemonGenerator(pokedex.squirtle, 5, [tackle,tailWhip], 1.5)
        charmander = pokemonGenerator(pokedex.charmander, 5, [scratch,tailWhip], 1.5)
        bulbasaur = pokemonGenerator(pokedex.bulbasaur,5,[tackle,leer], 1.5)
        while True: #first Pokemon selection
            poke = input('\n1.Squirtle\n2.Charmander\n3.Bulbasaur\n')
            if menuValid(poke, 3):
                poke = int(poke)
                break
        if poke == 1:
            print('Great choice! Squirtle is a great defensive pokemon, cute too!')
            input()
            player.addPoke(squirtle)
            gary.pokeList = [bulbasaur]
            
        elif poke == 2:
            print('Great choice! Charmander is a fiery attacker! loves to play fetch too!')
            input()
            player.addPoke(charmander)
            gary.pokeList = [squirtle]
            
        else:
            print('Great choice! Bulbasaur is a sturdy blocker! loves to bask in the sun!')
            input()
            player.addPoke(bulbasaur)
            gary.pokeList = [charmander]
                
        os.system(clearVar)
        player.pokeList[0].gainedXP = 100
        print('Gary: Fine, then I\'ll take',str(gary.pokeList[0].name)+'!')
        input()
        print('You turn to leave the lab, but suddenly you feel Gary grab your arm')
        input()
        print('Gary: Where are you going',str(player.name)+'? Dontcha wanna have your first battle?') #gary initiates first battle

        while True:
            print('1. YES!')
            print('2. No!')
            react = input()
            if menuValid(react, 2):
                react = int(react)
                break
        if react == 1:
            print('Gary: Alright! that\'s the spirit!, don\'t worry I won\'t gloat too much when I beat you!')
            input()
            
        elif react == 2:
            print('Gary: Too bad!')
            print('Before you have time to react Gary throws his pokeball and gets ready to battle')
            input()
            
        os.system(clearVar)
        won = battle(player, gary, False) #starts the battle
        os.system(clearVar)
        player.pokeList[0].HP = player.pokeList[0].maxHP
        if won == True:
            print('Gary: Aw shucks, you were just lucky this time! I\'m off to battle some real trainers, smell ya later!')
            input()
        else:
            print('Gary: Haha I knew it! you don\'t have what it takes! I\'m off to battle some real trainers, smell ya later!')
            input()
        print('And with that, Gary walks out the door, after a while you decide to do the same')
        input()
    else:
        if len(player.pokeList)==0:
            while True:
                print('As you enter the lab you see a couple scientists you\'ve seen around town but there\'s no sign of Professor Oak')
                print('What would you like to do?')
                print('1. Talk to one of the scientists\n2. Leave\n3. Menu')
                action = input()
                if menuValid(action, 3):
                    action = int(action)
                    if action == 1:
                        print('Scientist: "Well hello there',player.name+'!',' Looking for Professor Oak? We haven\'t seen him all morning."')
                        input()
                    elif action == 2:
                        return 'palletTown'
                    else:
                        print('You don\'t have any pokemon! there is no menu yet!')
                        input()
                os.system(clearVar)
                
        else:
            while True:
                os.system(clearVar)
                print('You enter Professor Oak\'s pokemon lab!')
                print('What would you like to do?')
                print('1. Talk to Professor Oak\n2. Talk to one of the scientists\n3. Leave\n4. Menu')
                action = input()
                if menuValid(action, 4):
                    action = int(action)
                    if action == 1:
                        print('Professor Oak: "Oh hello',player.name+'! How is the pokedex coming along?"')
                        input()
                        print('Professor Oak: "Let\'s see....', len(player.playerDex),'pokemon caught, keep it up!"')
                        input()
                    elif action == 2:
                        print('Scientist: "Phew, we work really hard around here, Professor Oak never gives us a break!"')
                        input()
                    elif action == 3:
                        return 'palletTown'
                    else:
                        menu(player)
        
"""
Viridian Forest
"""

def viridianWild(player, patches):
    wild = trainer('Wild', [], {}, 10, '', '')
    caterpie1 = pokemonGenerator(pokedex.caterpie,3,[tackle, stringShot])
    caterpie2 = pokemonGenerator(pokedex.caterpie,3,[tackle, stringShot])
    caterpie3 = pokemonGenerator(pokedex.caterpie,4,[tackle, stringShot])
    caterpie4 = pokemonGenerator(pokedex.caterpie,2,[tackle, stringShot])
    weedle1 = pokemonGenerator(pokedex.weedle,3,[poisonSting, stringShot])
    weedle2 = pokemonGenerator(pokedex.weedle,2,[poisonSting, stringShot])
    weedle3 = pokemonGenerator(pokedex.weedle,4,[poisonSting, stringShot])
    kakuna1 = pokemonGenerator(pokedex.kakuna,5,[tackle, harden])
    pikachu1 = pokemonGenerator(pokedex.pikachu,4,[tackle, tailWhip])
    encounters = [caterpie1, caterpie2, caterpie3, caterpie4, weedle1, weedle2, weedle3, kakuna1, pikachu1]
    chance = [True, False]
    i = 1
    for patch in range(1,patches+1):
        if choice(chance):
            print ('You hear a rustle in patch',i,'a wild pokemon appears!')
            i+=1
            input()
            wildPoke = choice(encounters)
            wild.pokeList.append(wildPoke)
            os.system(clearVar)
            won = battle(player, wild)
            if won == False:
                return False
            wild.pokeList.remove(wildPoke)
            encounters.remove(wildPoke)
            input()
        else:
            print('No pokemon this time!')
            input()
    return True

def viridianArea1(player):
    while True:
        os.system(clearVar)
        print('AREA 1')
        print('You find yourself at the entrance of the Veridian Forest, it\'s dark, and kinda scary') 
        print('you see a man who looks like he\'s itching for a fight, as well as a patch of tall grass')
        print('to the north you see the path continue into the forest')
        action = menuSelect('What do you want to do?',['Talk to man','Enter the grass','Continue into the forest (AREA 2)','Go back to Veridian City','Menu'])
        if action == 1: 
            won = trainerEncounter(player,gameState.trainers.viridianTrainers.bugCatcherDoug)
            if won == False:
                return gameState.lastPokecenter
        elif action == 2:
            print('You enter the tall grass...')
            input()
            passed = viridianWild(player, 1)
            if passed == False:
                return gameState.lastPokecenter
        elif action == 3:
            return 'viridianArea2north'
        elif action == 4:
            return 'viridianCity'
        else:
            menu(player)
            
def viridianArea2north(player):
    while True:
        os.system(clearVar)
        print('AREA 2')
        print('Moving north up the path you see two what seem to be two trainers on either side of the path,')
        print('one is wearing shorts, the other has a bug net.')
        print('It looks like you can\'t get by without fighting one, but you won\'t have to fight both')
        print('Either way, you\'ll have to pass through some tall grass to get to them')
        action = menuSelect('What would you like to do?',['Fight the one in shorts (AREA 3)','Fight the one with the net (AREA 3)','Go back (AREA 1)','Menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            print('you start to move through the tall grass...')
            input()
            passed = viridianWild(player, 1)
            if passed == False:
                return gameState.lastPokecenter
            won = trainerEncounter(player, gameState.trainers.viridianTrainers.youngsterJoey)
            if won == False:
                return gameState.lastPokecenter
            else:
                return 'viridianArea3'
        elif action == 2:
            print('you start to move through the tall grass...')
            input()
            passed = viridianWild(player, 1)
            if passed == False:
                return gameState.lastPokecenter
            won = trainerEncounter(player, gameState.trainers.viridianTrainers.bugCatcherLouis)
            if won == False:
                return gameState.lastPokecenter
            else:
                return 'viridianArea3'
                                   
        elif action == 3:
            return 'viridianArea1'
        else:
            menu(player)

def viridianArea2south(player):
    while True:
        os.system(clearVar)
        print('AREA 2')
        print('Moving south down the path you see two what seem to be two trainers on either side of the path,')
        print('one is wearing shorts, the other has a bug net.')
        print('It looks like you can\'t get by without fighting one, but you won\'t have to fight both')
        print('Either way, you\'ll have to pass through some tall grass to get to them')
        action = menuSelect('What would you like to do?',['Fight the one in shorts (AREA 1)','Fight the one with the net (AREA 1)','Go back (AREA 3)','Menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            print('you start to move through the tall grass...')
            input()
            passed = viridianWild(player, 1)
            if passed == False:
                return gameState.lastPokecenter
            won = trainerEncounter(player, gameState.trainers.viridianTrainers.youngsterJoey)
            if won == False:
                return gameState.lastPokecenter
            else:
                return 'viridianArea1'
        elif action == 2:
            print('you start to move through the tall grass...')
            input()
            passed = viridianWild(player, 1)
            if passed == False:
                return gameState.lastPokecenter
            won = trainerEncounter(player, gameState.trainers.viridianTrainers.bugCatcherLouis)
            if won == False:
                return gameState.lastPokecenter
            else:
                return 'viridianArea1'
                                   
        elif action == 3:
            return 'viridianArea3'
        else:
            menu(player)

def viridianArea3(player):
    while True:
        os.system(clearVar)
        print('AREA 3')
        print('You find yourself standing in a small clearing in the forest')
        print('Across the clearing you see a girl, to the west you see a small opening in the trees,')
        print('to the south you see the path towards Virdian City, to the north you see the path toward Pewter City')
        action = menuSelect('What would you like to do?',['Talk to the girl','Go into the opening','Go down the south path','Go down the north path','Menu'])
        if action == 1:
            won = trainerEncounter(player, gameState.trainers.viridianTrainers.youngsterLiz)
            if won == False:
                return gameState.lastPokecenter
        elif action == 2:
            print('you enter into the opening')
            input()
            print('It\'s filled with wild pokemon! you may have to fight your way out!')
            passed = viridianWild(player, 3)
            if passed == False:
                return gameState.lastPokecenter
            return 'viridianArea3'
                                   
        elif action == 3:
            return 'viridianArea2south'
        elif action == 4:
            return 'viridianArea4north'
        else:
            menu(player)

def viridianArea4north(player):
    while True:
        os.system(clearVar)
        print('AREA 4')
        print('There is a long dark path ahead of you, filled with tall grass.')
        print('down th way there is a girl blocking the whole path, if she wants to battle there\'s no way to avoid her')
        action = menuSelect('What would you like to do?',['Go down the path','Go back','Menu'])
        if action == 1:
            passed = viridianWild(player, 1)
            if passed == False:
                return gameState.lastPokecenter
            won = trainerEncounter(player, gameState.trainers.viridianTrainers.bugCatcherKim)
            if won == False:
                return gameState.lastPokecenter
            passed = viridianWild(player, 2)
            if passed == False:
                return gameState.lastPokecenter
            return 'pewterCity'
        
        elif action == 2:
            return 'viridianArea3'
        else:
            menu(player)

def viridianArea4south(player):
    while True:
        os.system(clearVar)
        print('AREA 4')
        print('There is a long dark path ahead of you, filled with tall grass.')
        print('down th way there is a girl blocking the whole path, if she wants to battle there\'s no way to avoid her')
        action = menuSelect('What would you like to do?',['Go down the path','Go back','Menu'])
        if action == 1:
            passed = viridianWild(player, 1)
            if passed == False:
                return gameState.lastPokecenter
            won = trainerEncounter(player, gameState.trainers.viridianTrainers.bugCatcherKim)
            if won == False:
                return gameState.lastPokecenter
            passed = viridianWild(player, 2)
            if passed == False:
                return gameState.lastPokecenter
            return 'viridianArea3'
        
        elif action == 2:
            return 'pewterCity'
        else:
            menu(player)

"""
Pewter City
"""

def pewterCity(player):
    while True:
        os.system(clearVar)
        print('Pewter City! home to Brock\'s famous Rock Type Gym. If you think you\'re strong enough, maybe you can challenge him!')
        print('In this town there is a Pokecenter, a Pokemart, and a Museum!')
        print('To the south there is a road that leads in to the Viridian Forest, and to the east there is a path that leads to Mt. Moon.')
        action = menuSelect('Where would you like to go?',['Pokecenter','Pokemart','Pokemon Gym','Museum','Toward Mt.Moon','Into the Viridian Forest','Menu'])
        if action == 1:
            gameState.lastPokecenter = 'pewterCity'
            pokeCenter(player)
        elif action == 2:
            itemShop(player)
        elif action == 3:
            return 'rockGym'
        elif action == 4:
            return 'museumFirst'
        elif action == 5:
            if 'Boulder Badge' not in player.badges:
                print('You are stopped by a trainer at the start of the path...')
                input()
                print('Trainer: "Hold up there, pal. I can\'t help but notice you don\'t have a Boulder Badge,')
                print('"The path up ahead is dangerous, I can\'t let you go on unless I see you can handle yourself"')
                input()
                print('Trainer: "Go get the Boulder Badge from Brock and I\'ll let you through"')
                input()
            else:
                return 'MTMoon1east'
        elif action == 6:
            return 'viridianArea4south'
        else:
            menu(player)

def museumFirst(player):
    print('You walk into the museum. At the entrance there is a ticket booth.')
    action1 = menuSelect('Employee: "Hello there! Would you like to enter the museum? it\'s $50 for a childs ticket"', ['Yes','Maybe Later'])
    if action1 == 1:
        testMoney = player.money - 50
        if testMoney <0:
            print('You don\'t have enough money! You\'ll have to come back another time')
            input()
            return 'pewterCity'
        else:
            player.money -= 50
    else:
        print('You decide to come back another time')
        input()
        return 'pewterCity'
    while True:
        os.system(clearVar)
        print('The museum sure is big! on this level you see exhibits of moon rocks and a spaceship.')
        print('There is also a staircase that leads up to the second floor.')
        action = menuSelect('What would you like to do?',['Check out the moon rocks','Check out the spaceship','Go upstairs','Leave','Menu'])
        if action == 1:
            print('These stones were brought back by the astronauts when they went to the moon!')
            print('Some pokemon will evolve if you bring a moon stone close to them')
            input()
        elif action == 2:
            print('it\'s a model the space shuttle Endeavor! it\'s not in service anymore..')
            input()
        elif action == 3:
            while True:
                os.system(clearVar)
                print('upstairs you see two fossil exhibits, and a man looking into one of the cases')
                action2 = menuSelect('What would you like to do?',['Look at the first exhibit','Look at the second exhibit','Talk to the man','Go downstairs','Menu'])
                if action2 == 1:
                    print('It\'s a fossil of Omanyte, an extinct pokemon!')
                    print('There\'s an artists recreation of what they think it looked like')
                    input()
                    print("""                                                                                                    
                                                                    `.:+oyhhhhhhhhhhyyso+:.                 
                                                               .:oyhyo+/-.``         ``.:/oyy+-             
                                                           `:oys+:.                         `:sho`          
                                                        `/ss/.`                                `/h/         
                                                      -ss/``..----------.....``                  `oy.       
                                                    :yy::---.`````````.-----:://///::-`            :h.      
                                                  -yo-`                            ```-:::.         :d.     
                                                `os.                                     `-/-        +h     
                                               .y/                                          ./.       y+    
                                              :y.    `......```                               /-      .m`   
                                              +y---:::---...-------------..`                    +.      d+   
                                            os:``                     ````.-----..`            `s     .od   
                                          oo`                                 ```.--..         o     /.N.  
                                         +s`                                        ``:-.      +   `:` m-  
                                        :y`                                            `.:.  `-+----`  d:  
                                        .h.                                                -/--`  +`    d:  
                                      `y/       ````````                                  `+`    :`    m-  
                                       +s`..-::--...........--------.....`                `:`     -.    m`  
                                      `d/.``                        `````.----...        ./       .- `./m   
                                      ++                                      ``.-:-.   `/        ./..`/h   
                                     `h`                                           `.:-`+`   -:-  ..   so   
                                     /+                                               `o-   .. /  :`   d/   
                                     h`                                               .+   .-  /  /   `m.   
                                   -s     ```.....`````                              +`   :   /  +```+h    
                                   o:.-----.....``....------.......``               -/   :`   / `/```d/    
                                 `d:.`                      `````...------...`     +`   : `.:` /`  -d`    
                           `.-:/o:++                                       ``..-:.` s    : `:. ./`  so     
                        .:++/:-oo`d.                                             .--s   `:    `:.-:-m`     
                      -oo:`   /s`+o                                                -s    /   .:   `ho      
                    .oo.     .h`+o`                                                `y    --.::`   -h`      
                  :y-       y:oo`                                                  h`    /::`.- .h-       
                  /y.       `ds/    .-:+//::::-.`              ..-:::::/-..`        o+   :` /  `:y+        
                 :h`        `m/   -+/o+-`.-::-..--`         `:+:-.```.-/oo-:/-`     `h.`-`  /  `ho         
                 `h-          y   +/`/. .sdNNmN+/..+`      ./y/  .+syy+:` /o``-+-     -y.    : `yo          
                :h           :/ `h ./ `hNNmmmNddy :s-```./::o  +mmmNNyhh` /+   :/`    -o`  -..y/           
                +y            //`y::- .mNNNNmmmms //.-::-` o. -mNmmmNNmm-  y    `+.    .o.`:/s-            
                :d             -+oy++``ymmmmmmmh.`o`       o` .mmNNNNmmm`  s    `-+.    `syo/              
                  h/              .-.`/:.:+oss+:.-:`        ::  +dmmNNmh:  :-     --+     `y+               
                 .h+`                 `---.----.`           /-` .:///-` ./:       /s.     -m`              
                  .os-`                                      .::-````.:/:`         ++     .N`              
                    `/o/.`                                      `.----.             :+`   oy               
                    `.os--.`                                                        `//`+y`               
                 `-/++/.    `-`                                     :             .`   .+h:`               
                  :y/-....-:/.       .      .                       :.             .:     `:++-``           
                    .-:/oy+.       .-`     .:         .        `.  ::              +//.      `:+so-`        
                     .so:`    ``.-/.      ./         .y.        .//-              +: `:/-`       .+s+`      
                    `:/://:/+sho-       :/        .+o-s-   ``-/o/`             `o/     .:::.`````.:d/      
                          `yy:`       .+-      `/so. ./hooooo/-              `:h/``       `/dsooo+/-.`     
                           .+o+++///+yo` `.-:+oo:`   h+.``                `-+o::ddysoo++++oo:.```````      
                                    sy+++o+:-`       `+o/-`          ``-+syo-```.sy``````                  
                                                        .:+++++++ossoo+sy:+osssso/`                        
                                                                 `:/+++:`                                  
        """ )
                    input()
                elif action2 == 2:
                    print('it\'s a fossil of kabuto, an extinct pokemon!')
                    print('There\'s an artists recreation of what they think it looked like')
                    input()
                    print("""                                                                                                    
                                               `--:----------------.`                                        
                                      `-------.`                  -+++::-.                                  
                                 `-----`                         .:   -:-.:---                              
                             .:::-                                --.`  `o   `---.                          
                         `:/o-                                       .---`       `-:-`                      
                    `:/:``/-                                                      `-:-`                   
                   -o+..--:`                                                          `:-.                 
                 :/-`...`                                                                -:.               
                -/.                                                                         -/`             
              ./.                                                                           .+::            
             /:`                  :                                                          :-.:`          
           `/-                    :`                     .:oyhdyyo/-`                         +` --         
           `+`        -+ydh+-`      /                 `-odNMMMMMMMMMNmh+.                      `+  ./`      
          +`      .+hNMMMMMNdo-`   `-.            .:sdNMMMMMMMMMMMMMMMMmy-                     -:  `/`      
         /.     .sNMMMMMMMMMMMNdy+-.``.      `.:ohmMMMMMMMMMMMMMMMMMMMMMMNy.                    o   `/`     
         s     /mMMMMMMMMMMMMMMMMMNmmdhysssyhmNMMMMMMNmNNMMMMMMMMMMMMMMMMMMm:                   ::    /`    
         h    +.dMMMMMMMMMMMmdddmMMMMMMMMMMMMMMMMMms:..../sNMMMMMMMMMMMMMMMMNo`                  :-   `/    
         s    + yMMMMMMMMNs-`` `./hMMMMMMMMMMMMMMy`        .hMMMMMMMMMMMMMMMMMh:`                 ./.  ./   
         o    / +MMMMMMMM/        `yMMMMMMMMMMMMm`          .MMMMMMMMMMMMMMMMMMNdo:`                -:` o`  
         /`   ` .NMMMMMMN          :MMMMMMMMMMMMd           `NMMMMMMMMMMMMMMMMMMMMMmh+:.             `/-.+  
         `/`     +MMMMMMM/        `yMMMMMMMMMMMMM+         `sMMMMMMMMMMMMMMMMMMMMMMMMMMmy/.`           -/y` 
          `:-`    sMMMMMMNs-`` `.:hMMMMMMMMMMMMMMMy:.` ``./dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd+.          `:/ 
            .:-``  sMMMMMMMMmdhdmMMMMMMMMMMMMMMMMMMMNdhddNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNs.          s 
               `.:-`-yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhsooosdMMMMMMMMMN/         o 
                `+/- -hNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNs:`      `NMMMNNMMMMMo        +`
               .+.     -smMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy.          dd+:--yMMmyy+       o 
              -+         ./yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd            o`     +d`  .:      o 
              s             +shNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+            :-      +    --    `+ 
              o            /:.+-/ymNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/             +      ./    -`   +` 
              +`           + ./    -+hmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd             o       -+.` :`  ::  
              `+           `+o`   `   `yoohmNMMMMMMMMMMMMMMMMMMMMMMMMMMMNm:            o        o.-:s``-/   
               -:         `-::---.-/.-+:`-/:/:so++ooooo++osdhhmNNNNmdhs+-+.           /-      `/`   `..     
                ./.              `::   ....  .+--.----.----    ````    `+-          `/.      ::             
                  -:-`         .::`         .+                :/.-------           :/      -/`              
                     ---::.`.::/:.        `::                 `+-                ::`     -:.                
                         .--`    `--.------                     -::.          -:-.--.----`                  
                                                                   .---.------                                  
        """ )
                    input()
                elif action2 == 3:
                    print('Old Man: "I remember the moon landing. Bought a brand new color TV to watch it on. No one told me it would be in black and white..."')
                    input()
                    print('"you know, I heard you can find all kinds of fossils like these in Mt. Moon!')
                    input()
                elif action2 == 4:
                    break
                else:
                    menu(player)

        elif action == 4:
            print('You\'ve seen enough for today')
            input()
            return 'pewterCity'
        else:
            menu(player)


def rockGym(player):
    print('You enter the Rock Gym, it\'s dark, you can hardly see a thing.')
    input()
    while True:
        os.system(clearVar)
        print('Ahead you see another trainer, they could be looking for a fight, but you could probably sneak past')
        print('past them you can see Brock, he seems to be just waiting for a challenger')
        action = menuSelect('What would you like to do?',['Fight the trainer','Sneak past and go to brock','Leave','Menu'])
        if action == 1:
            won = trainerEncounter(player, gameState.trainers.pewterTrainers.juniorTrainerRodney)
            if won == False:
                return gameState.lastPokecenter
        elif action == 2:
            won = trainerEncounter(player, gameState.trainers.pewterTrainers.brock)
            if won == False:
                return gameState.lastPokecenter
            if 'Boulder Badge' not in player.badges:
                player.badges.append('Boulder Badge')
                print('With that, you head back to Pewter City')
                input()
                return 'pewterCity'
        elif action == 3:
            return 'pewterCity'
        else:
            menu(player)

"""
Mt. Moon
"""

def MTMoonWild(player, patches):
    wild = trainer('Wild', [], {}, 10, '', '')
    spearow1 = pokemonGenerator(pokedex.spearow,7,[peck])
    spearow2 = pokemonGenerator(pokedex.spearow,5,[peck])
    pidgey1 = pokemonGenerator(pokedex.pidgey,6,[gust, tackle])
    ratata1 = pokemonGenerator(pokedex.ratata,5,[tackle, quickAttack, tailWhip])
    jigglypuff1 = pokemonGenerator(pokedex.jigglypuff,6,[pound, sing])
    sandshrew1 = pokemonGenerator(pokedex.sandshrew,7,[scratch, tailWhip])
    ratata2 = pokemonGenerator(pokedex.ratata,4,[tackle, tailWhip])
    pidgey2 = pokemonGenerator(pokedex.pidgey,7,[tackle, gust])
    caterpie1 = pokemonGenerator(pokedex.caterpie,4,[tackle, stringShot])
    encounters = [spearow1, spearow2, pidgey1, ratata1, jigglypuff1, sandshrew1, ratata2, pidgey2, caterpie1]
    chance = [True, False, True, True]
    i = 1
    for patch in range(1,patches+1):
        if choice(chance):
            print ('You hear a rustle in patch',i,'a wild pokemon appears!')
            i+=1
            input()
            wildPoke = choice(encounters)
            wild.pokeList.append(wildPoke)
            os.system(clearVar)
            won = battle(player, wild)
            if won == False:
                return False
            wild.pokeList.remove(wildPoke)
            encounters.remove(wildPoke)
            input()
        else:
            print('No pokemon this time!')
            input()
    return True

def MTMoon1east(player):
    JTEleanor = gameState.trainers.MTMoonTrailTrainers.juniorTrainerEleanor
    lassBetty = gameState.trainers.MTMoonTrailTrainers.lassBetty
    youngsterJim = gameState.trainers.MTMoonTrailTrainers.youngsterJim
    BCMatt = gameState.trainers.MTMoonTrailTrainers.bugCatcherMatt
    trainers = [JTEleanor, lassBetty, youngsterJim, BCMatt]
    while True:
        os.system(clearVar)
        print('You look out on the start of the path from Pewter City to Mt. Moon')
        print('It looks like there are lots of trainers making their way towards the mountain, some are probably looking to battle')
        print('You could try to avoid them, or you could search them out on your way to the mountain')
        action = menuSelect('What would you like to do?',['Try to avoid them','Search them out','Go back to Pewter city','Menu'])    
        if action == 1 or action == 2:
            print('You start making your way out onto the path...')
            input()
            if action == 1:
                avoid = [0,1,1,2,2]
            elif action == 2:
                avoid = [1,2,2,3,3]
            encounters = choice(avoid)
            for i in range(encounters):
                os.system(clearVar)
                opponent = choice(trainers)
                print('But a trainer spotted you!')
                print('It\'s', opponent.name+'!')
                won = trainerEncounter(player, opponent)
                if won == False:
                    return gameState.lastPokecenter
                trainers.remove(opponent)
                goBack = menuSelect('Phew, would you like to keep going or turn back to Pewter city?',['Keep going','Turn back'])
                if goBack == 2:
                    return 'pewterCity'
            print('You made it through the first part of the path!')
            input()
            return 'MTMoon2east'
        elif action == 3:
            return 'pewterCity'
        else:
            menu(player)

def MTMoon1west(player):
    JTEleanor = gameState.trainers.MTMoonTrailTrainers.juniorTrainerEleanor
    lassBetty = gameState.trainers.MTMoonTrailTrainers.lassBetty
    youngsterJim = gameState.trainers.MTMoonTrailTrainers.youngsterJim
    BCMatt = gameState.trainers.MTMoonTrailTrainers.bugCatcherMatt
    trainers = [JTEleanor, lassBetty, youngsterJim, BCMatt]
    while True:
        os.system(clearVar)
        print('You look out on the start of the path from Pewter City to Mt. Moon')
        print('It looks like there are lots of trainers making their way towards the mountain, some are probably looking to battle')
        print('You could try to avoid them, or you could search them out on your way to Pewter City')
        action = menuSelect('What would you like to do?',['Try to avoid them','Search them out','Go back to the other part of the path','Menu'])    
        if action == 1 or action == 2:
            print('You start making your way out onto the path...')
            input()
            if action == 1:
                avoid = [0,1,1,2,2]
            elif action == 2:
                avoid = [1,2,2,3,3]
            encounters = choice(avoid)
            for i in range(encounters):
                os.system(clearVar)
                opponent = choice(trainers)
                print('But a trainer spotted you!')
                print('It\'s', opponent.name+'!')
                won = trainerEncounter(player, opponent)
                if won == False:
                    return gameState.lastPokecenter
                trainers.remove(opponent)
                goBack = menuSelect('Phew, would you like to keep going or turn back to the other part of the path?',['Keep going','Turn back'])
                if goBack == 2:
                    return 'MTMoon2east'
            print('You made it back to Pewter City!')
            input()
            return 'pewterCity'
        elif action == 3:
            return 'MTMoon2east'
        else:
            menu(player)

def MTMoon2east(player):
    JTJane = gameState.trainers.MTMoonTrailTrainers.juniorTrainerJane
    youngsterNeil = gameState.trainers.MTMoonTrailTrainers.youngsterNeil
    while True:
        os.system(clearVar)
        print('You are standing at the top of a large hill, to your right you see a ledge.')
        print('It looks like it leads to a path that heads straight back to Pewter City.')
        print()
        print('Ahead you see the path to the entrance to the Mt.Moon tunnel.')
        print('Along the way you see two patches of grass and two trainers,')
        print('It looks like like you could avoid the trainers by moving through the patches of grass.')
        action = menuSelect('What would you like to do?',\
                            ['Jump down the ledge and head back to Pewter city','Go around the first trainer in the grass','Fight the first trainer','Go into the grass looking for wild pokemon','Go on the first part of the path toward Pewter City','Menu'])    
        if action == 1:
            print('You jump down the ledge')
            input()
            print('A trainer at the base of the ledge spots you!')
            won = trainerEncounter(player, youngsterNeil)
            if won == False:
                return gameState.lastPokecenter
            return 'pewterCity'
        elif action == 2 or action == 3:
            if action == 2:
                passed = MTMoonWild(player, 1)
                if passed == False:
                    return gameState.lastPokecenter
            elif action == 3:
                passed = trainerEncounter(player, JTJane)
                if passed == False:
                    return gameState.lastPokecenter
            return 'MTMoon3east'
        elif action == 4:
            passed = MTMoonWild(player, 1)
            if passed == False:
                return gameState.lastPokecenter
            
        elif action == 5:
            return 'MTMoon1west'
        else:
            menu(player)

def MTMoon2west(player):
    JTJane = gameState.trainers.MTMoonTrailTrainers.juniorTrainerJane
    while True:
        os.system(clearVar)
        print('You look up at a tall hill.')
        print('Along the way you see a patch of grass and a trainer')
        print('It looks like like you could avoid the trainer by moving through the patch of grass.')
        action = menuSelect('What would you like to do?',\
                            ['Go around the trainer in the grass','Fight the trainer','Go into the grass looking for wild pokemon','Go back the way you came','Menu'])    

        if action == 1 or action == 2:
            if action == 1:
                passed = MTMoonWild(player, 1)
                if passed == False:
                    return gameState.lastPokecenter
            elif action == 2:
                passed = trainerEncounter(player, JTJane)
                if passed == False:
                    return gamState.lastPokecenter
            return 'MTMoon2east'
        elif action == 3:
            passed = MTMoonWild(player, 1)
            if passed == False:
                return gameState.lastPokecenter
        elif action == 4:
            return 'MTMoon3east'
        else:
            menu(player)

def MTMoon3east(player):
    JTTim = gameState.trainers.MTMoonTrailTrainers.juniorTrainerTim
    lassMyriam = gameState.trainers.MTMoonTrailTrainers.lassMyriam
    while True:
        os.system(clearVar)
        print('Ahead you see the second trainer')
        print('It looks like like you could avoid the trainer by moving through the patches of grass.')
        action = menuSelect('What would you like to do?',\
                            ['Go around the second trainer in the grass','Fight the second trainer','Go into the grass looking for wild pokemon','Go back the way you came','Menu'])    
        if action == 1 or action == 2:
            if action == 1:
                passed = MTMoonWild(player, 1)
                if passed == False:
                    return gameState.lastPokecenter
            elif action == 2:
                passed = trainerEncounter(player, lassMyriam)
                if passed == False:
                    return gameState.lastPokecenter
            if len(JTTim.pokeList)>0:
                print('phew, you think you\'ve made it...')
                input()
                print('voice: "Ha! gotcha!"')
                input()
                passed = trainerEncounter(player, JTTim)
                if passed == False:
                    return gameState.lastPokecenter
            return 'MTMoonEntrance'
        elif action == 3:
            passed = MTMoonWild(player, 1)
            if passed == False:
                return gameState.lastPokecenter
            
        elif action == 4:
            return 'MTMoon2west'
        else:
            menu(player)

def MTMoon3west(player):
    lassMyriam = gameState.trainers.MTMoonTrailTrainers.lassMyriam
    while True:
        os.system(clearVar)
        print('Ahead you see the second trainer')
        print('It looks like like you could avoid the trainer by moving through the patches of grass.')
        action = menuSelect('What would you like to do?',\
                            ['Go around the second trainer in the grass','Fight the second trainer','Go into the grass looking for wild pokemon','Go back the way you came','Menu'])    
        if action == 1 or action == 2:
            if action == 1:
                passed = MTMoonWild(player, 1)
                if passed == False:
                    return gameState.lastPokecenter
            elif action == 2:
                passed = trainerEncounter(player, lassMyriam)
                if passed == False:
                    return gameState.lastPokecenter

            return 'MTMoon2west'
        elif action == 3:
            passed = MTMoonWild(player, 1)
            if passed == False:
                return gameState.lastPokecenter
            
        elif action == 5:
            return 'MTMoonEntrance'
        else:
            menu(player)

def MTMoonEntrance(player):
    while True:
        os.system(clearVar)
        print('You find yourself standing at the entrance of Mt. Moon. The mountain is large and imposing, with a well maintained tunnel carved into it\'s base')
        print('There is a girl sitting on a boulder catching her breath, there is also a pokecenter, the tunnel into the mountain, and the trail to Pewter City')
        action = menuSelect('What would you like to do?',\
                            ['Talk to the girl','Pokecenter','Go into Mt. Moon','Trail to Pewter City','Menu'])    
        if action == 1:
            print('Girl: Phew! What a hike huh? I tripped on a geodude on my way up. The thing nearly killed me!"')
            input()
        elif action == 2:
            gameState.lastPokecenter = 'MTMoonEntrance'
            pokeCenter(player)
        elif action == 3:
            print('You step into the tunnel leading through Mt. Moon...')
            input()
            return 'MTMoonArea1'
            
        elif action == 4:
            return 'MTMoon3west'
        else:
            menu(player)

def MTMoonCaveWild(player):
    wild = trainer('Wild', [], {}, 10, '', '')
    zubat1 = pokemonGenerator(pokedex.zubat,7,[leechLife])
    zubat2 = pokemonGenerator(pokedex.zubat,11,[leechLife, supersonic])
    zubat3 = pokemonGenerator(pokedex.zubat,8,[leechLife])
    zubat4 = pokemonGenerator(pokedex.zubat,9,[leechLife])
    zubat5 = pokemonGenerator(pokedex.zubat,6,[leechLife])
    geodude1 = pokemonGenerator(pokedex.geodude,11,[tackle, defenseCurl])
    geodude2 = pokemonGenerator(pokedex.geodude,13,[tackle, defenseCurl])
    geodude3 = pokemonGenerator(pokedex.geodude,9,[tackle, defenseCurl])
    paras1 = pokemonGenerator(pokedex.paras,10,[scratch])
    clefairy1 = pokemonGenerator(pokedex.clefairy,8,[pound])
    encounters = [zubat1, zubat2, zubat3, zubat4, zubat5, geodude1, geodude2, geodude3, paras1, clefairy1]
    chance = [True, False]
    if choice(chance):
        print ('a wild pokemon appears!')
        input()
        wildPoke = choice(encounters)
        wild.pokeList.append(wildPoke)
        os.system(clearVar)
        won = battle(player, wild)
        if won == False:
            return False
        wild.pokeList.remove(wildPoke)
        encounters.remove(wildPoke)
        input()
    return True
    
def MTMoonArea1(player):
    hikerNorton = gameState.trainers.MTMoonTrainers.hikerNorton
    lassDoris = gameState.trainers.MTMoonTrainers.lassDoris
    while True:
        os.system(clearVar)
        print('(Mt. Moon Area 1)')
        print('(this cave is filled with wild pokemon, you could run into a pokemon at any time!)')
        print()
        print('It sure is dark in here! You can see a few other trainers stumbling around, and well as a few paths you can take')
        print('There is a man in hiking gear to the west, behind him is a rope ladder leading through a hole in the ground')
        print('To the east there is a girl with a flashlight, she is walking down the other path.')
        print('Lastly, there is the tunnel exit to the road to Pewter City')
        action = menuSelect('What would you like to do?',\
                            ['Talk to the Hiker','Go down the rope ladder','Talk to the girl','Move down the east path (Area 2)','Exit toward Pewter City','Menu'])
        if action <= 5:
            passed = MTMoonCaveWild(player)
            if passed == False:
                return gameState.lastPokecenter
        
        if action == 1:
            passed = trainerEncounter(player, hikerNorton)
            if passed == False:
                return gameState.lastPokecenter
            
        elif action == 2:
            return 'MTMoonLowerLevel1'
            
        elif action == 3:
            passed = trainerEncounter(player, lassDoris)
            if passed == False:
                return gameState.lastPokecenter
            
        elif action == 4:
            return 'MTMoonArea2'
        elif action == 5:
            return 'MTMoonEntrance'
        else:
            menu(player)

def MTMoonLowerLevel1(player):
    rocketHobb = gameState.trainers.MTMoonTrainers.rocketHobb
    while True:
        os.system(clearVar)
        print('(Mt. Moon Lower Level 1)')
        print('(this cave is filled with wild pokemon, you could run into a pokemon at any time!)')
        print()
        print('You get to the bottom of the ladder and look around...')
        print('it\'s a small room, not much is in here. But in the corner you see a strange man dressed in black fiddling with something')
        action = menuSelect('What would you like to do?',\
                            ['Talk to the man','Go back up the ladder','Menu'])
        if action <=2:
            passed = MTMoonCaveWild(player)
            if passed == False:
                return gameState.lastPokecenter
            
        if action == 1:
            passed = trainerEncounter(player, rocketHobb)
            if passed == False:
                return gameState.lastPokecenter        
        elif action == 2:
            return 'MTMoonArea1'
        else:
            menu(player)

def MTMoonArea2(player):
    superNerdHerbert = gameState.trainers.MTMoonTrainers.superNerdHerbert
    while True:
        os.system(clearVar)
        print('(Mt. Moon Area 2)')
        print('(this cave is filled with wild pokemon, you could run into a pokemon at any time!)')
        print()
        print('To the south there is a man in a lab coat, the path goes to the north, the path toward the entrance, and there is another rope ladder leader down to the east')
        action = menuSelect('What would you like to do?',\
                            ['Talk to the man in the lab coat','Go down the north path (Area 3)','Go down the path toward the entrance (Area 1)','Go down the rope ladder','Menu'])
        if action <=4:
            passed = MTMoonCaveWild(player)
            if passed == False:
                return gameState.lastPokecenter
        
        if action == 1:
            passed = trainerEncounter(player, superNerdHerbert)
            if passed == False:
                return gameState.lastPokecenter
            
        elif action == 2:
            return 'MTMoonArea3'
            
        elif action == 3:
            return 'MTMoonArea1'   
        elif action == 4:
            print('You climb down the rope ladder...')
            input()
            return 'MTMoonLowerLevel2'
        else:
            menu(player)

def MTMoonLowerLevel2(player):
    rocketDex = gameState.trainers.MTMoonTrainers.rocketDex
    rocketTex = gameState.trainers.MTMoonTrainers.rocketTex
    while True:
        os.system(clearVar)
        print('(Mt. Moon Lower Level 2)')
        print('(this cave is filled with wild pokemon, you could run into a pokemon at any time!)')
        print()
        print('You get to the bottom of the ladder and look around...')
        print('it\'s very dark down here but in the corner you can see two men chatting while they pack things you can\'t make out into the boxes')
        if len(rocketDex.pokeList)>0 or len(rocketTex.pokeList)>0:
            action = menuSelect('What would you like to do?',\
                                ['Yell at them','Sneak up on them','Go back up','Menu'])
        else:
            action = menuSelect('What would you like to do?',\
                                ['Look in the boxes','Go back up','Menu'])
        if action <= 3:
            passed = MTMoonCaveWild(player)
            if passed == False:
                return gameState.lastPokecenter
        
        if action == 1:
            if len(rocketDex.pokeList)>0 or len(rocketTex.pokeList)>0:
                print('You yell at them, letting them know you\'re there...')
                input()
                print('Man 1: "Hey Tex, looks like we\'ve got a live one!"')
                input()
                print('Man 2: "Yeah! let\'s grab him before he can squeal!"')
                input()
                passed = trainerEncounter(player, rocketDex)
                if passed == False:
                    return gameState.lastPokecenter
                
                passed = trainerEncounter(player, rocketTex)
                if passed == False:
                    return gameState.lastPokecenter
            else:
                print('They\'re full of fossils taken from this cave!')
                input()
                print('Rocket Tex: "Don\'t get any ideas kid, these fossils are ours!"')
                input()
        elif action == 2:
            if len(rocketDex.pokeList)>0 or len(rocketTex.pokeList)>0:
                print('As you sneak up you can overhear a bit of their conversation...')
                print()
                print('Man 1: "Why does the boss want these again?"')
                input()
                print('Man 2: "He found a place down south that can resurrect them!"')
                input()
                print('Man 1: "Whoah, that\'s crazy. Technology sure is amazing..."')
                print('Man 2: "Hey, there\'s a kid here, get \'em!"')
                passed = trainerEncounter(player, rocketDex)
                if passed == False:
                    return gameState.lastPokecenter
                
                passed = trainerEncounter(player, rocketTex)
                if passed == False:
                    return gameState.lastPokecenter
            else:
                return 'MTMoonArea2'
        elif action == 3:
            if len(rocketDex.pokeList)>0 or len(rocketTex.pokeList)>0:
                return 'MTMoonArea2'
            else:
                menu(player)
        else:
            menu(player)

def MTMoonArea3(player):
    while True:
        os.system(clearVar)
        print('(Mt. Moon Area 3)')
        print('(this cave is filled with wild pokemon, you could run into a pokemon at any time!)')
        print()
        print('This path slopes down as you go deeper. No doubt about it, at the end of the tunnel there is a stairwell leading into the depths')
        action = menuSelect('What would you like to do?',\
                            ['Go down the stairwell (Area 4)','Go down the path toward Pewter City (Area 2)','Menu'])
        if action <= 2:
            passed = MTMoonCaveWild(player)
            if passed == False:
                return gameState.lastPokecenter
        
        if action == 1:
            return 'MTMoonArea4'
            
        elif action == 2:
            return 'MTMoonArea2'
            
        else:
            menu(player)

def MTMoonArea4(player):
    rocketLouise = gameState.trainers.MTMoonTrainers.rocketLouise
    superNerdGarrett = gameState.trainers.MTMoonTrainers.superNerdGarrett
    while True:
        os.system(clearVar)
        print('(Mt. Moon Area 4)')
        print('(this cave is filled with wild pokemon, you could run into a pokemon at any time!)')
        print()
        if len(rocketLouise.pokeList)>0 or len(superNerdGarrett.pokeList)>0:
            print('The lower level of this tunnel is dark and dingy, but ahead you can see two figures...')
            input()
            print('Lady: "Garrett, you said you could identify it..."')
            input()
            print('Garrett: "I\'m trying but I don\'t have my books!"')
            input()
            action = menuSelect('What would you like to do?',\
                                ['approach them','go back (Area3)','Menu'])
            if action <= 2:
                passed = MTMoonCaveWild(player)
                if passed == False:
                    return gameState.lastPokecenter
            
            if action == 1:
                print('Lady: "There\'s someone here!"')
                input()
                passed = trainerEncounter(player, rocketLouise)
                if passed == False:
                    return gameState.lastPokecenter
                print('Garrett: "You\'re trying to take my fossils! I won\'t let you!"')
                input()
                passed = trainerEncounter(player, superNerdGarrett)
                if passed == False:
                    return gameState.lastPokecenter
                action1 = menuSelect('Garrett: "which one do you want?"',\
                    ['Helix Fossil','Dome Fossil'])
                if action1 == 1:
                    print('Got the Helix Fossil!')
                    input()
                    player.itemList.append('Helix Fossil')
                    print('Garrett: "then I\'ll take this one"')
                    print('Garrett got the Dome Fossil!')
                    input()
                else:
                    print('Got the Dome Fossil!')
                    input()
                    player.itemList.append('Dome Fossil')
                    print('Garrett: "then I\'ll take this one"')
                    print('Garrett got the Helix Fossil!')
                    input()
            elif action == 2:
                return 'MTMoonArea3'
                
            else:
                menu(player)
        else:
            print('The exit of the Mt. Moon tunnel is just ahead, there is also the staircase that leads into the cave')
            print('Garrett is standing admiring his fossil')
            action = menuSelect('What would you like to do?',\
                                ['Leave Mt. Moon','go deeper into the cave (Area3)','Talk to Garrett','Menu'])
            if action <= 2:
                passed = MTMoonCaveWild(player)
                if passed == False:
                    return gameState.lastPokecenter
                
            if action == 1:
                print('You step out of Mt. Moon..')
                input()
                return 'ceruleanCity'
            elif action == 2:
                return 'MTMoonArea3'
            elif action == 3:
                print('Garrett: "isn\'t it pretty? the Boss said there\'s a place on Cinnabar Island that can resurrect pokemon from a fossil!"')
                input()
            else:
                menu(player)

def ceruleanCity(player):
    while True:
        os.system(clearVar)
        print('Cerulean City! home to Misty\'s powerful Water Type Gym. You might be able to challenge her!')
        print('In this town there is a Pokecenter and a Pokemart!')
        action = menuSelect('Where would you like to go?',['Pokecenter','Pokemart','Pokemon Gym','Menu'])
        if action == 1:
            gameState.lastPokecenter = 'ceruleanCity'
            pokeCenter(player)
        elif action == 2:
            itemShop(player)
        elif action == 3:
            print('Man: "Hold up there friend! you\'re not ready to challenge Misty yet!"')
            input()
        else:
            menu(player)

    
ashPidgey = pokemonGenerator(pokedex.pidgey, 5, [earthquake, withdraw, superFang, pinMissile],1.5)
garyPidgey = pokemonGenerator(pokedex.pidgey,30,[leer],1.5)
ashBulbasaur = pokemonGenerator(pokedex.bulbasaur,5,[sonicBoom, selfdestruct, glare, haze],1.5)
garyBulbasaur = pokemonGenerator(pokedex.bulbasaur, 30, [leer],1.5)
ashSquirtle = pokemonGenerator(pokedex.squirtle, 5, [furyAttack, tailWhip, bubble],1.5)
garyCharmander = pokemonGenerator(pokedex.charmander, 30, [leer],1.5)
garySquirtle = pokemonGenerator(pokedex.squirtle, 5, [tailWhip],1.5)
ashCharmander = pokemonGenerator(pokedex.charmander, 5, [scratch, furyAttack],1.5)
ashBeedrill = pokemonGenerator(pokedex.beedrill,5,[furyAttack,poisonSting],1.5)
ashPikachu = pokemonGenerator(pokedex.pikachu, 5, [waterGun, drillPeck, hydroPump, explosion],1.5)

ash = trainer('ash', [ashBulbasaur, ashPidgey, ashSquirtle, ashPikachu, ashBeedrill], [['Pokeball',5],['Potion',5]], 500,'','')
gary = trainer('gary', [garyCharmander, garyPidgey, garyBulbasaur], [], 10,'','')

"""
main game area
"""

modules = {'bedroom':bedroom, 'momsHouse':momsHouse, 'lab':lab, 'garysHouse':garysHouse, 'route29north':route29north, 'palletTown':palletTown, 'viridianCity':viridianCity,\
            'route29south':route29south, 'victoryRoadApproachWest':victoryRoadApproachWest,'victoryRoadApproach':victoryRoadApproach, 'viridianArea1':viridianArea1, 'viridianArea2north':viridianArea2north, 'viridianArea2south':viridianArea2south, 'viridianArea3':viridianArea3,\
           'viridianArea4north':viridianArea4north,'viridianArea4south':viridianArea4south, 'pewterCity':pewterCity, 'rockGym':rockGym, 'museumFirst':museumFirst,\
           'MTMoon1east':MTMoon1east, 'MTMoon1west':MTMoon1west, 'MTMoon2east':MTMoon2east, 'MTMoon2west':MTMoon2west, 'MTMoon3east':MTMoon3east, 'MTMoon3west':MTMoon3west, 'MTMoonEntrance':MTMoonEntrance,\
           'MTMoonArea1':MTMoonArea1, 'MTMoonLowerLevel1':MTMoonLowerLevel1, 'MTMoonArea2':MTMoonArea2, 'MTMoonLowerLevel2':MTMoonLowerLevel2, 'MTMoonArea3':MTMoonArea3, 'MTMoonArea4':MTMoonArea4,\
           'ceruleanCity':ceruleanCity}

#print(battle(ash, gary, False))
def pokemon():
    try:
        print(main(bedroom,modules)) #runs the game
    except Exception as e:
        print()
        print('ERROR, take a screenshot before hitting enter!')
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
        for i in range(5):
            input()
