from mechanics import *

def myBedroomFirst(player):
    """
    WIP
    """
    while True:
        os.system(clearVar)
        print('You awake to the sound of your alarm, your Mom is shouting that you\'ll be late to school. It\'s time to get up!')
        print('As you wipe the sleep from your eyes a cold realization washes over you, you didn\'t finish your homework! And it\'s due today!!!')
        action = menuSelect('What would you like to do?',['Get dressed, head downstairs','Check what\'s on T.V.','Hit snooze, try and catch a few more ZZZ','Run to my computer, there\'s still time to finish!','Menu'])
        if action == 1:
            return 'myHouseNoQuiz'
        elif action == 2:
            print('It\'s a weather report for Gyarapolis, looks like clear skies with a chance of thunderstorms in the afternoon')
            input()
        elif action == 3:
            print('...Mom:"',player.name,'GET UP! YOU ARE GOING TO BE LATE!! DON\'T MAKE ME COME UP THERE!!!"')
            input()
        elif action == 4:
            return 'quiz'
        else:
            menu(player) 
            
def myHouseNoQuiz(player):
    """
    WIP
    """
    while True:
        os.system(clearVar)
        print('Mom:"Good Morning! Big Day today, did you finish your homework?')
        action = menuSelect('What would you like to do?',['"Yeah of course, who do you think I am?"','Go back upstairs without a word.','Try to run out of the house without her noticing.','"Oh yeah, I forgot it upstairs!','Menu'])#enter question here, along with the list of possible answers
        if action == 1: 
            print('Mom: A liar apparently, go back up there and get it done!')
            input()
            return 'quiz'
        elif action == 2:
            print('Mom: I thought so, I\'ll have breakfast waiting for you when you are done.')
            input()
            return 'quiz'
        elif action == 3:
            print('Dad: Where do you think you\'re going?!')
            input()
        elif action == 4:
            print('Mom: Uh, huh, sure you did.')
            input()
            return 'quiz'
        else:
            menu(player)

def quiz(player):
    quizAnswers =[]
    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    e = 'e'
    while True:
        os.system(clearVar)
        print('You sit at your desk and jostle the computer mouse to bring it out of sleep mode, your homework is still loaded from the night before. It\'s a personality quiz, meant to get a feel for your aptitude toward certain pokemon!')
        action = menuSelect('What is your favorite color?',['A cool Cerulean','A fiery Vermillion','A vibrant Viridian','A fun Fuschia','A subtle Saffron'])
        if action == 1:
            quizAnswers.append(a)
        elif action == 2:
            quizAnswers.append(b)
        elif action == 3:
            quizAnswers.append(c)
        elif action == 4:
            quizAnswers.append(d)
        else:
            quizAnswers.append(e)
            
        print('Answer 1/20 recorded')
        input()

        action = menuSelect('Aw man this is gonna take forever...', ['Keep going','Answer randomly'])
        if action == 1:
        
            action = menuSelect('Someone approaches you on the street and returns something dropped. How do you respond?',['Say thank you regularly','Say thank you, but play it cool','Say something self-effacing','Say thank you and offer them a reward','Say it\'s not yours'])#enter question here, along with the list of possible answers
            if action == 1:
                quizAnswers.append(a)
            elif action == 2:
                quizAnswers.append(b)
                #return 'newModule'
            elif action == 3:
                quizAnswers.append(c)
                #return 'newModule'
            elif action == 4:
                quizAnswers.append(d)
                #return 'newModule'
            else:
                quizAnswers.append(e)
            print('Answer 2/20 recorded')
            input()

            action = menuSelect('You arrive at a large birthday party cellebration. What do you do first?',['Find a small group in the corner to chat with','See if there is a party game to play','Find some people you haven\'t met and introduce yourself','Head to the dance floor and show off some moves','Go to the snack bar and get something to eat and drink'])#enter question here, along with the list of possible answers
            if action == 1: #the number of actions will equal the number of possible answers in the last line
                quizAnswers.append(e)
                #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
            elif action == 2:
                quizAnswers.append(d)
                #return 'newModule'
            elif action == 3:
                quizAnswers.append(c)
                #return 'newModule'
            elif action == 4:
                quizAnswers.append(b)
                #return 'newModule'
            else:
                quizAnswers.append(a)
            print('Answer 3/20 recorded')
            input()

            action = menuSelect('What is your favorite time of day?',['morning','midday','afternoon','evening','night'])#enter question here, along with the list of possible answers
            if action == 1: #the number of actions will equal the number of possible answers in the last line
                quizAnswers.append(c)
                #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
            elif action == 2:
                quizAnswers.append(b)
                #return 'newModule'
            elif action == 3:
                quizAnswers.append(a)
                #return 'newModule'
            elif action == 4:
                quizAnswers.append(d)
                #return 'newModule'
            else:
                quizAnswers.append(e)
            print('Answer 4/20 recorded')
            input()

            action = menuSelect('What is your favorite subject in school?',['Math','English','Gym','Science','History'])#enter question here, along with the list of possible answers
            if action == 1: #the number of actions will equal the number of possible answers in the last line
                quizAnswers.append(e)
                #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
            elif action == 2:
                quizAnswers.append(b)
                #return 'newModule'
            elif action == 3:
                quizAnswers.append(d)
                #return 'newModule'
            elif action == 4:
                quizAnswers.append(a)
                #return 'newModule'
            else:
                quizAnswers.append(c)
            print('Answer 5/20 recorded')
            input()

            action = menuSelect('A human hand extends out of the toilet! What do you do?',['Try to flush it','Scream and run','Check behind the toilet','Slam the lid on it','Shake hands with it'])#enter question here, along with the list of possible answers
            if action == 1: #the number of actions will equal the number of possible answers in the last line
                quizAnswers.append(a)
                #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
            elif action == 2:
                quizAnswers.append(c)
                #return 'newModule'
            elif action == 3:
                quizAnswers.append(e)
                #return 'newModule'
            elif action == 4:
                quizAnswers.append(d)
                #return 'newModule'
            else:
                quizAnswers.append(b)
            print('Answer 6/20 recorded')
            input()

            action = menuSelect('What is your ideal vacation?',['A hike through the mountains','A cabin by a lake','A week at the beach','A rainforest tour','A trip to a foreign city'])#enter question here, along with the list of possible answers
            if action == 1: #the number of actions will equal the number of possible answers in the last line
                quizAnswers.append(b)
                #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
            elif action == 2:
                quizAnswers.append(a)
                #return 'newModule'
            elif action == 3:
                quizAnswers.append(d)
                #return 'newModule'
            elif action == 4:
                quizAnswers.append(c)
                #return 'newModule'
            else:
                quizAnswers.append(e)
            print('Answer 7/20 recorded')
            input()

            action = menuSelect('You have a summer assignment to complete before school starts. How do you do it?',['Finish it as soon as possible','Slowly work on it throughout the summer','Wait until your friends have started theirs','Rush to finish it last minute','Forget about it completely/Blow it off'])#enter question here, along with the list of possible answers
            if action == 1: #the number of actions will equal the number of possible answers in the last line
                quizAnswers.append(e)
                #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
            elif action == 2:
                quizAnswers.append(c)
                #return 'newModule'
            elif action == 3:
                quizAnswers.append(a)
                #return 'newModule'
            elif action == 4:
                quizAnswers.append(b)
                #return 'newModule'
            else:
                quizAnswers.append(d)
            print('Answer 8/20 recorded')
            input()

            action = menuSelect('Would you go into a haunted house?',['Uh... n-no','Yeah there\'s no such thing','Only with a friend','If someone dared me','If I was with someone I like'])#enter question here, along with the list of possible answers
            if action == 1: #the number of actions will equal the number of possible answers in the last line
                quizAnswers.append(e)
                #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
            elif action == 2:
                quizAnswers.append(d)
                #return 'newModule'
            elif action == 3:
                quizAnswers.append(a)
                #return 'newModule'
            elif action == 4:
                quizAnswers.append(b)
                #return 'newModule'
            else:
                quizAnswers.append(c)
            print('Answer 9/20 recorded')
            input()

            action = menuSelect('What do you usually eat for breakfast?',['A fruit smoothie','cereal','eggs','I don\'t eat breakfast','toast'])#enter question here, along with the list of possible answers
            if action == 1: #the number of actions will equal the number of possible answers in the last line
                quizAnswers.append(c)
                #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
            elif action == 2:
                quizAnswers.append(a)
                #return 'newModule'
            elif action == 3:
                quizAnswers.append(b)
                #return 'newModule'
            elif action == 4:
                quizAnswers.append(e)
                #return 'newModule'
            else:
                quizAnswers.append(b)
            print('Answer 10/20 recorded')
            input()

            action = menuSelect('What is your favorite season?',['Spring','Summer','Autumn','Winter','They all have their merits'])#enter question here, along with the list of possible answers
            if action == 1: #the number of actions will equal the number of possible answers in the last line
                quizAnswers.append(c)
                #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
            elif action == 2:
                quizAnswers.append(b)
                #return 'newModule'
            elif action == 3:
                quizAnswers.append(d)
                #return 'newModule'
            elif action == 4:
                quizAnswers.append(a)
                #return 'newModule'
            else:
                quizAnswers.append(e)
            print('Answer 11/20 recorded')
            input()

            action = menuSelect('You find a wallet on the side of the road. What do you do?',['Yay! Let\'s see how much\'s inside!','Is anyone watching...','Turn it in to the police','Look for I.D. see if you can find them yourself','Leave it, someone else will find it'])#enter question here, along with the list of possible answers
            if action == 1: #the number of actions will equal the number of possible answers in the last line
                quizAnswers.append(a)
                #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
            elif action == 2:
                quizAnswers.append(c)
                #return 'newModule'
            elif action == 3:
                quizAnswers.append(b)
                #return 'newModule'
            elif action == 4:
                quizAnswers.append(e)
                #return 'newModule'
            else:
                quizAnswers.append(d)
            print('Answer 12/20 recorded')
            input()

            action = menuSelect('You hear a blood-curdling scream from outside your bedroom door. How do you react?',['Burst out of the room to see what\'s wrong','Hide under your bed and whisper,"W-who goes there?..."','Ask if anyone is hurt','Try to intimidate them by answering with a louder scream','Try to see what\'s happening through the keyhole'])#enter question here, along with the list of possible answers
            if action == 1: #the number of actions will equal the number of possible answers in the last line
                quizAnswers.append(d)
                #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
            elif action == 2:
                quizAnswers.append(a)
                #return 'newModule'
            elif action == 3:
                quizAnswers.append(c)
                #return 'newModule'
            elif action == 4:
                quizAnswers.append(b)
                #return 'newModule'
            else:
                quizAnswers.append(e)
            print('Answer 13/20 recorded')
            input()

            action = menuSelect('How do you fall asleep?',['As soon as my head hits the pillow','At least a half hour mindlessly surfing on my phone','Read some chapters on a long book I\'m reading','Go over in my head what happened today and what I need to do tomorrow','Toss and turn stressing about stuff'])#enter question here, along with the list of possible answers
            if action == 1: #the number of actions will equal the number of possible answers in the last line
                quizAnswers.append(d)
                #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
            elif action == 2:
                quizAnswers.append(a)
                #return 'newModule'
            elif action == 3:
                quizAnswers.append(c)
                #return 'newModule'
            elif action == 4:
                quizAnswers.append(e)
                #return 'newModule'
            else:
                quizAnswers.append(b)
            print('Answer 14/20 recorded')
            input()

            action = menuSelect('Grab a random digit on your left hand. Which one did you grab?',['Thumb','Index finger','Middle finger','Ring finger','Pinky finger'])#enter question here, along with the list of possible answers
            if action == 1: #the number of actions will equal the number of possible answers in the last line
                quizAnswers.append(a)
                #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
            elif action == 2:
                quizAnswers.append(b)
                #return 'newModule'
            elif action == 3:
                quizAnswers.append(c)
                #return 'newModule'
            elif action == 4:
                quizAnswers.append(d)
                #return 'newModule'
            else:
                quizAnswers.append(e)
            print('Answer 15/20 recorded')
            input()

            action = menuSelect('Your dad asks what you would like him to bake for your birthday party. What would you pick?',['A face cake','A pie','A cheesecake','A mud pie','A bunch of different flavor cupcakes'])#enter question here, along with the list of possible answers
            if action == 1: #the number of actions will equal the number of possible answers in the last line
                quizAnswers.append(d)
                #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
            elif action == 2:
                quizAnswers.append(b)
                #return 'newModule'
            elif action == 3:
                quizAnswers.append(a)
                #return 'newModule'
            elif action == 4:
                quizAnswers.append(c)
                #return 'newModule'
            else:
                quizAnswers.append(e)
            print('Answer 16/20 recorded')
            input()

            action = menuSelect('Your friend fails to show up to meet at an agreed upon time. What do you do?',['Call them to see where they are','Become irritated','Complain about them to another friend','Wait patiently','Get angry and bail'])#enter question here, along with the list of possible answers
            if action == 1: #the number of actions will equal the number of possible answers in the last line
                quizAnswers.append(e)
                #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
            elif action == 2:
                quizAnswers.append(d)
                #return 'newModule'
            elif action == 3:
                quizAnswers.append(a)
                #return 'newModule'
            elif action == 4:
                quizAnswers.append(c)
                #return 'newModule'
            else:
                quizAnswers.append(b)
            print('Answer 17/20 recorded')
            input()

            action = menuSelect('Someone cuts you in line to get food. What do you do?',['Politely tell them where the back of the line is','Tap them on the shoulder and snidely ask if they\'re lost','Try to pick a fight','Loudly accuse them of cutting in line','Say nothing, but text your friend about the situation'])#enter question here, along with the list of possible answers
            if action == 1: #the number of actions will equal the number of possible answers in the last line
                quizAnswers.append(a)
                #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
            elif action == 2:
                quizAnswers.append(c)
                #return 'newModule'
            elif action == 3:
                quizAnswers.append(d)
                #return 'newModule'
            elif action == 4:
                quizAnswers.append(b)
                #return 'newModule'
            else:
                quizAnswers.append(e)
            print('Answer 18/20 recorded')
            input()

            action = menuSelect('There is a person you like, but you don\'t know how to get close. What do you do?',['Bravely declare my love','Might try to say hello','Tell a joke to get their attention','Ask a friend to see if they like me','Look from afar'])#enter question here, along with the list of possible answers
            if action == 1: #the number of actions will equal the number of possible answers in the last line
                quizAnswers.append(d)
                #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
            elif action == 2:
                quizAnswers.append(b)
                #return 'newModule'
            elif action == 3:
                quizAnswers.append(c)
                #return 'newModule'
            elif action == 4:
                quizAnswers.append(a)
                #return 'newModule'
            else:
                quizAnswers.append(e)
            print('Answer 19/20 recorded')
            input()

            action = menuSelect('You are starting a new D&D campaign, your Dungeon Master asks you to make a character. What do you make?',['A fighter','A wizard','A bard','A palladin','A druid'])#enter question here, along with the list of possible answers
            if action == 1: #the number of actions will equal the number of possible answers in the last line
                quizAnswers.append(d)
                #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
            elif action == 2:
                quizAnswers.append(e)
                #return 'newModule'
            elif action == 3:
                quizAnswers.append(b)
                #return 'newModule'
            elif action == 4:
                quizAnswers.append(a)
                #return 'newModule'
            else:
                quizAnswers.append(c)
            print('Answer 20/20 recorded')
            input()


            bulbN = quizAnswers.count('a')
            charN = quizAnswers.count('b')
            squirtN = quizAnswers.count('c')
            machN = quizAnswers.count('d')
            solosisN = quizAnswers.count('e')
        else:
            print('you decide that it\'s better to just answer randomly, you\'re already running late after all..')
            input()
            bulbN = randint(1,7)
            charN = randint(1,7)
            squirtN = randint(1,7)
            machN = randint(1,7)
            solosisN = randint(1,7)

        poke = {'Bulbasaur':bulbN,'Charmander':charN,'Squirtle':squirtN,'Machop':machN, 'Solosis':solosisN}
        highest = 0
        newPokeList = []
        for potential in poke:
            if poke[potential] >highest:
                highest = poke[potential]
                newPoke = potential
                newPokeList = [potential]
            elif poke[potential] == highest:
                newPokeList.append(potential)
        if len(newPokeList) > 1:
            print('That\'s interesting, you fell between',len(newPokeList),'pokemon')
            action = menuSelect('Which would you prefer?',newPokeList)
            newPoke = newPokeList[action-1]
        playerPoke = newPoke
        player.pokeList.append(potentialPokes[playerPoke])

        return 'getFirstPoke'

def getFirstPoke(player):
    print('Whew, glad to be done with that! Time to go to school')
    input()
    while True:
        os.system(clearVar)
        action = menuSelect('You go downstairs and your Mom and Dad are waiting for you. "We have a surprise for you. It\'s a ' +player.pokeList[0].name +'! What do you think?"',['I love it!','Thank you so much!','Thanks...','It\'s so cute!','It looks like Grandpa!'])#enter question here, along with the list of possible answers
        if action == 1:
            print('Dad: Hopefully they\'ll be a partner for life!\nDad\'s Quagsire: QUAG!')
            input()
            return 'walkToSchool'

        elif action == 2:
            print('Mom: You are very welcome.\nMom\'s Blissey: Sey, sey, Bliss!')
            input()
            return 'walkToSchool'

        elif action == 3:
            print('Mom:...Well if you don\'t like it... \nDad: We worked hard to get you this, if you don\'t like it you can go out and catch something!')
            input()
            return 'walkToSchool'

        elif action == 4:
            print('Dad\'s Quagsire:SIRE!!!\nMom\'s Blissey: BLISS!\nMom and Dad: I think they are inclined to agree! HAHA')
            input()
            return 'walkToSchool'

        else:
            print('Mom: Gasp! Well that\;s not very nice!\nDad:HAHA but it really does!\nDad\'s Quagsire:SIRE! SIRE!')
            input()
            return 'walkToSchool'

def walkToSchool(player):
    while True:
        os.system(clearVar)
        print('You leave the house to go to school')
        print('on the way out you run into your friend Oscar')
        print('Oscar: "Hey! '+player.name+' did you get a pokemon? So did I! Wanna battle and see how they do?')
        action = menuSelect('What would you like to do?',['Yeah let\'s do it!','Maybe later, we\'re late!','Menu'])
        if action == 1:
            print('Oscar: "Yeah! that\'s the spirit!"')
            won = trainerEncounter(player, gameState.trainers.gyroTrainers.firstEncounterOscar,\
                                   '"Take it easy on me, I\'ve never done this before!"',\
                                   '"Phew, that was intense! just like camping"')
            player.partyHeal()
            print('With that, you and your friend decide to continue your walk to school')
            input()
            return 'firstDaySchool'
            
        elif action == 2:
            print('Oscar: "Oh come on! don\'t be lame!"')
            won = trainerEncounter(player, gameState.trainers.gyroTrainers.firstEncounterOscar,\
                                   '"Take it easy on me, I\'ve never done this before!"',\
                                   '"Phew, that was intense! just like camping"')
            player.partyHeal()
            print('With that, you and your friend decide to continue your walk to school')
            input()
            return 'firstDaySchool'
        else:
            menu(player)

def firstDaySchool(player):
    i=0
    while True:
        if i < 2:
            os.system(clearVar)
            print('You walk into school and find your seat in the classroom, there are a view minutes before class starts')
            print('You see something written on the board and your rival Charles is talking to his friends next to you')
            action = menuSelect('What would you like to do?',['Look at the board','Eves drop on Charles','Wait for class to start','Menu'])
            i+=1
            if action == 1:
                if i ==1:
                    print('it\'s a pokemon type advantage chart! the attacking types are on the y-axis, and the defending types are on the x-axis')
                    printChart()
                    input()
                else:
                    print('No time!')
                    i+=2
            elif action == 2:
                if i == 1:
                    print('Charles: "My parents got me a Porygon, top of the line, latest model!"')
                    input()
                else:
                    print('Charles: "My dad is gonna pull his connections in the Mayor\'s office to get me a job after school!"')
                    input()
                    i+=2
            elif action == 3:
                print('You decide to wait it out until Ms. Ingneau arrives..')
                input()
                i+=2
                
                #return 'newModule
            else:
                menu(player) #the last option is usually menu, but doesn't have to be
        else:
            os.system(clearVar)
            print('Ms. Ingneau walks into the classroom and starts erasing the board')
            input()
            print('Ms. Ingneau: "Hello Class! Welcome back, I hope everyone had an exciting break!"')
            print('"Today we will have a quiz about pokemon type effectiveness, and I have a special prize for whoever gets the highest grade!"')
            action = menuSelect('What would you like to do?',['Look at the board','Eves drop on Charles','Wait for class to start','Menu'])

            if action == 1:
                if i ==1:
                    print('it\'s a pokemon type advantage chart! the attacking types are on the y-axis, and the defending types are on the x-axis')
                    printChart()
                    input()
                else:
                    print('No time! Ms. Ingneau comes into the room and starts erasing the board')
                    input()
                    i+=1
            elif action == 2:
                if i == 1:
                    print('Charles: "My parents got me a Porygon, top of the line, latest model!"')
                    input()
                else:
                    print('Charles: "My dad is gonna pull his connections in the Mayor\'s office to get me a job after school!"')
                    input()
            elif action == 3:
                print('You decide to wait it out until Ms. Ingneau arrives..')
                input()
            else:
                menu(player)
        
def moduleName(player):
    while True:
        os.system(clearVar)
        print('example') #Enter descriptor info here, hashtags indicate comments, they are ignored by the code
        action = menuSelect('Question',['list','of','possible','answers','Menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            print('enter dialogue here, or if pokecenter/item shop, copy pokecenter/item code')
            input()
            #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            print('enter dialogue here etc')
            input()
            #return 'newModule'
        elif action == 3:
            print('enter dialogue here, etc')
            input()
            #return 'newModule
        elif action == 4:
            print('enter dialogue here, etc')
            input()
            #return 'newModule
        else:
            menu(player) #the last option is usually menu, but doesn't have to be


def wildEncounter(player, patches):
    wild = trainer('Wild', [], {}, 10)
    caterpie1 = pokemonGenerator(pokedex.caterpie,3,[tackle, stringShot])
    caterpie2 = pokemonGenerator(pokedex.caterpie,3,[tackle, stringShot])
    caterpie3 = pokemonGenerator(pokedex.caterpie,4,[tackle, stringShot])
    caterpie4 = pokemonGenerator(pokedex.caterpie,2,[tackle, stringShot])
    weedle1 = pokemonGenerator(pokedex.weedle,3,[poisonSting, stringShot])
    weedle2 = pokemonGenerator(pokedex.weedle,2,[poisonSting, stringShot])
    weedle3 = pokemonGenerator(pokedex.weedle,4,[poisonSting, stringShot])
    kakuna1 = pokemonGenerator(pokedex.kakuna,5,[tackle, harden])
    encounters = [caterpie1, caterpie2, caterpie3, caterpie4, weedle1, weedle2, weedle3, kakuna1]
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

bulb = pokemonGenerator(pokedex.bulbasaur,5,[tackle,growl])
char = pokemonGenerator(pokedex.charmander,5,[scratch,tailWhip])
squirt = pokemonGenerator(pokedex.squirtle,5,[tackle,tailWhip])
solosis = pokemonGenerator(pokedex.solosis,5,[tackle,leer])
machop = pokemonGenerator(pokedex.machop,5,[scratch,leer])

potentialPokes = {'Bulbasaur':bulb,'Charmander':char,'Squirtle':squirt, 'Solosis':solosis,'Machop':machop}

modules = {'myHouseNoQuiz':myHouseNoQuiz, 'quiz':quiz, 'getFirstPoke':getFirstPoke, 'walkToSchool':walkToSchool, 'firstDaySchool':firstDaySchool}

print(main(myBedroomFirst, modules))
