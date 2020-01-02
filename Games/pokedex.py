from moves import *
from random import *
import copy
import inspect

def menuValid(number, maxNum):
    noGood = 'invalid input'
    try:
        number = int(number)
        if number <= maxNum and number >0:
            return True
        else:
            print(noGood)
            return False
    except ValueError:
        print(noGood)
        
class pokemon:
    """
    creates a pokemon

    takes a name as a string
    starting pokemon level; integer
    typ is the pokemon type; list of two entries; ['water', 'fire']
    takes maxHP as an integer
    takes stats as a dictionary formatted as {'attack':30, 'defense':40, 'speed': 40}
    takes moves as a dictionary formatted as {1:[tackle, 'tackle'],etc}
    baseXP is the base amount of XP the pokemon gives if killed; integer
    needXP is amount of XP needed to gain a level; integer
    XPmod is how much the gained XP is adjusted; two digit, single decimel place; 1.6 or 0.8 
    """
    def __init__(self,name, pokeNum, entry, level,typ,statMods, moves, needXP,XPmod,evo, pokedexSprite, frontSprite, backSprite, trainer=1):
        self.name = name
        self.pokeNum = pokeNum
        self.entry = entry
        self.level = level
        self.typ = typ
        self.maxHP = 10
        self.statMods = statMods
        self.moves = moves
        self.HP = self.maxHP #sets current HP equal to max HP at creation
        self.needXP = needXP
        self.XPmod = XPmod
        self.gainedXP = 0
        self.stats = {'attack':5, 'defense':5, 'sp.attack':5, 'sp.defense':5, 'speed':5}
        self.tempStats = copy.deepcopy(self.stats)
        self.status = []
        self.evo = evo
        self.trainer = trainer
        self.pokedexSprite = pokedexSprite
        self.frontSprite = frontSprite
        self.backSprite = backSprite
        self.timesAttacked = 0
        self.referenceHP = self.HP
        self.opponents = []

    def getName(self): #gives the name of the pokemon
        print(self.name)

    def HPBar(self): #displays the current HP of the pokemon as a bar
        percentage = self.HP/self.maxHP
        remaining = round(20*percentage)
        taken = 20 - remaining
        return '('+'#'*remaining+'-'*taken+')'

    def getMoves(self): #returns the list of available moves
        for i in range(1,len(self.moves)+1):
            print(str(i)+'.', self.moves[i].name)
        print(str(i+1)+'. cancel')

    def learnMove(self, move):
        moveNo = len(self.moves)+1
        if move not in self.moves:
            if moveNo<=4:
                self.moves[moveNo] = move
                print(self.name, 'learned', move.name+'!')
                input()
            else:
                while True:
                    print(self.name, 'is trying to learn', move.name,'but',self.name,'already knows four moves')
                    print('Would you like to replace one of these moves?')
                    self.getMoves()
                    action = input()                
                    if menuValid(action, 5):
                        action = int(action)
                        if action == 5:
                            print(self.name, 'did not learn', move.name)
                            break
                        else:
                            print(self.moves[action].name,'will be replaced with',move.name)
                            while True:
                                print('Are you sure? y/n')
                                sure = input()
                                if sure ==  'y' or sure == 'n':
                                    break
                            if sure == 'y':
                                self.moves[action] = move
                                print(self.name, 'learned', self.moves[action].name+'!')
                                break
                        

    def damageTaken(self, damage): #reduces the HP when damage is taken
        if damage == 0:
            self.HP = self.HP
        else:
            self.HP -= damage
            if self.HP<0:
                self.HP = 0


    def statChange(self, stat, boost): #reduces the appropriate stat when stat damage is taken
        minstat = .131
        maxstat = 4
        ratio = self.tempStats[str(stat)]/self.stats[str(stat)]
        margin = 0.02
        if abs(ratio - minstat)<margin:
            print(str(self.name)+'\'s', stat,'can\'t be reduced anymore!')
        elif abs(ratio-maxstat)<margin:
            print(str(self.name)+'\'s',stat,'can\'t be increased anymore!')
        else:
            if boost:
                change = 'increased!'
                self.tempStats[str(stat)] *= 1.33
            else:
                change = 'decreased!'
                self.tempStats[str(stat)]*= 0.66
            print(self.name+'\'s',stat,change)

    def XPGain(self, gain):
        self.gainedXP += gain
        print(self.name,'gained',gain,'experience!')
        if self.gainedXP >= self.needXP:
            self.levelUp()

    def levelUp(self):
        print(self.name, 'grew to level', str(self.level+1)+'!')
        self.gainedXP = self.gainedXP - self.needXP
        self.addLevel(2)
        print(self.stats)
        if self.level in moveTree[self.name]:
            self.learnMove(moveTree[self.name][self.level])

    def evolve(self):
        print('Huh?',self.name,'is evolving!')
        input()
        for level in self.evo:
            newPoke = self.evo[level]
        for thing in evos:
            if thing[0] == newPoke:
                newPoke = thing[1]
        print(self.name,'evolved into',newPoke.name+'!')
        self.name = newPoke.name
        self.pokeNum = newPoke.pokeNum
        self.statMods = newPoke.statMods
        self.entry = newPoke.entry
        self.evo = newPoke.evo
        self.needXP = newPoke.needXP
        self.maxHP = round(10+self.level*self.statMods[0])
        self.stats['attack'] = round(5+self.level*self.statMods[1])
        self.stats['defense'] = round(5+self.level*self.statMods[2])
        self.stats['sp.attack'] = round(5+self.level*self.statMods[3])
        self.stats['sp.defense'] = round(5+self.level*self.statMods[4])
        self.stats['speed'] = round(5+self.level*self.statMods[5])
        self.tempStats = self.stats
        self.pokedexSprite = newPoke.pokedexSprite
        self.frontSprite = newPoke.frontSprite
        self.backSprite = newPoke.backSprite
        for i in range(self.level-1):
            self.needXP = round(self.needXP*self.XPmod)
        
    def addLevel(self, endLevel):
        levelsAdded = endLevel - 1
        self.level+=levelsAdded
        if self.level in self.evo:
            self.evolve()
        self.maxHP += round(levelsAdded*self.statMods[0])
        self.HP += round(levelsAdded*self.statMods[0])
        self.stats['attack'] = round(self.stats['attack']+levelsAdded*self.statMods[1])
        self.stats['defense'] = round(self.stats['defense']+levelsAdded*self.statMods[2])
        self.stats['sp.attack'] = round(self.stats['sp.attack']+levelsAdded*self.statMods[3])
        self.stats['sp.defense'] = round(self.stats['sp.defense']+levelsAdded*self.statMods[4])
        self.stats['speed'] = round(self.stats['speed']+levelsAdded*self.statMods[5])
        self.tempStats['attack']= round(self.tempStats['attack']+levelsAdded*self.statMods[1])
        self.tempStats['defense']= round(self.tempStats['defense']+levelsAdded*self.statMods[2])
        self.tempStats['sp.attack']= round(self.tempStats['sp.attack']+levelsAdded*self.statMods[3])
        self.tempStats['sp.defense']= round(self.tempStats['sp.defense']+levelsAdded*self.statMods[4])
        self.tempStats['speed']= round(self.tempStats['speed']+levelsAdded*self.statMods[5])
        for i in range(levelsAdded):
            self.needXP = round(self.needXP*self.XPmod)

    def statRestore(self):
        self.tempStats = copy.deepcopy(self.stats)

    def heal(self, amount):
        self.HP += amount
        if self.HP > self.maxHP:
            self.HP = self.maxHP
    

    def statusAction(self, opponent, position):
        """
        Performs the relevant status effects
        position is the place in the battle sequence it happens
        'before' = before the turn
        'during' = during the turn
        'after' = after the turn
        """
        act = []

        #non-exclusive statuses
        if 'flinched' in self.status:
            if position == 'before':
                self.status.remove('flinched')
            if position == 'during':
                print(self.name,'flinched!')
                act.append(False)
            
        
        if 'bide' in self.status:
            if position == 'during':
                if self.timesAttacked <2:
                    print(self.name,'is biding their time')
                    input()
                    act.append(False)
                else:
                    damageVal = 2*(self.referenceHP - self.HP)
                    print(self.name,'unleashed energy!')
                    input()
                    opponent.damageTaken(damageVal)
                    self.status.remove('bide')
                    act.append(False)
                
        
        if 'leech' in self.status:
            if position == 'after':
                damageVal = self.maxHP//16+1
                self.damageTaken(damageVal)
                opponent.heal(damageVal)
                print(opponent.name,'absorbed health from',self.name)
                input()

        if 'confusion' in self.status:
            if position == 'before':
                print(self.name,'is confused!')
            if position == 'during':
                chance = [True, False, False, False]
                if self.timesAttacked == 4:
                    chance = [True]
                hurt = [True,False]
                clear = choice(chance)
                if clear:
                    print(self.name,'broke out of it\'s confusion!')
                    self.status.remove('confusion')
                    act.append(True)
                else:
                    if hurt:
                        print(self.name,'hurt itself in it\'s confusion!')
                        selfDamage = damage(self, self, 40, 'attack','defense')
                        self.damageTaken(round(selfDamage))
                        act.append(False)
                        input()


        #exclusive statuses               
        if 'burn' in self.status:
            if position == 'before':
                self.tempStats['attack'] = self.stats['attack']/2
            elif position == 'after':
                damageVal = round(self.maxHP/8)
                self.damageTaken(damageVal)
                print(self.name, 'was hurt by the burn')
                input()

        elif 'paralyzed' in self.status:
            if position == 'before':
                print(self.name,'is paralyzed, it may not attack')
            elif position == 'during':    
                chance = [True,True,False]
                paralyze = choice(chance)
                if paralyze == False:
                    print(self.name, 'is fully paralyzed!')
                    input()
                act.append(paralyze)
        
        elif 'sleep' in self.status:
            if position == 'before':
                print(self.name,'is asleep!')
            elif position == 'during':
                chance = [True,False,False]
                if self.timesAttacked == 4:
                    chance = [True]
                sleep = choice(chance)
                if sleep == True:
                    print(self.name,'woke up!')
                    self.status.remove('sleep')
                    act.append(True)
                else:
                    print(self.name,'is fast asleep')
                    input()
                    act.append(False)
                    
        elif 'poison' in self.status:
            if position == 'after':
                damageVal = round(self.maxHP/8)
                self.damageTaken(damageVal)
                print(self.name, 'was hurt by the poison')
                input()
              
        return False not in act

def pokemonGenerator(pokemon, level, givenMoves, trainer = 1):
    newPoke = copy.deepcopy(pokemon)
    newPoke.trainer = trainer
    newPoke.addLevel(level)
    i = 1
    for move in givenMoves:
        newPoke.moves[i] = move
        i += 1
    return newPoke



class pokedex: #fills the global pokedex
    def __init__(self):
        self.bulbasaur = pokemon('Bulbasaur', 1, 'This pokemon has a large plant bulb on it\'s back', 1, ['grass','poison'],\
                                 [2,0.98,0.98,1.3,1.3,0.9],{}, 20, 1.3,{15:'ivysaur'},"""
                        _,.------....___,.' ',.-.
                     ,-'          _,.--"        |
                   ,'         _.-'              .
                  /   ,     ,'                   `
                 .   /     /                     ``.
                 |  |     .                       \.\\
       ____      |___._.  |       __               \ `.
     .'    `---""       ``"-.--"'`  \               .  \\
    .  ,            __               `              |   .
    `,'         ,-"'  .               \             |    L
   ,'          '    _.'                -._          /    |
  ,`-.    ,".   `--'                      >.      ,'     |
 . .'\'   `-'       __    ,  ,-.         /  `.__.-      ,'
 ||:, .           ,'  ;  /  / \ `        `.    .      .'/
 j|:D  \          `--'  ' ,'_  . .         `.__, \   , /
/ L:_  |                 .  "' :_;                `.'.'
.    ""'                  ""''''                    V
 `.                                 .    `.   _,..  `
   `,_   .    .                _,-'/    .. `,'   __  `
    ) \`._        ___....----"'  ,'   .'  \ |   '  \  .
   /   `. "`-.--"'         _,' ,'     `---' |    `./  |
  .   _  `""'--.._____..--"   ,             '         |
  | ." `. `-.                /-.           /          ,
  | `._.'    `,_            ;  /         ,'          .
 .'          /| `-.        . ,'         ,           ,
 '-.__ __ _,','    '`-..___;-...__   ,.'\ ____.___.'
 `"^--'..'   '-`-^-'"--    `-^-'`.''""'''`.,^.`.--' mh'""",'','')
        self.ivysaur = pokemon('Ivysaur', 2, 'This pokemon has a small flower on it\'s back',1,['grass','poison'],\
                               [2.3,1.24,1.26,1.6,1.6,1.2],{},30,1.3,{34:'venusaur'},"""
                               ,'"`.,./.
                             ,'        Y',"..
                           ,'           \  | \\
                          /              . |  `
                         /               | |   \\
            __          .                | |    .
       _   \  `. ---.   |                | j    |
      / `-._\   `Y   \  |                |.     |
     _`.    ``    \   \ |..              '      |,-'""7,....
     l     '-.     . , `|  | , |`. , ,  /,     ,'    '/   ,'_,.-.
     `-..     `-.  : :     |/ `   ' "\,' | _  /          '-'    /___
      \""' __.,.-`.: :        /   /._    l'.,'
       `--,   _.-' `".           /__ `'-.' '         .
       ,---..._,.--"""""""--.__..----,-.'   .  /    .'   ,.--
       |                          ,':| /    | /     ;.,-'--      ,.-
       |     .---.              .'  :|'     |/ ,.-='"-.`"`' _   -.'
       /    \    /               `. :|--.  _L,"---.._        "----'
     ,' `.   \ ,'           _,     `''   ``.-'       `-  -..___,'
    . ,.  .   `   __     .-'  _.-           `.     .__    \
    |. |`        "  ;   !   ,.  |             `.    `.`'---'
    ,| |C\       ` /    | ,' |(]|            -. |-..--`
   /  "'--'       '      /___|__]        `.  `- |`.
  .       ,'                   ,   /       .    `. \\
    \                      .,-'  ,'         .     `-.
     x---..`.  -'  __..--'"/""'''  ,-.      |   |   |
    / \--._'-.,.--'     _`-    _. ' /       |     -.|
   ,   .   `-..__ ...--'  _,.-' | `   ,.-.  ;   /  '|
  .  _,'         '"-----""      |    `   | /  ,'    ;
  |-'  .-.    `._               |     `._// ,'     /
 _|    `-'   _,' "`--.._________|        `,'    _ /.
//\   ,-._.'"/\__,.   _,"     /_\__/`. /'.-.'.-/_,`-' mh
`-"`"' v'    `"  `-`-"              `-'`-`  `'
""",'','')
        self.venusaur = pokemon('Venusaur',3, 'This pokemon has a large flower on it\'s back which it uses to photosynthesize',1,['grass','poison'],\
                                [2.7,1.64,1.66,2.0,2.0,1.6],{},40,1.3,{0:0},"""
                           _._       _,._
                        _.'   `. ' .'   _`.
                ,"'"/`""-.-.,/. ` V'\-,`.,--/"'"."-..
              ,'    `...,' . ,\-----._|     `.   /   \\
             `.            .`  -'`"" .._   :> `-'   `.
            ,'  ,-.  _,.-'| `..___ ,'   |'-..__   .._ L
           .    \_ -'   `-'     ..      `.-' `.`-.'_ .|
           |   ,',-,--..  ,--../  `.  .-.    , `-.  ``.
           `.,' ,  |   |  `.  /'/,,.\/  |    \|   |
                `  `---'    `j   .   \  .     '   j
              ,__`"        ,'|`'\_/`.'\'        |\-'-, _,.
       .--...`-. `-`. /    '- ..      _,    /\ ,' .--"'  ,'".
     _'-""-    --  _`'-.../ __ '.'`-^,_`-''""---....__  ' _,-`
   _.----`  _..--.'        |  "`-..-" __|'"'         .""-. ""'--.._
  /        '    /     ,  _.+-.'  ||._'   ''"". .          `     .__\\
 `---    /        /  / j'       _/|..`  -. `-`\ \   \  \   `.  \ `-..
," _.-' /    /` ./  /`_|_,-"   ','|       `. | -'`._,   L  \ .  `.   |
`"' /  /  / ,__...-----| _.,  ,'            `|----.._`-.|' |. .` ..  .
   /  '| /.,/   \--.._ `-,' ,          .  '`.'  __,., '  ''``._ \ \`,'
  /_,'---  ,     \`._,-` \ //  / . \    `._,  -`,  / / _   |   `-L -
   /       `.     ,  ..._ ' `_/ '| |\ `._'       '-.'   `.,'     |
  '         /    /  ..   `.  `./ | ; `.'    ,"" ,.  `.    \      |
   `.     ,'   ,'   | |\  |       "        |  ,'\ |   \    `    ,L
   /|`.  /    '     | `-| '                  /`-' |    L    `._/  \\
  / | .`|    |  .   `._.'                   `.__,'   .  |     |  (`
 '-""-'_|    `. `.__,._____     .    _,        ____ ,-  j     ".-'"'
        \      `-.  \/.    `"--.._    _,.---'""\/  "_,.'     /-'
         )        `-._ '-.        `--"      _.-'.-""        `.
        ./            `,. `".._________...""_.-"`.          _j
       /_\.__,"".   ,.'  "`-...________.---"     .".   ,.  / \\
              \_/''"-'                           `-'--(_,`"`-` mh
""",'','')
        self.charmander = pokemon('Charmander', 4, 'This pokemon has a fiery tail!', 1, ['fire','fire'],\
                                  [1.8,1.04,0.86,1.2,1,1.3],{}, 20, 1.3,{16:'charmeleon'},"""
              _.--""`-..
            ,'          `.
          ,'          __  `.
         /|          " __   \\
        , |           / |.   .
        |,'          !_.'|   |
      ,'             '   |   |
     /              |`--'|   |
    |                `---'   |
     .   ,                   |                       ,".
      ._     '           _'  |                    , ' \ `
  `.. `.`-...___,...---""    |       __,.        ,`"   L,|
  |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \\
-:..     `. `-..--_.,.<       `"      / `.        `-/ |   .
  `,         "''''     `.              ,'         |   |  ',,
    `.      '            '            /          '    |'. |/
      `.   |              \       _,-'           |       ''
        `._'               \   '"\                .      |
           |                '     \                `._  ,'
           |                 '     \                 .'|
           |                 .      \                | |
           |                 |       L              ,' |
           `                 |       |             /   '
            \                |       |           ,'   /
          ,' \               |  _.._ ,-..___,..-'    ,'
         /     .             .      `!             ,j'
        /       `.          /        .           .'/
       .          `.       /         |        _.'.'
        `.          7`'---'          |------"'_.'
       _,.`,_     _'                ,''-----"'
   _,-_    '       `.     .'      ,\\
   -" /`.         _,'     | _  _  _.|
    ""--'---""''''        `' '! |! /
                            `" " -' mh""",'','')
        self.charmeleon = pokemon('Charmeleon',5,'This pokemon is very aggressive!',1,['fire','fire'],\
                                  [2.26,1.28,1.16,1.6,1.3,1.6],{},30,1.3,{36:'charizard'},"""
                      ,-'`\
                  _,"'    j
           __....+       /               .
       ,-'"             /               ; `-._.'.
      /                (              ,'       .'
     |            _.    \             \   ---._ `-.
     ,|    ,   _.'  Y    \             `- ,'   \   `.`.
     l'    \ ,'._,\ `.    .              /       ,--. l
  .,-        `._  |  |    |              \       _   l .
 /              `"--'    /              .'       ``. |  )
.\    ,                 |                .        \ `. '
`.                .     |                '._  __   ;. \'
  `-..--------...'       \                  `'  `-"'.  \\
      `......___          `._                        |  \\
               /`            `..                     |   .
              /|                `-.                  |    L
             / |               \   `._               .    |
           ,'  |,-"-.   .       .     `.            /     |
         ,'    |     '   \      |       `.         /      |
       ,'     /|       \  .     |         .       /       |
     ,'      / |        \  .    +          \    ,'       .'
    .       .  |         \ |     \          \_,'        / j
    |       |  L          `|      .          `        ,' '
    |    _. |   \          /      |           .     .' ,'
    |   /  `|    \        .       |  /        |   ,' .'
    |   ,-..\     -.     ,        | /         |,.' ,'
    `. |___,`    /  `.   /`.       '          |  .'
      '-`-'     j     ` /."7-..../|          ,`-'
                |        .'  / _/_|          .
                `,       `"'/"'    \          `.
                  `,       '.       `.         |
             __,.-'         `.        \'       |
            /_,-'\          ,'        |        _.
             |___.---.   ,-'        .-':,-"`\,' .
                  L,.--"'           '-' |  ,' `-.\\
                                        `.' mh
""",'','')
        self.charizard = pokemon('Charizard',6,'This pokemon flies over forests looking for small animals to scoop up',1,['fire','flying'],\
                                 [2.66,1.68,1.56,2.18,1.7,2.0],{},40,1.3,{0:0},"""
                 ."-,.__
                 `.     `.  ,
              .--'  .._,'"-' `.
             .    .'         `'
             `.   /          ,'
               `  '--.   ,-"'
                `"`   |  \
                   -. \, |
                    `--Y.'      ___.
                         \     L._, \
               _.,        `.   <  <\                _
             ,' '           `, `.   | \            ( `
          ../, `.            `  |    .\`.           \ \_
         ,' ,..  .           _.,'    ||\l            )  '".
        , ,'   \           ,'.-.`-._,'  |           .  _._`.
      ,' /      \ \        `' ' `--/   | \          / /   ..\\
    .'  /        \ .         |\__ - _ ,'` `        / /     `.`.
    |  '          ..         `-...-"  |  `-'      / /        . `.
    | /           |L__           |    |          / /          `. `.
   , /            .   .          |    |         / /             ` `
  / /          ,. ,`._ `-_       |    |  _   ,-' /               ` \\
 / .           \"`_/. `-_ \_,.  ,'    +-' `-'  _,        ..,-.    \`.
.  '         .-f    ,'   `    '.       \__.---'     _   .'   '     \ \\
' /          `.'    l     .' /          \..      ,_|/   `.  ,'`     L`
|'      _.-""` `.    \ _,'  `            \ `.___`.'"`-.  , |   |    | \\
||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|
||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||
|| '              V      / /           `   | `   ,'   ,' '.    !  `. ||
||/            _,-------7 '              . |  `-'    l         /    `||
. |          ,' .-   ,' ||               | .-.        `.      .'     ||
 `'        ,'    `".'    |               |    `.        '. -.'       `'
          /      ,'      |               |,'    \-.._,.'/'
          .     /        .               .       \    .''
        .`.    |         `.             /         :_,'.'
          \ `...\   _     ,'-.        .'         /_.-'
           `-.__ `,  `'   .  _.>----''.  _  __  /
                .'        /"'          |  "'   '_
               /_|.-'\ ,".             '.'`__'-( \\
                 / ,"'"\,'               `/  `-.|" mh
""",'','')
        self.squirtle = pokemon('Squirtle', 7, 'This pokemon likes to squirt water at people that get too close', 1, ['water','water'],\
                                [1.98,0.96,1.3,1,1.28,0.86],{}, 20, 1.3,{16:'wartortle'},"""
               _,........__
            ,-'            "`-.
          ,'                   `-.
        ,'                        \\
      ,'                           .
      .'\               ,"".       `
     ._.'|             / |  `       \\
     |   |            `-.'  ||       `.
     |   |            '-._,'||       | \\
     .`.,'             `..,'.'       , |`-.
     l                       .'`.  _/  |   `.
     `-.._'-   ,          _ _'   -" \  .     `
`.""'''-.`-...,---------','         `. `....__.
.'        `"-..___      __,'\          \  \     \\
\_ .          |   `""'''    `.           . \     \\
  `.          |              `.          |  .     L
    `.        |`--...________.'.        j   |     |
      `._    .'      |          `.     .|   ,     |
         `--,\       .            `7""' |  ,      |
            ` `      `            /     |  |      |    _,-'"''`-.
             \ `.     .          /      |  '      |  ,'          `.
              \  v.__  .        '       .   \    /| /              \\
               \/    `""\""''''`.       \   \  /.''                |
                `        .        `._ ___,j.  `/ .-       ,---.     |
                ,`-.      \         ."     `.  |/        j     `    |
               /    `.     \       /         \ /         |     /    j
              |       `-.   7-.._ .          |"          '         /
              |          `./_    `|          |            .     _,'
              `.           / `----|          |-............`---'
                \          \      |          |
               ,'           )     `.         |
                7____,,..--'      /          |
                                  `---.__,--.'mh
""",'','')
        self.wartortle = pokemon('Wartortle',8, 'This pokemon likes to withdraw into it\'s shell to avoid being hit',1,['water','water'],\
                                 [2.28,1.26,1.6,1.3,1.6,1.16],{},30,1.3,{36:'blastoise'},"""
     __                                _.--'"7
    `. `--._                        ,-'_,-  ,'
     ,'  `-.`-.                   /' .'    ,|
     `.     `. `-     __...___   /  /     - j
       `.     `  `.-""        " .  /       /
         \     /                ` /       /
          \   /                         ,'
          '._'_               ,-'       |
             | \            ,|  |   ...-'
             || `         ,|_|  |   | `             _..__
            /|| |          | |  |   |  \  _,_    .-"     `-.
           | '.-'          |_|_,' __!  | /|  |  /           \\
   ,-...___ .=                  ._..'  /`.| ,`,.      _,.._ |
  |   |,.. \     '  `'        ____,  ,' `--','  |    /      |
 ,`-..'  _)  .`-..___,---'_...._/  .'      '-...'   |      /
'.__' ""'      `.,------'"'      ,/            ,     `.._.' `.
  `.             | `--........,-'.            .         \     \\
    `-.          .   '.,--""     |           ,'\        |      .
       `.       /     |          L          ,\  .       |  .,---.
         `._   '      |           \        /  .  L      | /   __ `.
            `-.       |            `._   ,    l   .    j |   '  `. .
              |       |               `"' |  .    |   /  '      .' |
              |       |                   j  |    |  /  , `.__,'   |
              `.      L                 _.   `    j ,'-'           |
               |`"---..\._______,...,--' |   |   /|'      /        j
               '       |                 |   .  / |      '        /
                .      .              ____L   \'  j    -',       /
               / `.     .          _,"     \   | /  ,-','      ,'
              /    `.  ,'`-._     /         \  i'.,'_,'      .'
             .       `.      `-..'             |_,-'      _.'
             |         `._      |            ''/      _,-'
             |            '-..._\             `__,.--'
            ,'           ,' `-.._`.            .
           `.    __      |       "'`.          |
             `-"'  `""'''            7         `.
                                    `---'--.,'"`' mh
""",'','')
        self.blastoise = pokemon('Blastoise',9, 'This pokemon can blast out water from the two cannons on it\'s back',1,['water','water'],\
                                 [2.68,1.66,2.0,1.7,2.1,1.56],{},40,1.3,{0:0},"""
                       _
            _,..-""'--' `,.-".
          ,'      __.. --',  |
        _/   _.-"' |    .' | |       ____
  ,.-""'    `-"+.._|     `.' | `-..,',--.`.
 |   ,.                      '    j 7    l \__
 |.-'                            /| |    j||  .
 `.                   |         / L`.`""','|\  \\
   `.,----..._       ,'`"'-.  ,'   \ `""'  | |  l
     Y        `-----'       v'    ,'`,.__..' |   .
      `.                   /     /   /     `.|   |
        `.                /     l   j       ,^.  |L
          `._            L       +. |._   .' \|  | \\
            .`--...__,..-'""'-._  l L  ""'    |  |  \\
          .'  ,`-......L_       \  \ \     _.'  ,'.  l
       ,-"`. / ,-.---.'  `.      \  L..--"'  _.-^.|   l
 .-"".'"`.  Y  `._'   '    `.     | | _,.--'"     |   |
  `._'   |  |,-'|      l     `.   | |"..          |   l
  ,'.    |  |`._'      |      `.  | |_,...---""'''`    L
 /   |   j _|-' `.     L       | j ,|              |   |
`--,"._,-+' /`---^..../._____,.L',' `.             |\  |
   |,'      L                   |     `-.          | \j
            .                    \       `,        |  |
             \                __`.Y._      -.     j   |
              \           _.,'       `._     \    |  j
              ,-"`-----""'''           |`.    \  7   |
             /  `.        '            |  \    \ /   |
            |     `      /             |   \    Y    |
            |      \    .             ,'    |   L_.-')
             L      `.  |            /      ]     _.-^._
              \   ,'  `-7         ,-'      / |  ,'      `-._
             _,`._       `.   _,-'        ,',^.-            `.
          ,-'     v....  _.`"',          _:'--....._______,.-'
        ._______./     /',,-'"'`'--.  ,-'  `.
                 ""'''`.,'         _\`----...' mh
                        --------""'
""",'','')
        self.caterpie = pokemon('Caterpie',10,'This pokemon eats leaves until it\'s ready to enter a cocoon',1,['bug','bug'],\
                                [2.0,0.6,0.7,0.4,0.4,0.9],{},15,1.3,{7:'metapod'},"""
                   _,........_
               _.-'    ___    `-._
            ,-'      ,'   \       `.
 _,...    ,'      ,-'     |  ,"'":`._.
/     `--+.   _,.'      _.',',|"|  ` \`
\_         `"'     _,-"'  | / `-'   l L\\
  `"---.._      ,-"       | l       | | |
      /   `.   |          ' `.     ,' ; |
     j     |   |           `._`"'"' ,'  |__
     |      `--'____          `----'    .' `.
     |    _,-"'"    `-.                 |    \\
     l   /             `.               F     l
      `./     __..._     `.           ,'      |
        |  ,-"      `.    | ._     _.'        |
        . j           \   j   /`"'"      __   |          ,"`.
         `|           | _,.__ |        ,'  `. |          |   |
          `-._       /-'     `L       .     , '          |   |
              F-...-'          `      |    , /           |   |
              |            ,----.     `...' /            |   |
              .--.        j      l        ,'             |   j
             j    L       |      |'-...--<               .  /
             `     |       . __,,_    ..  |               \/
              `-..'.._  __,-'     \  |  |/`._           ,'`
                  |   ""       .--`. `--,  ,-`..____..,'   |
                   L          /     \ _.  |   | \  .-.\    j
                  .'._        l     .\    `---' |  |  || ,'
                   .  `..____,-.._.'  `._       |  `--;"I'
                    `--"' `.            ,`-..._/__,.-1,'
                            `-.__  __,.'     ,' ,' _-'
                                 `'...___..`'--^--' mh
""",'','')
        self.metapod = pokemon('Metapod',11,'The outer shell of this pokemon is able to harden on command',1,['bug','bug'],\
                               [2.1,0.4,1.1,0.5,0.5,0.6],{},20,1.3,{10:'butterfree'},"""
                                   ,--..
                                  /     `.
                                 /|       `.
                                / |        |
                               /  j        |
                              /  |         `
                             '  ,'          \\
                           ,'                L
                          /                  +
                        .:.                   .      `
                     ,"`.  `.       ,..-._    +
                     |  |`.  L     '   _.'`.   .
                     j  `.,\ '    | ,.' |  +.  +
                    '`.    |,'    |" `""   / `, .
                   |   `""'/      `-.____.'    \|
                 ,'|     ,'                     Y
                /  |    /                      '|
               /   |  ,'                     ,' +
              /    \-'                      /    `
             /    /                       ,'      `
            .     ,`'-.                 ,'         L
             \   /     \               /            .
                /      `               \            |
              `/          _,            `          ,'
               |                         `       ,'
               |           "'             `.   ,'
               j         -"'               |`-'
              /                           /'/
             /           ,               / /
            /            '              j /
          .' ___                        '/
          |-'   `"`-.                  '/
          '          \                .'
        ,"            l          _,.-'
       ,---..         |L     _.-'
     ,'      `.      / |  ,-'
    /          `  _,'  ;-'
  ,'--.       ,-`|  ,-'
 /     L   _,'  _|-'
(       \-' _,-'
 `......^.-' mh
""",'','')
        self.butterfree = pokemon('Butterfree',12,'This pokemon can put other pokemon to sleep with the spores from it\'s wings',1,['bug','flying'],\
                                  [2.3,0.9,1.0,1.8,1.6,1.4],{},30,1.3,{0:0},"""
       ,-.                                            ___.._
 _     `. `.                                    _,-""'      ',._
`.`.      `.\                                _,'         _..-'  `.
  `._\       `.                            ,'         _,'_,.-'-.  \\
      `.       `.                        ,'        ,-',-"       \  .
        `.       \                      /  _,----"',-'           L  L
          `.      \                   ,' _.--"-.  [              |  |
            `.     .                 / ,'       | |     _..---../   |
              .     L               / /         | j ,.-'        `   |
               \    .              ' /          j ,'             |  |
                \    .            ' /          ' /               |  |
                 \   l           / /          /,'                j  '
                  L__L._        / /          +'      __,........'  j
                ,'   '  "`.    / /         .' _,.--'"           \  |
               /,""-.      `. ' '        _/.-'                  | F
              /|   / l       . /       ,'                       | |
             | |  /  |       ]'      ,'                         | |
            ,._\"'   |       |     ,'-'"'''''''''''''----.._    / |
            |  \`.._,'       F  _,'                         `--'  |
            `..'           _/ ,:_____                         L   |
              `..          .-'       `'--.._                   | j
            _,. /,---.       \              `--..              | |
           F  <j-.'   `       ._                 `"-._        j  '
           |  <|`,.    |       `L._                   `..   _, ,'
           `..<|`.___,'        |.  `-.                   Y"' _.
              `L               | `.   `-.._____________,',.-'
                `.            .Y   \      `"".""'''.  ."'
                  `.        ,' |\   `.        `+-._ \  |
                    `,--. -'   | .    `.       `   `.| |
                    /    //    |  \    ``-..___/     | |
                   j    .l     |   .    F   \   `   F  |
                   |    ||     |    `   `    .   ` ,  /
                   |    ||    F      `-.|     . _,' _'
                   |   / |    |       `._`-----'  ,'
                   |  /  |   /           `-------'
                   l /   \_,'
                    " mh
""",'','')
        self.weedle = pokemon('Weedle',13,'This pokemon gives a painful sting from the stinger on it\'s head',1,['bug','poison'],\
                              [1.9,0.7,0.6,0.4,0.4,1.0],{},15,1.3,{7:'kakuna'},"""
               ,`.
               L  \\
              ,    \\
             j      \\
             ,       \\
            j         `
            ,          .__
         ,-'Y          `  `-.
      .-'    `..___..-'      `-.
     /__           ,-.          \\
    /(__)         `   '          `.
   |               `"'             L
   `.------._                      |
 ,'          `                     |
F             |                    |
|             |                    |
`._         ,'                     j
   `+------'                      /
     \                           /                         |`._
      `.                       ,'                          |   \\
        `._                _,-'                            |    \\
           `-,.________,.-'   `.                           |     L
            /                   '                          |     |
           /             _,._   |                          ,`---,'
         ,'|            /    .  j                        .'      `.
         . L            '    | ,                      ,-'"'`-..   |
          .,\            `--' / `.               ___./       ,.' ,'
             \              ,'    \__         ,-'     "-.    | |'
              `-._______,.-'  __   | `'-._.,- ._        _`   `"Y
                |           ."  \  |     \      `.    ,'  \   ,'
                |           '    | ;      .       .   `._./.-'
                7.           `'"' / `.--. |   _.. |      j
                `.__       `   _-'   |   |j  /   ||     .'
                    `-...,_..-'      `--'/   `._, ^----'
                         .\            _'       ,'
               `         `._-.______,.'`.___,.-'mh
""",'','')
        self.kakuna = pokemon('Kakuna',14, 'This pokemon it starting to form it\'s future powerful arm stingers',1,['bug','poison'],\
                              [2.0,0.5,1.0,0.5,0.5,0.7],{},20,1.3,{10:'beedrill'},"""
           _,--'"'''''---.._
         ,'                 `._
       ,'                      `.
     ,'                          \\
    .                             \\
  ,'.                  ,-`.        \\
 /   \               ,'    ,        \\
|`.  |\            ,`      |         |
L  `.| |         .''     _,'        _'
 \    "'        ,`'_..-''        _,'
  `.            '""          _,.' `.
    /._                 _..-"       \\
   /   `.          _,.-'             \\
  /      \-.___.--'/                  \\
 |      ,/.     .-^+.._               F
  L..-''.' \  .'   |   `'--.....___   .
  /     /   `/     |               `"-;
 /     j    j      '                ,'
 `.    |    |       L          _.-'Y
  ,`._/     |        .    _,.-'     .
  `.  '|    |         \""'|         |
   |   |    |         |   |         |
   |   |    |        ,'   |         |
   |   L    +      ,'     |         |
   |    \    L    ,\      j         |
   L     \   |   /  `.   /          j
    \    j\  |  /    `. /          .
     L  .  ` | /       \          /
     +  |   `|/                  /
      \ | _,..._         \      /
       ./'      `-._      \   ,'
        l           `.     ^_/
        +             `   /
         L-""--.       .,'
         |      `.     ,
         .        \  ,'
          `       _.'
           `....-' mh
""",'','')
        self.beedrill = pokemon('Beedrill',15,'This pokemon hunts small insects and even some mammals with it\'s powerful sting',1,['bug','poison'],\
                                [2.4,1.8,0.8,0.9,1.6,1.5],{},30,1.3,{0:0},"""
                     ,--""+--.
                    /     j   /`.
                   |     /   |   `.
                   |   ,'    '     \\
                   j,-'     '`..    \\
                  +      _ /    `._/ \\
                  |     / '-.     |   .
                  |    /     |   /    |
                  |   /     j   j     |
                  |  j      |   |     |._
                  | .'     7    |     |  `.
  ___      _.._   | j      |    +     '    `.
 |.---=-.,'+-. `. |/       F     L  ,'    ,'`.
 ||,==--'|_' |  j  \      /      |,'   ,`'    L
 'Y'   | |  '/ ',.-.\    j     ,,^  _,' \     |
`.||   |  `.'  '    `.   / _,-'   `'     L   F
  ||   `     .  ,-.   `,--'              |   |
  `'    `.  /_,' ,'     `--------------""'''Y
         _:"'_.-'       /_>:-.__           /
      `-".`"'__,`-.,-._/      `.""`------"'
      `.| `"'      | | _.--'""'--\\
       || /        | '"  ___,.._  \\
      _|||__      / /,.-'       `- .
    ,'   `. .    /,'/'  _.,-"'"--._F
    7     | |  .',L'|_-'           |
    +     | | / / ',"'  ,.-'""'`-._|
     L    ' |. /  .-.`"'           |
     |   j j   \  `-.'\           j
     +   | | \  `.   ` `.  _.... ,
      L  | |  \   .   `  \"     /
      | ,' |   L  ,'    \ `    .
      | || |   '  |      L `   |
      `./|j     `. .     `. \ j
       |  '       ` .     | '\`
                   \ '.   | \\
                    | |  /,-'
                    j l  "
                  _/_,'
                 ',' mh
""",'','')
        self.pidgey = pokemon('Pidgey',16,'This pokemon is very common in large cities where people feed them', 1, ['normal','flying'],\
                              [1.9,0.9,0.8,0.7,0.7,1.12], {}, 20, 1.3,{16:'pidgeotto'},"""
                   .,
            , _.-','
          ""|"    `""''.,
         /'/       __.-'-"/
        ','  _,--""      '-._
    _...`...'.""''''.\""-----'
 ,-'          `-.) /  `.  \\
+---."-.    |     `.    .  \\
     \  `.  |       \   |   L
      `v  ,-j        , .'   |
     .'\,' /        /,'      -._
    ,____.'        .            `-.
        |         /                `-.
       /          `.                  `-.
      /             `. |                 `.                  _.
     .                `|                 ,-.             _.-" .
    j                  |                 |  \         _.'    /
    .                  |               .'    \     ,-'      /
    |                  |            ,-.\      \  ,'      _.-
    |                . '  `.       |   `      `v'  _,.-"/
    ||    \          |  ` |(`'-`.,.j         \ `.-'----+---.
    |'|   |L    \  | |   `|   \'              L \___      /
    ' L   |`     L | |     `.                 | j   `"'"-'
       `-'||\    | ||j       `.       ._    ` '.
          `\ '"`^"- '          `.       \    |/|
            `._                  `-.     \   Y |
    __,..-""`..`._                  `-._  `\ `.|
   +.....>+----.' ""----.........,--"'" `--.'.'
       ,' _\  ,..--.-"' __>---'  |
      --""  "'  _." }<""          `---""`._
               /..."  L__.+--   _,......'..'
                 /.-""'/   \ ,-'
                     .' ,-""'
                    /.-' mh
""",'','')
        self.pidgeotto = pokemon('Pidgeotto',17,'This pokemon can produce powerful gusts to blow away it\'s opponents',1,['normal','flying'],\
                                 [2.36,1.2,1.1,1,1,1.42],{},27,1.3,{25:'pidgeot'},"""
                        |
                   ____ A,
               _,-'\  || /`'`.
              /-.   '.'|    ,'-.
            .'   `. |/j | ,'    ..
           .""|._  \` | ,'  _.,\--.
           '/ |  |"\\,| |,"| |  |  \\
           |.'_..|().\../()|_/\ |\ |'
           | |     ,'   `    L \| Y
           | '    /.-""-.`    |||  \\
           . |   |_,-----.|   j||  `
           | .   . .     ,'  /,'/
         __|  \   \ \__,'/  // j
     _,'" ,'   `._ `.__.'  ,'  |---._
   ,'    .        `"----""'    .     `.
  ,     .                       `      `
 /     /    ,-""''''''''''`--._  \      '
 |    j   ,'                   `. `     |
|'.'  |  /                       `.|    |
| `.  /.'                          \  | |
L  `'v'/                            . |,|
 \   '|                             | ' f
      |                             ./ /
  `   '                             j /
   `  `                            / /
    `. .                          / /
      `.`.                       /,'
         \`.                   ,',
          . `                 .-
           `.  +.       _,.- ,'
            |`-| `"--""' `,'-|
           ,'  | _      _ |  |
   ,--...-'    `' |> <("     |-..__,..
 ,'    _.+- ,  +..'    `-.  .  `.___  '
`-""--:-' ,' |  `.       |   `..   .||_\\
     /"|_'   `.,-|       | _.|  `-.'_\ `
     .'        | |        ` ||
                '          V' mh
""",'','')
        self.pidgeot = pokemon('Pidgeot',18,'This pokemon has a long feather on it\'s head which it uses to attract a mate',1,['normal','flying'],\
                               [2.76,1.6,1.5,1.4,1.4,2.02],{},35,1.3,{0:0},"""
                   ..-`"-._
                 ,'      ,'`.
               ,f \   . / ,-'-.
              '  `. | |  , ,'`|
             `.-.  \| | ,.' ,-.\\
              /| |. ` | /.'"||Y .
             . |_|U_\.|//_U_||. |
             | j    /   .    \ |'
              L    /     \    .j`
               .  `"`._,--|  //  \\
               j   `.   ,'  , \   L
          ____/      `"'     \ L  |
       ,-'   ,'               \|'-+.
      /    ,'                  .    \
     /    /                     `    `.
    . |  j                       \     \\
    |F   |                        '   \ .
    ||  F                         |   |\|
    ||  |                         |   | |
    ||  |                         |   | |
    `.._L                         |  ,' '
     .   |                        |,| ,'
      `  |                    '|||  j/
       `.'    .             ,'   /  '
         \\    `._        ,'    / ,'
          .\         ._ ,'     /,'
            .  ,   .'| \  (   //
            j_|'_,'  |  ._'` / `.
           ' |  |    |   |  Y    `.
    ,.__  `; |  |-"'"^"'"'  |.--""`
 ,--\   "'" ,    \  / \ ,-     "''"---.
'.--`v.=:.-'  .  L."`"'"\   ,  `.,.._ /`.
     .L    j-"`.   `\    j  |`.  "'--""`-'
     / |_,'    L ,-.|   (/`.)  `-\.-'\
    `-""        `. |     l /     `-"`-'
                  `      `- mh
""",'','')
        self.ratata = pokemon('Ratata',19,'This pokemon has strong teeth, it has been known to chew through metal!', 1, ['normal','normal'],\
                              [1.7,1.12,0.7,0.5,0.7,1.44],{}, 20, 1.3, {12:'raticate'},"""
                                      ,'""`--.
                                     |     __ `-.
                                     |    /  `.  `.
                                      \        ,   `.
                                       `.      \_    `.
                                         `.    | `.    \\
                                           `--"    `.   `
                                                     `.  `
                 ,.._                                  \  `
               /_,.  `.                                 \  `
              j/   .   \                  ___            \  \\
              |    |   `____         _,--'   `.           .  L
               L  /`--"'    `'--._ ,'   ,-`'\ |            . |
                |-                /  ,''     ||            | |
     -v._      /                   ,'        ||            | |
       `.`-._,'               _     \        |j    _,...   | |
         `,.'             _,-. \     |      /,---""     `- | |
        .'              ,".   ||     `..___/,'            `' |
        |   ,         _/`-'  /,'                            `|
        |-.__.-'"''""' ""''''''--`_,...-----''''--...--      `.
         `.____,..              ""   __,..---""'              |
          |       `              --"'.                        `
          |     ,' `._                \'                       `
          | |  .^.    `.             /                          `.
         ,'_]__|  \   / `.          /          /____._            `._
       ,'          \ j    '        /          /       `.             `.
 ___,.' `._       __L/    |     __'          /     _, / \             |
`-._       L,.-""'  .    ,' _.-','          /-----'-./   `--.         |
   '   / ,'         '..'"_,'    /         F /  ."'_,'        |.__     '
  / ,.\,'              ""      /         / (,'\ .'        ,.-"'  `.  j
  -'   '                      /        ,'     `"         / __/' .- ,'
                           __.'"`.    /                 `-' | _,L,'
                         .',      `""'                      '/,--
                          / _..' _,,'
                          ,' `-"' mh
""",'','')
        self.raticate = pokemon('Raticate',20, 'This pokemon digs deep burrows which can sometimes cause damage to buildings',1,['normal','normal'],\
                                [2.2,1.62,1.2,1,1.4,1.94],{},25,1.3,{0:0},"""
                        |.     .|
                      `.  `._.' |,'Y'     _.......
      +--------..  _\"'  "'""'"'--.=-_ ,-'  ,.-- '     .
       |  '""`.  `.`-._           .-" |   .'    (      |`
       j       \  |..'-- ,-----. ,.]..|  /       `.    L .
  ____(___     |      _.' -  , `--..    | __.....-/-..__|L
.'._______""'"----  ,'   _____._    ` ,-':,...------""'"i .
         |""'"-.  -'    '.     /`    ' -------.j__      | |
     .,--------        / \    j  L      `=..-""----'    | |
           ,-_,.-     j   L | |   .     `-..:-.__       | |
        ,++-.  |      |   /-+-|   |       | `"-._`._    | |
      .+"" '- .'      L  j  | L   j       | L    `-.`.  F-|
    ,'    .-) `,       \_/     \ /        j  \       ` /-.|
   '        |  .        `.......-        /   j_       j  j
         .--|  ,\_                      ,'". / )     ,^-.|
          `.`,-                        /  / / ,`._  ,.   F
       "'"| '  .'`.'                   `-'\ "'  \ \,  \ /
      | j`.    |     . ,. .,..  ,_  .     `...-.| |.  ,'
      `-'  /""/    ,' .' \ '  `/. `-       Y   |`"  `/
          j  /'                             .  | \ ,'
           \ \                              |  | ,'
           ' '                              j j-'
            `.\                            ,.'
            _+.`.                       _.,---.._    _
   ,-""--.,'   `--.._              ,::`"-        '""' -.
 .'  _..--          ,`"`--------""'  `._    ....<""`-",.'
 `-"'   _,-""'  _,-'                    `-..__   v._  `.
   / ,-'/  _,-`'                              `-. \ `-.|
   -'  |_,'                                      "' mh
""",'','')
        self.spearow = pokemon('Spearow',21,'This pokemon eats bugs with it\'s powerful peck', 1,['normal','flying'],\
                               [1.9,1.2,0.6,0.62,0.62,1.4],{},20,1.3,{20:'fearow'},"""
               _,
             .'.'  _.
           ,' ._,-'_"'
        _,'   '  ------""'`._
      ,'                 _,.--"'              ___        __,..
      |    _,..       ,-'             _,.--""'   7_,.--"'    ,'
      j. .'D  |       |            ,'"       _.-'       _.-""'.  _,..-"'
 ,---'  `+----'       |`._      _.'         '                '.-'      /
j         `.       ,-'    `'--,"                           ,'       ,-'
|    __    |      '-.._,    .'                           ,'     ,.-'
`. ,' ('T--'        ."     /                          _.'  _,--"
  `   `,  /         _`.   j                         _', ,-"__,..,-.
      `-"`.        \   `-.|                        _,'"'""'       l
           `.,      \     L                     _.'      __,...--'
            ` '-    .`     `._             _,.-' ,--'""'"
             '  \`.,\         `+------,--"'     /
                 \ )`'      ,-'      /         /
                  `     _,-'       ,'         /
                   `+""'         ,'     ,.  ,'
                     `.        ,'     ,'   .
                       `-._.,-'      /. _.,j
                           ""`-----.'  '  /
                                / /   /  /
                    _.......__,' /__,' ,'
                  ,\  ,--..--------"_  ...._
                 '--"(_,`|  ,..-' _,....__  |.
                        '-./...-'"        `""'- mh
""",'','')
        self.fearow = pokemon('Fearow',22,'Because of it\'s majestic wingspan, this pokemon is often confused for one of the legendary birds',1,['normal','flying'],\
                              [2.4,1.8,1.3,1.22,1.22,2],{},30,1.3,{0:0},"""
    ,---...__     ,.._
  ."'"_...   ""---\.,_`"-._                    __,..._
 ,--   "''''":--..    "-   `-._ _,.        ,-"" ..----'"'",
`---........_____ ._     `-._  `. |       / /'      '""'"-----.
\"'"''""''"'"'"-`           `-. `.      / j     .\ |\   -.,:,- .
 `-.......___     `._           \  \    ]\ |   . |L ||/\   `. ` .`.
         __,..==--'/ '           \  L  A|,'|    \| |||||  ` .`.. -._
    .--""          `.             L | j  /'"-.__\V '/|||   | `. `._ `.
      `....----_..-`"`/.          | | | j   __ `._   | |'_`.\  `.  `. |
            -"'       \           | `_|.   l  `.  `.   |||   ` | `   \'
            `-._,...-""\-         |        |    .   /`.  \  ..Y   `.  \
               `-..,'  .`         '         L \  .  `--"`.`.`|  .   \  |
                  \  ,'  `|     ,'          .\ +-'-...-^._`. | |..  ,\ '
                   `\     `.._ j             /"       \  |\ `..- `.'- `
                    `. ,' | .  |           .'          \ | `._`.
                      +   | | j           /             `'    `.`.
                       `.+._j_'      __..)                      `..
                        _,-'   .,   j ` .'""`--.                  `
                     _.' .-'  /,'`"-.  ,` .\ \` `
                   ,'  .' / /`,'    ||'` ,'`T|.`-|
                 ___,'/_,._/        L|   . |'-'\"
                                    `-   ||    ' mh
""",'','')
        self.ekans = pokemon('Ekans',23,'This pokemon will hide in piles of leaves to ambush it\'s prey',1,['poison','poison'],\
                             [1.8,1.2,0.88,0.8,1.08,1.1],{},25,1.3,{22:'arbok'},"""
        _,--""'"'"-.
      ,'   .,-.     `.
     '`...( |  |      \\
    |      `--'        .
    '_,...__,'          `
     `._                 `
        `..______         |
             |.          ,|
             | `-.....,-" |
             |            j
             ^.         _F
            /  `-.....-'/
           /          ,'
          /          /
         /          /
        j       _.-- .
        |      /     ,+---....___
        L     /     /            ""`-.._
         \   j     j                    `-.
          `. |     |            .'         `
            `+...__|__       .,+-..         |
                      ""`._.l      `.       j
                      ,.-"   "-.     L    ,'
                    ,'          L    : _.'
                   /            |   _:'
                  .            .|,-'
                   .            `.._
   '\               `-.             `"-.
 ,`.'                  `-.              L
 |  )                     `-. _...__     |
.'-'                         )      `.   j
|  |_                      _,'""`.    \ /
 .-' `+._               _,"       `.  |/
  \   |  "`,,,,,....---'           | .'
   `-.'   /                        |+
      `--+                     _.-'
          `--.___       __.---'
                 `""'''" mh
""",'','')
        self.arbok = pokemon('Arbok',24,'This pokemon has been known to hypnotize those who stare into it\'s eyes for too long',1,['poison','poison'],\
                             [2.3,1.9,1.38,1.3,1.58,1.6],{},30,1.3,{0:0},"""
                   _,.----'"'"'---..._
              _,-'"                   `-..
           _,'                            `-.
         ,'                                  `-.
       ,'                                _,..._ `.
      /                               ,."     `:- L
    ,'                             |.'         / ||
   /            _,.-._             L        .-' -,'
  /        _,.-"      `.            `     __   .'
 j      _,"           ||\|           `. ,-  _.'
.     ,' `-..________.-' |            |' ,-'
|   .' `--,.___       _,'| /`.        ` '
|   |     `._  '""'""'   . `_Y.        Y_
`._          `-...__      `.`-'        | `-,...___
   ``-,.._          `""--.._`.         |  /     _,+`-._
    .'    '--._             `-+      _ |./    ,"       \
   ,  _,...._  `..             `-.:L_,v-'"`-./_____     L
  .,-"       `-.| `,                )/       \     "`   |
  j             |  \`\       _,......|       |       `  |
  |       _,.---^.v[\_   _,-'        |       |        \ '
  |     ,"       _>.. "'"            |       |        _V
  '    .        /  |'`\              |.._   ,'     _,'
   .  j       ,'    |  `._           |   `""-----"'
    \ |      j      '     `--..,,,..j
     Y       |       \             /
      `.     |        \           /
        `.   `         `.      _,'
          `._ `.         `--..'
             `---...,,,...-"' mh
""",'','')
        self.pikachu = pokemon('Pikachu',25,'This pokemon stores electricity in it\'s cheeks',1,['electric','electric'],\
                               [1.8,1.1,0.8,1.0,1.0,1.8],{},25,1.3,{0:0},"""
                                             ,-.
                                          _.|  '
                                        .'  | /
                                      ,'    |'
                                     /      /
                       _..----""---.'      /
 _.....---------...,-""                  ,'
 `-._  \                                /
     `-.+_            __           ,--. .
          `-.._     .:  ).        (`--"| \\
               7    | `" |         `...'  \\
               |     `--'     '+"        ,". ,""-
               |   _...        .____     | |/    '
          _.   |  .    `.  '--"   /      `./     j
         \' `-.|  '     |   `.   /        /     /
         '     `-. `---"      `-"        /     /
          \       `.                  _,'     /
           \        `                        .
            \                                j
             \                              /
              `.                           .
                +                          \\
                |                           L
                |                           |
                |  _ /,                     |
                | | L)'..                   |
                | .    | `                  |
                '  \'   L                   '
                 \  \   |                  j
                  `. `__'                 /
                _,.--.---........__      /
               ---.,'---`         |   -j"
                .-'  '....__      L    |
              ""--..    _,-'       \ l||
                  ,-'  .....------. `||'
               _,'                /
             ,'                  /
            '---------+-        /
                     /         /
                   .'         /
                 .'          /
               ,'           /
             _'....----""'"" mh
""",'','')
        self.raichu = pokemon('Raichu',26,'This pokemon uses it\'s large tail as ground when releasing large amounts of electricity',1,['electric','electric'],\
                              [2.3,1.8,1.1,1.8,1.6,2.2],{},30,1.3,{0:0},"""
                                        _,--""`---...__
                            _.---"'""`-'.   .-"'"'`-.._`-._
                _,.-----.,-"         .". `-.           "---`.
             _,' _,.-..,'__          `.'  ,-`...._      ,""''`-.
           ,' ,-'     / (  .   ,-.       |    `.  `-._  .       `.
         ,',-"       /   `"    `"'       '      .    _`. \\
       ,','       ,-'7--.                 `.__."|   ( ` `j
      '.:--.    ,'   |   .       |\             '    `--'
     /.     | ,'     |   |       `'            .
    '       |',".    |._,'                     `      _.--""'""-._
'.          `-..'    `.                      ,  \  ,-' _.-""'""-. `.
` `                   F  -.                 /    ,' .-'          `  `
 \ `                 j     `.              ,-.   . /               . `
    `.               |     .-`.           .  '-.  V                 . `
  `   `.      .      | .    \  \         j      \/|                  ' .
   .    `.    |`.    |-.`._/`   .        |    ,'  A                  | |
    \     `. F   \   |--`  "._  |        `-.-"   / .                 | |
     \      -'    `. |        `"'                  |                 F '
      \             `+`.                           |                / .
       \              .-`                     .    j               / ,
        \              \   `.               .'    /               ' .
         \       |`._   \    `-.._        ,'    ,'              ,'.'
          '      |   `.  `.       `<`""'"'    .'             _,'.'
           `     |     `-. `._      )   `.     .          _.'_.'
            `    |        `--/     /`-._  .     `.___..--'_."
             `   |          /     /._   `""`.     `. _,.-"
              `  |         /     /   `--.....`.     `._
               ` |       ,'     /              ."'""'  `.
                `'      , `-..,7                `    . `.`.
                       .       '                 `.   \  `v
                      j.  ,   /                    `.._L_.'
                      || .   /
                      `"-'__/ mh
""",'','')
        self.sandshrew = pokemon('Sandshrew',27,'This pokemon can curl into a ball when threatened',1,['ground','ground'],\
                                 [2.1,1.5,1.7,0.4,0.6,0.8],{},25,1.3,{22:'sandslash'},"""
          _...-----'`._
      _,-'   _`. ."". \`._
    ,'    ,-'   ` ` |  \/--.
  ,:_  ,-'       ` `|  |`.  `.
 /   `'-..        `  .-'  `   \\
j         `.--,    \       `   :
|         '--' |    \       `._'-.
|___     |     |     L      .'    `.
|   `-. /|___.' `.   |    .'.       .
|     ,'          .  j.  /   `.      \\
.  _,'            |,'  `.      \   ,<`.
 .'             _.-      `      j.'  \ \\                          ,.
  `       ,v-""'   \      )__,+'      . \                       ,' |
   `.    / |  /  _,'`.  ,'  \  \       /`.                   _.:   |
     `,-'-`  / ,'     \'    j,  \   ,.'   L               ,-'   . F
     / ,. | / .        \  .'     \.-\     |         _,.-"`.     `,'
     (_\/|'|   \        .'   _,-"    `    +....---+'       `     '
     . \ |.     \    ,.^---`<_        | ,'||       \        \   /
      `.'| \_    :v-'         `.      |-  | \ __..--\     _,'\,'
        `'/`----'/              '.  ,'    |  Y       L_,-'  ,'
          \     /            ___,.'\     j   |       |    .'
           \   ."`",""'"'"'"`     | .   .'   |       |  ,'
            \  |   |         |    | | .' j,.-|       j-'
             `. ___|________/.....|_Y'  /    |   _.-'
          __,-' \                 |    /    _j,-'
         '--.    .                `...+---""
        `_____\  _`..__    __,..-"'
              .-'_|._  `"'"       \\
             , -'    .          __/
             "------------""''"" mh
""",'','')
        self.sandslash = pokemon('Sandslash',28,'This pokemon has powerful claws that can cut through rock',1,['ground','ground'],\
                                 [2.6, 2.0, 2.2, 0.9, 1.1, 1.3],{},30,1.3,{0:0},"""
                    ,\\
                _,-'.+..----"/_____
             _,'---,        /      `"",
           .'    ,'  __..../_     _,-'
          /    ,' ,-"       ,'---+--...__
        ,'   ----'        ,'             `"
       '                ,'     ______  ,-"`-._
      /  ,+""',   ....-^--..<""      ``-._    `-.
    ,' .'-'  /      |        `._          `-.   _`-
   /    `""''       `           `.           `,"
  |                  `.           `.      ,-'"--.
  '               ,-   `._ ,-""'`.__:---""'-._   `._
   `-----..__  _,'     .-".       `._         `.    `.
   /________.'"/      /  j         | `-._       `.    `.
\`-.`.__    )_/__    ._,-|         |     `.       `.""''
 .      `""'"j   `""`'   |         |       `.       `.
 \`._       /            L         '         `.....---
  `  `..___'              \      ,"            .   `.
   `.     `              _.\ _.-" `-._          `.   `.
     `-._  \         _,-"-. '|        .`-.-""'"``\     `.
         `"-^'   _.-'        |         \  `.      `---...-
              \."            |          L   `.     `.
              /              `          |     \      `.
             j                `.        |      `,....__`
             |                  \       |       `   \
              .                  .      F        \   `.
      _,...,---`.                 `.   j `.       L--..`
    ,",.--"'-.   -.                _`. |   `._    .
    ,'        \_.--`._     ,----.-<.  V       `-._ ._
   /.---"".-""' )     `""''      `. `-.._         `' `._
        ,' _.-""'"`.               |     `"-..__        `-.
        '""         \         _,..-'            `""----...-'
         '-----------+---""''" mh
""",'','')
        self.nidoranF = pokemon('Nidoran F',29,'This pokemon is normally docile, but has a powerful bite if provoked',1,['poison','poison'],\
                                [2.2,0.94,1.04,0.8,0.8,0.82],{},20,1.3,{16:'nidorina'},"""
        .'-.                            ,.. _,._
  ,--"".`.  `.                        ,'  /'    `-.._
  \__   `-`   \                     ,'  ,' _____     `-.
     | ,-.._   \                  ,'    _,'     \   ___.'
     j |    `   L               .'    ,'        |  |
    . j      \  |              /    ,'  ___     |  |
    | |  .""'|  `    _,.--....'|   /-'""   `.   |  '
    |j  j    `   `-""          '  '         |   | F
    ||  |    ,'                   `         |   | |
    |`. |   /      ,"".       .    \        |   ' |
    `  `.  /,\     |   \     / `    \       |,-' F
     `.  `/ | \    '    .   /.  |    \   _,-   ,-'
       `-. j  |\       "   /.|  |     `""__..-'
        .' |_ |(`        ,' )|__'      `._____
.-------'.   `-'-`       `--""      ""'""__..-'
 ""''""--.                           "'"(
     ___.'        .                 -----..._
   ."____..       '   -'              ""`----`_
          `.     . _._   _,             ,. `./ |
            >     `.  ."".              \ |  \ j
           j       `.,'  /               "'   Y
          /          `..'                     |
                                              |
         .                             ,"-.   |
         |                             |   \  |
         |                             .   /  |
         |                              `-'   |
         |   `.                           ,   '
         L     \                      _  /   /.
          \     \             |      ( `/  .'  `.
           L     `.           |       "/ _/    _|
         _,|       -,_        |       j-'_._  ,  `.
        '..|       (_.'--.._  L       |-+_  ..`.,.`
           |      j         "" .    __|   `"'
           |,..__<             |"`,"  \\
           | _,x..)            '-' --.'
            " mh
""",'','')
        self.nidorina = pokemon('Nidorina',30,'This pokemon has smaller horns than the male, prefering to claw and bite',1,['poison','poison'],\
                                [2.5,1.24,1.34,1.1,1.1,1.12],{},27,1.3,{0:0},"""
                           _            _
                          / )  _  _,.-"" )
                        ,' /..' /"   _,+'--"`.
                       /     / j_.-"'     ,-"
                     ,'    ,'       _____  `
                   _+__   .     _.-'     \  `...._
              ,'""'    ""/  _.-'          .       \\
            ,'          '  ',--'""`-.      L   ,-"
          ."              .'         \     |  /
        ,' _                          \    | j      _
       / ,'   _,+-'                 _,'   ,' /_,.-"" |
    _.' '  .+'.  \               ,-"___.."  -'      ,'
 ,-"     ,'-' |  |           .,-""''___,..-'       /
j        `""'"---'             '"'""       ._    , _.--".
\   ,                                        `- ' `._  ,'
 \                            _.-'            ."`.   `-. ____...----""`
  `.-"-._,..---+ +          ,'       `         `.'      `.             |
      `.        \/        ,'          |            ,.---. \           .
        `._               +__,...__   |     ,     |     |  L        .'
           `--...-""`-._   /       `,"    ,'      `     |  |      ,'
                     /  `./        /    ,'         \    j  '    .'
                    /    j        /    .       _    `._'     ,-'
                   j     '       /     |     ." `         ,-'
                   |, .<(       '      `      \_/       ,'
                   |-...+.___,./`.______\             ,'
                   `.'`.' \/  V /_/.___  `.  _     _,'
                                `....\_`,-",' |,-./
                                        `""..-'---` mh
""",'','')
        self.nidoqueen = pokemon('Nidoqueen',31,'This pokemon can use powerful stomps to cause earthquakes',1,['ground','poison'],\
                                 [2.9,1.84,1.74,1.5,1.7,1.52],{},35,1.3,{0:0},"""
                                          ."
                                        ,'  |
                                      _,... '.___
                             +--._  ,'.-"+.      "`-.
                         _,---\   `" / |p|.'     "'   \\
                       ,- _.---".   |_,'      ,-""'"-._|
                     ,' ,.'    .'          ,-'        ,'
                   ,' ,' |    .          .^---._      |
            |. _  `. /   .    |   ,---.+'       `.    |
           ,| | `/\|.    `    |  .      `-.       .  /
       .---. "`-`.,\ \    `-.,'  |         `-._   | '
        `.-'        , ""'"--'..-  \            `--'.L
          .          |`.     `     `._             _,'   .
           `.        |  `.    |_,..   `-..______.-'  _,-| |. ,"\\
             -.     /     +--'/    `.            -,"'   `"  ".-'
               `-+-'      |  /       `.        '\ |           .L_
           -"--.,-`._..._,' j          `.     / | '           (_,'
          `.    j.-'     `- |            \   j  |  `.  _...___'
            `. /__ ,...._  \|             |  |  |...-`"
              j|  `      ,-/`.           /   `  ;.._
          ,-. ||   |""-.'  |  `..__,...-'     \'    `.
          `   |/`--    .  /|                  /----.__\\
           \  .         `' /                 /         \\
            . |           ,`.              ,'     ___..+--.
            +-|          /   `-..______..-"     ,"  `.   /___
          ,'  |         j               .'    ,'      `"|    /
       ,-+    .         |`._          ,+_    /          `-..'
   _.-'  |     `.      /    ``-----:='   `.,'         _,..'
,-'      L       `-.--'         ,,'        |       ,-'
\_        \         `._    _,.-'           `.___..'
  `.._     `._      __.+'"'
      `---... +---"" mh
""",'','')
        self.nidoranM = pokemon('Nidoran M',32,'This pokemon uses the horn on it\'s head to fend of predators and attract mates',1,['poison','poison'],\
                                [2.02,1.14,0.8,0.8,0.8,1],{},20,1.3,{16:'nidorino'},"""
                  ."\                            _
                  | |  ,.                    _,-" /
                  j `-' /                 _.'   /..
                ,'     |                ,'   _..  |
               /       `.          ."','  ,-'   \ `...
             .'          \       ,' ,' ,-'      |   _/
            /             \     /    ,'         |  |
           /               `.  /    /           |  '
          |                  `/    /            | `.
       .-.`                  /   ,'            j   |        _
       \                   /V   /              |  ,'     ,-' |
        .                _/    /               | /    ,-'   /
        |               |    ,'               j / _.-'    ,'
        |               |   /                 ' ""       /
     `"--               |  /                  |        ,'  _,..-.
      \                 | j                  .'       ---"'     /
       \               j  |                  /                ,'
        \       __...--.  |                 /_..-----.       /
         \   ,""       |  |   _.           /        /      ,'
          . /          |  |  /  |        ,'        /      /
           Y           |  |.'   F    _,-'         /__,._ `.......
        _,'               '    / _.+'   ,-""-.        .'       ,'
    _.-'                      `-'| |   ,      .       -._   ,-'
_.-'                  ."\        | |    ._   ,'         / .'
 `""'---...._        /D  |       | |      ""' .     __  `--.
       / |  ,      ,`  `-|       ` |  /`    ,'    /"  \     `.
      .  `_/      /  `-..|         |  .'   /      `.  |       \\
      `          '-......'         |      .         `-'        L
       \                          ,'     j                     |
        `                      _.'       |                    .-.
        /    ,            _,.-'          |                    '  \\
       j._            ,-+'             __|                  ,^.   \\
      | | `+""-.....,' .'           ,-'   `._           _.-'""'`""
      |,|  _`. |     ,+          _,'         `"-------"'
      '  ""   "     | ,""-.   _,'
                    |,` _.+--'
                    ' "' mh
""",'','')
        self.nidorino = pokemon('Nidorino', 33, 'This pokemon is very aggressive, using it\'s poisonous horn to attack',1,['poison','poison'],\
                                [2.32,1.44,1.14,1.1,1.1,1.3],{},27,1.3,{0:0},"""
    `._
     \ `.
      \  `.
       .   `.
       j     :-----+...-.
       /  _,'   /""_     `.     _,..._
     ,'  '      .-"c|"`+- -+--"'      `-.._
   ,'            ""'+_ |       _,--""--.._ `---..
  '     _             "'      '\          `--._  `.
 |    -'                      _.'              `-. `.
 (     __   ,.----.._        \``-.                |  `._
  `.  /_ ""'   ___.| ,.      j  `.`.   ,          `.    `.
    `'| |    ,'    '.'/'""'"'   j`. \,'|  _________||""`-'`.
      `_.\   j       j      __-'|_/'"._:."  __       .    "
          | /        /      \ `/        |`.   .   ..._`.
          ||        /       | /         | |    :.'    -/
          |'    _,-'        |.`.       ,' |   | |\_
    _     | `--'     _,-    . `.`--- ,'   /   |  .\`-..
    |`v,-'""''`-.,.-'        `._``--'  _,'    |  | \  ,'
,--'`- _       \ \              '""''`'       `_,'  +-
 -.'    \       . |                        /`     ,---.
 -`\    |       | L                        `-'     '""'`\
 '---...:_      / \                          |   ,.-""'.|
          '---+'   \                         ' ,'       `
               '`''".                       / /          `.
                     \                     j |            '.
                      `.                   | |              \\
                        \ _                |/             /\|
                         / "-   --""----+--'             / ||
                        `v'""'""-..     |      `..__.,.-'-.,,
                         |         `-.,'           .`.J     /
                         |            |             '---...'
                         |     .     /
                         |    | `,  j
                        ..--+'"--_  /
                         `-.|     \'
                             `----' mh
""",'','')
        self.nidoking = pokemon('Nidoking', 34, 'This powerful pokemon controls a large territory which it defends from other Nidokings',1,['ground','poison'],\
                                [2.72,2.04,1.54,1.7,1.5,1.7],{},35,1.3,{0:0},"""
                  _.___.._              ,'            ,. ____
                   \      '-.._      |: | '       __,- _ ... )
                   j-"'"|"`-._ `.'.  | \| |    ,"'_,--.     `.
                  |     |     `. `.\-' j   .-.'  '     `.    |
     _.           `     |       \  "  /    \   .'       |    |
    /  |           \    L       j           )   \       j   j
   /   |            \    `.   ,'_ ..   .__,. ,   `     /   ,'
  /   j              `-._  `./  /`. \       / /"| \ .-'  ,'
 .  ,.|                _`+..    |.)`       ' (| |  ``._.'
 |-'  |              ,'    /,     "`'       '--"   |   '`.
j     |             '        \ './.             |\-'      `
|     |            |          \  `/, . . . _-|./ |        _\\
| ,-"".            `-""-.     |`-._`| \--|'/|, ,,'    _.-' /
|/     \        __(      \   ,+..._`---...-'_.--"". .'     \\
|       `   ,-"'   `._   | _.      `"-....-'       `.    ,.---.
|    ,-'"  '"'\       L,-|'            `v           |  ,'      `
L   /    ."`--'       |  |              |           |||         `'
 | /     `..        ,.|  |.             |          ,' '|       ."".\\
 `'      | /        . `. | `.       _,--+--._    ,',-''|        `-'|
  `     .,"`. ,..  / `  `|   `-...-'         `"-' / ,.-\         /"".
   \   j    |`. |.-   `/. `.     __.-----...__   ,`/    `.___    \  |
    .  |    |  \|      | \\ `- -'             `.. |       |  `,"" `.'
     ` |   j .         | | \                   |  |       |,-| \\
      `'   | ".      ,-' `. L                  .-' `        ,'  |
        `. |   \    /     .'`.               ,'     `      /    |
          `.    `""'      /   `-._       __.' .'\    `....'    /
           ,'             \ _____ `""''""  _.'  /             '
           ' ,--'""`--.___,'     ""------''    '_    _,...__ /`.
            `-........'                          `-.'       `,"
                                                     `"'"---' mh
""",'','')
        self.clefairy = pokemon('Clefairy',35,'Some people say that this pokemon came from the moon.',1,['normal','normal'],\
                               [2.5,0.9,0.96,1.2,1.3,0.7],{},20,1.3,{0:0},"""
                    __.._
                ,--'     "`-._    _,.-,--------.
    ________ ,-'              `-"'   /     _.-'|
 ,-'  '     :                       .    ,'    '
|    '     j      _.._              |  ,'     j
L   /      |    .'    `.            |.'      /
 \ j       |    `.,'   |           ,'       /    _
  .|      ,'\         /           '.___    / _.-" |
   `    .'   `-.....-'                 `- +-'    /
    `. ,'                                `.     <__
      `.             .\ \                 |   ___ ,'
      |     | #      || |                  ,""   "`.
      |     | #      `'_/                   .       `.
     ,'     `.         ,-"".                L         `.
    /     (__)       _  ""'                  :""-.      .
   /             \"''|         |/            |    \     |
  .               \  |         |           | |     |    |
  |     _          `-'        j           /  |     '    |
  L      `.                   |          /   |   ,'     '
   \       `.                ,'         /    |_,'      /
    `.   ,.<'                `+--.    ,'     /       ,'
      `./`._'                 '_.`._,'      j      _,
        /"'                      "          |   _,'
       /   `._              .              '..-'
      j       `-._           `            /
      |        _,'`"--........+.         /
      ,"-.._,-'                 `.  .-._/
      '---'                       `+__,' mh
""",'','')
        self.clefable = pokemon('Clefable',36,'This pokemon tries to always avoid being see.',1,['normal','normal'],\
                               [3,1.4,1.46,1.9,1.8,1.2],{},30,1.3,{0:0},"""
                                       __,......._
    _............___          ____....<__         `"._
   '._      `",     `'--._,.-'   ___     `"-.    ___..>---,---------..
 ____ -.,..--"            `-  ,-'   `       .`-"'       .'_         ,-'
'._  ""'-.                  .'     _.._                    `-._ ,.-'
   `-._   `._              .     ,'    `.                    ,-'----.._
       _>.   -.            `     |      |                _,-'          )
,..--""`--""'""`-.          \    `-.    |             ,.+.__   _,;---""
\_ |              `.         `.       _.'         _,-`      `""   `.
  "\                `       / _`"----'           '                 /-.
   `.____                  |  #      #' \                         `,..'
       ,-"--...__          `--        --'                   ___,..'
      '-.---"'  |           -.,........,            ,.---""' .
                |            |        \'             \""--..._`
                |             \       /              |
                .              `.    /               |
                 ,               `--'                j
                j \                                 /
                |  .                               '`.
                 L._`.                           .' ,|
                 |  `.:-._                    _,' ,' |
                 `.,'| ""'`.__            _,< _..-   '
                     `...-'   `----------'   `-.__|`' mh
""",'','')
        self.vulpix = pokemon('Vulpix',37,'This pokemon is always keeping it\'s many tails moving to distract opponents.',1,['fire','fire'],\
                               [1.86,0.82,0.8,1,1.3,1.3],{},20,1.3,{0:0},"""
               _,.+-----__,._
              /  /    ,'     `.
     ,+._   ./...\_  /   ,..   \\
     | `.`+'       `-' .' ,.|  |
     |  |( ,    ,.`,   |  `-',,........_       __......_
      \ |..`/,-'  '""'' `""'"  _,.---"-,  .-+-'      _.-""`--._
       ."|       /"\`.      ,-'       / .','      ,-'          \\
      .'-'      |`-'  |    `./       / / /       /   ,.-'       |
     j`v+"      `----"       ,'    ,'./ .'      /   |        ___|
     |                      |   _,','j  |      /    L   _.-"'    `--.
      \                     `.-'  j  |  L     F      \-'             \\
       \ .-.               ,'     |  L   .    /    ,'       __..      `
        \ `.|            _/_      '   \  |   /   ,'       ,"    `.     '
         `.             '   `-.    `.__| |  /  ,'         |            |
           `"-,.               `----'   `-.' .'   _,.--""''" --.      ,'
              |          ,.                `.  ,-'              `.  _'
             /|         /                    \'          __.._    \'
   _...--...' +,..-----'                      \-----._,-'     \    |
 ,'    |     /        \                        \      |       j    |
/| /   |    j  ,      |                         ,._   `.    -'    /
\\'   _`.__ | |      _L      |-----\            `. \    `._    _,'
 ""`"'     "`"---'""`._`-._,-'      `.              `.     `--'
                       "`--.......____:.         _  / \\
                               `-----.. `>-.....`,-'   \\
                                      `|"    `.  ` . \ |
                                        `._`..'    `-"'
                                           "' mh
""",'','')
        self.ninetales = pokemon('Ninetales',38,'This pokemon is admired in many cultures for it\'s graceful appearance',1,['fire','fire'],\
                               [2.56,1.52,1.5,1.62,2,2],{},30,1.3,{0:0},"""
        ,-""'-.._
   .---'"" ">` - `--
   `.      `-._  .`-.
     `-.       \ .` : -.
      _.>._     / ` `:..,
 ,.../...._`"-./    '.|, `
`---.._"'-.`-._    |    "'--.
       `--.\`. `._,'         `.---------------.._
            "-'--.___          \`'"-..__         `-._
                     `."`-\     ` `"--.."`-.-..__    `".
                       `.  `.     |``._ `--. `-..`"-._`.\-.
                         \   -....' `-.`-.  `-._ `-.  `-.\ `.
                          `-.__  `.`-. `. `._   `._ `-.  `.  `.
                               `-..`` `. `.  `.    `.  `-.     \\
                                   \`.` `  `.  `.    `.   `-.   `.
                                    `.`-'`.  \   .     `.    `.   \\
                                      `..  \  \   \      `.    `.,_`.
                                         \` \  .   `.     '\     `.`.`._
                                          \``.  \    \     \`.    |
                                           ' '.  \    \     \ \   L
                                             \ \  '    `    '. `.  \\
                                              ` `. \    `    '.  `. `.
                                               `. `,`.   `.   `.   `._.
                                                 `-  \._   `.  `.     "`
                                                      ` `.   `.  .
                                                          `-. ``-.:-.
                                                              -.`. '"-'
                                                                 `"-. mh
""",'','')
        self.jigglypuff = pokemon('Jigglypuff',39,'This pokemon sings a lovely song, but no one has ever heard the end of it',1,['normal','normal'],\
                               [3.4,0.9,0.4,0.9,0.5,0.4],{},20,1.3,{0:0},"""
   ,..__
  |  _  `--._                                  _.--""'`.
  |   |._    `-.        __________         _.-'    ,|' |
  |   |  `.     `-..--""_.        `""-..,-'      ,' |  |
  L   |    `.        ,-'                      _,'   |  |
   .  |     ,'     ,'            .           '.     |  |
   |  |   ,'      /               \            `.   |  |
   |  . ,'      ,'                |              \ /  j
   `   "       ,                  '               `   /
    `,         |                ,'                  '+
    /          |             _,'                     `
   /     .-""''L          ,-' \  ,-'""''`-.           `
  j    ,' ,.+--.\        '    ',' ,.,-"--._`.          \\
  |   / .'  L    `.        _.'/ .'  |      \ \          .
 j   | | `--'     |`+-----'  . j`._,'       L |         |
 |   L .          | |        | |            | |         |
 |   `\ \        / j         | |            | |         |
 |     \ `-.._,.- /           . `         .'  '         |
 l      `-..__,.-'             `.`-.....-' _.'          '
 '                               `-.....--'            j
  .                  -.....                            |
   L                  `---'                            '
    \                                                 /
     ` \                                        ,   ,'
      `.`.    |                        /      ,'   .
        . `._,                        |     ,'   .'
         `.                           `._.-'  ,-'
    _,-""'"`-,                             _,'"-.._
  ,'          `-.._                     ,-'        `.
 /             _,' `"-..___     _,..--"`.            `.
|         _,.-'            `""''         `-._          \\
`-....---'                                   `-.._      |
                                                  `--...' mh
""",'','')
        self.wigglytuff = pokemon('Wigglytuff',40,'This pokemon will inflate it\'s body allowing it to float into the air',1,['normal','normal'],\
                               [3.9,1.4,0.9,1.7,1,0.9],{},30,1.3,{0:0},"""
,-.                                                 .
.` `.                                             .'|
` `. `-._                     _,.--._            /  |
 `  ..   `.                  /       `.        ,' , '
  `  ` `.  `-._              | '".     \      /  / .
   `. `   `.   `.          ,"'---'      .   ,' ,'' |
     ` `.    `.  `.       .             |  /  / /  F
      `. .     `.  \ ,..--|             |,'  / /  /
        \ `.     .  |      \           ,.   / /  /
         `._`._   j   .----.`._     _,` | ," / ,'
            `._`"`  ,',""'"-.`.""--' ,-":+.-'.'
            ,'     . |`._)   . L     ||_7\+-'
           /       | |       | |     .\   \.
          /        |  .      | |      \\_,'j
         .          ._ `----' /        `--" '
        j             "--..--'              |
       ,|                        ,-".       |
     ,' |                       /   |       '
    /   '                       `..'    ,'   \\
   /   j                               /      L
  j    |                              .       |
  |  _.'                              |     , |
  `-' .                               |   ,'  '
      |                               `.-'     .
      |                                        |
      |                                        j
      '                                       .
       `                                     /
        `.                                  /
     ______.                              ,'
   ,'       `-._                     _,.'""`--..
  .         ___,+ -...._________,...<_          \\
   .___,.-"'                          `-._      |
                                          `-....' mh
""",'','')
        self.zubat = pokemon('Zubat',41,'This pokemon has no eyes, instead using high pitched screeches to echo locate',1,['poison','flying'],\
                               [1.9,0.9,0.7,0.6,0.8,1.1],{},20,1.3,{22:'golbat'},"""
                                        `"--.._
                                         '  ,__`-._
                                          ` |   `-.`._
                                           |`       `._`.
                                    ./"\   | `.        `.`.
                                  .'/   .  | _ `.        `.`.
     /|                          / /    |  || `-.`.         `..
    / |                         . /     |  ||    `.`.         `.`
   /  '        _.,.____      _,.'._     '  j       `.`          `..
  j ,-.`       . ""--._`-. ,',.-++.`. ,'  //         `..          `..
  / '  \`       \      `. '.'|  ''  \`   //            ``.          `.
 j /    \`.      \       || `'       |\ //              `..    __,....`.
 |.      `.`.     `.     ||         [|'//                 \\_,"        `
 ||       |,.`._    `----.`_"\   _.-"  .        ___........\|
jj        || `-.`-.______ `/`--'"       \   _.-'
|.        ||     `--..___""              .,'
||        ||             ""|             Y
||        ||               \            /
||        ||           _....\.         ,\\
||        '|        ,-'       `,.___,.-. .
||         L      ,'           `  /     ` .
||         '`    /              ||       ` .
||          \| ,'               ||        `.`
||        ___|/                 '|          .`.
||    _,-'    |                  L           ` .
||  ,'                           ||           ` .
` ./                             ||            ` .
 `V                              ||             ` .
                                 ||              ``
                                 ||               ``
                                 ||                `\\
                                 ||                 `'
                                 ||
                                 ||
                                 !|
                                 _/ mh
""",'','')
        self.golbat = pokemon('Golbat',42,'This pokemon uses it\'s fangs to bite into and drain the life from it\'s victims',1,['poison','flying'],\
                               [2.6,1.6,1.4,1.3,1.5,1.8],{},25,1.3,{0:0},"""
                           ---..__
_____                          `._"`._
  `._`"--_._                      `.  `._._
     `._   `-._._                   `.   `.`._
        `.     `-._.                  `.    `.`._
          `.       `-`._                `.    `-.`.
            `.        `-`._               \      `.`.
              \          `.`.              \       `-.`.
               \            `..             \         `.`.
                \             `..            \          `.`
                 \             _:`.           |           `..
                  L       _,-"" jj            |     ___......:
                  |     ,'      ||            |  ,."        .'
                  |   ,'        ||            |"'           / \\
                  |  /         /|L       ,".   ]`.         /   L
                  |,'         . ` \      /  ""'  "`.      j    |
                  /_          |  `.\    (\  <.)|    \     |    |
                    `-.       |    \`.  |_____..     \   j     |
                       `,     |     `.`.\|    V \   .'\  |     |
                         \    |       `._|       | <  ` j     j
                          `.  |          `.      |  \  |      |
                            \ |           |L      L  L |__    |
                             \|           ||      |  |  __`. j
                              Y           ||.-.   |  | |   \ |
                               \,--""'""`-.|`. \  |  |/|    `
                                '          |  \ `.'    j
                                          (|  | ,.`.  /
                                      _.-"_`._| | `' /
                              ,....../ ,'" `.__.'_,-'
                              `-----._`..      ""
                                      `.J mh
""",'','')
        self.oddish = pokemon('Oddish',43,'This pokemon is often mistaken for weeds',1,['grass','poison'],\
                               [2,1,1.1,1.5,1.3,0.6],{},20,1.3,{21:'gloom'},"""
                           .-"--.__
          _                / '+.--'
           \.-._          j / |
            \`-.`._      . j  |
             \  `. `.    | |  L                        _,,--+='
              L   `. `-. | |   \                  _.-+'    /
              |     \   j  |    \            _,-'" .'    ,'
              .      \  |  |     \         ,'   _,'    ,'
               \      `j   |      \      .'   ,'      /
                `.     |   |       \   ,'   ,'       /
                  \    |   |        \ /    /        /
  _,-''"'""'""'""`--. j    |         V    /      _,+............._
-=`...-----...__     `|    |         .   /   _.-'        _,.--"",..=.
      `-.       `._   |    |          L,'  ,'       _,.-'    ,-'
         `.        `. |    |          |  .'     _.-'       ,'
            .        \|    '          L/    _,-'          /
             `._      `.    L        /   _,'            ,'
                `-._    \   `       ,' ,'             ,'
                    `-.. `   \     /,-'           _.-'
                      ,'"-..  .   /_,..---"`+'""'"
                     /           '           `.
                    j                          .
                   .                           |
                   |   .-.       ,.            |
                   |    -'       `.'           |
                   `                           '
                    `.      .--.             ,'
                      `.    `._|          ,-'
                    _.-`   ,..______.. .  `-.
                  ,'       |          |      `.
                ,'         '          |        `.
               /         ,'            .         .
               \     _,-'               `._      |
                `---'                      `-....' mh
""",'','')
        self.gloom = pokemon('Gloom',44,'This pokemon emits a foul smell which can make you feel sick',1,['grass','poison'],\
                               [2.3,1.3,1.4,1.7,1.5,0.8],{},25,1.3,{0:0},"""
                            ,.--""+`-,
                    ___,..-'  C'  `.' `-.
                 ."|      `-,...._   ___:.
                /'"|   _,..^..__ _'"'     `-.
               ' `" ,-`c.   ..  `.     ,"".  `.
              /,  ,'       `._'   `.|)  "'    /\           .
          _,.|'- /  .-.             \         `".          |\\
      _.-'   |  |   '-        _     |           |          | \\
    ,'       |  |            \.'    |           |          |  .
   ,          . |                   |           j          j  |
  /_.-'"'"'"':.+|                   |          /         ,'   |
 /'       ,-'    \                 /        _,'-..___,..'     j
j|       /        `.             ,^.......-+                 /
||      /     _,-.""'-..____,..-'-._        \               /
| \   ,|    ,' .'   ,'    .         `.       \__         ,-'
 . `-'.|   /  /  _.'       `.         \       . `---+.-'|
  `._, ' j   j '"            `--..     `.     |.     `. |
        .|   |                           .    ||       `|
        `'   |,----......__...._         '    ||        |
             |`._=-=====___''-. `-.      |   / |        '
          _,.L   `"'"------|  .---'      |  /`-+_
     ,'"`/    \            |  |          |.'.    `""'-.
     |   \__,.'`           | j              _+-._     |
     |    `     `._        | |             ,     `---"
      .    `...,-' +._      `|            /
       `.       -'"   `-...________,..--.  `.,..
         \     |                         `.     |
          `._  |                          '    /
             `'                      _,.-'    /
                                  ,-'        /
                                 `.       _,'
                                   `'----' mh
""",'','')
        self.vileplume = pokemon('Vileplume',45,'This pokemon uses the pollens produced by it\'s flower to paralyze opponents',1,['grass','poison'],\
                               [2.6,1.6,1.7,2.2,1.8,1],{},30,1.3,{0:0},"""
                        _..--------..__
                    ,-"'    __         `-.
                 ,-'    .-"'  |   .--.    `. ____
               ,'  _..   `""''    `-'  _.-'"'    `"--._
             .'   `..'  _           _,' ,""`,        __`._
      _.--""'`"---.._  '."   ___..,'__   `"'        `. `. `.
    .'__       .-,   `'-+.--"-------..`-.   `=`       `"'   \\
  ,'(__,'   _   "       |( ,-'""'""'`-.`,|  _.----""'"`--.../
 /         |_)          | `-...______,.' |-'        `-'      `-.
j                      .'_,..........__,'     c.          .-.   `.
|        _,..  `+' _,.-'"        .,    `-._               \__'    `
|       `___,'   ,'   .:"',     '"    .-,  `-.     ,--.      _     |
 \             ,'       ""             `      `.   `--'    ,' |    |
  `.         ,'  .'""`.          :",       __   \          `..'    '
    `._     .    `---'            "       |  `.  \               ,'
       `"--+                   __          `"'    .           _,'
           |                 ('  )                |...,,...-'"
            `.                 "'                ,'
              `-..__                          _,'
                    `+---.=,---------+.----+"'
                ,'"`/     "          "   ,-.\\
                \    \         _        /  | +.
               .`.            '/       /   | | \\
             ,'   A   '               /    j |  `.
            '    / \   \             j    / /`.   \\
             `--'   \   \            |   j,'   `.,'
                      . |-.........,.|   .
                       `'            `,.' mh
""",'','')
        self.paras = pokemon('Paras',46,'This pokemon is born with a parasitic mushroom on it\'s back',1,['bug','grass'],\
                               [1.8,1.4,1.1,0.9,1.1,0.5],{},20,1.3,{24:'parasect'},"""
           ____                               ____
      ,-"|"    "",._                    _,--"' |  ``-.
     /   \.   _,'   `-.               ,'  \   ,'    ,-".
    /      `"'        |              /     \.'      |   L
   /_     .-..    ,'""|             |   _,.    ,--. `.__|
  j  \   /    |  /    |     _____   `  j   \  |    \     L
  |  |   `    L  \   / _.""|    ."'--._|    |  `.__/     |
  |  '    `-./    `.+-'    `..-'       |-.  |        ,"`.|
  `-'            ,'  )   __,...__       ` `-._      /   ||
   `,---.      ,'  .'_,-'        ``-._   `-.__|-.../_...'
    `-..,\.--'/..-`.'  ..-------..._ ,-."'`-.    `.
            ,"`.__  `.'    `'  `-' .(   ).   \     . ,--._
         ,"|`._)  `. |  _      ,.  |`-,'  `. |     |'     `.
        / _|  .    | | `-'     -'  |  .   ,' |,-""-`.,--.   `.
       /"" `.  `"-'  '    ___       `. `"'  .'       .   I-.  `.
     ,'      `-..,.-' ,-'"   `-.      `"--'"/         \   \ `.  `
    /         |      /         |"-.        /           `.  `. `. \\
   /          |.    | `. ___ ,.'  |       j            \ `   `. \ .
  j           | `. (`._ \  ."   _,{      ,'             L `.   . \|
  |           |,' `-.  `\   ",-'  |_,..-'|              |   L  |  '
  |           |      `-..'  '__,.-'      |              |    . |
 /|            L        `""''           j               |    | |
j |            |                        |              j     | |
| |             L                       |              .     ' j
| [             |                       |             /       '
 - `.           |                       |            /
    `.   ,'""`-,                        |.--..__    /
      `.'      \                        '       `.,'
        `.      \                     ,'      _,-'
          `.     `.                 ,'    _,-'
            `-..__ \              <___..-" mh
""",'','')
        self.parasect = pokemon('Parasect',47,'By this stage in the pokemon\'s life, the mushroom has fully taken over the function of the pokemon',1,['bug','grass'],\
                               [2.3,1.9,1.6,1.2,1.6,0.6],{},25,1.3,{0:0},"""
                                       _______
                                   _,""|      `-._
                                 ,"  _.'          `.
                                ,'""'               `.
                              ,'       ,.----._  .--. \\
                             /        `____    \  \_ ) \\
                           ,'              ""`-'    "   L
                         ,'                             |
                       ,'.'                              L
                     ,'-'    _,...._             .""`.   |
                  _,'     ,-'       `.       ,.   `.  `. '
              _.-'      .'     ______/       `_)    `._;  \\
           ,-'           `-"'""                            \\
         ,'   ,.---,                                        \\
        /   .'   _,                    ,""'`-._         ."`-.'
        7-"'-+--'     ___               `-.__  `.       `.   `
      ,'      \_____.'   `.--.'""`.          `-.'         `-..\\
     /         `.`._|     | |      |`--...,.---.               `.
   ,'      . `  |    \    ,-|     ,'..,-'       `.,_             \\
  /     "       |.,.._"'"'   `-..'  .'            \ `"-.._      __\\
 /              | '-..""..________./              |..-"". `+.  (  ,
j               | L"`--._....___  /               |_...  `/  \  -.'
|             | | |      `--._  "/                j__..`  `.  `.-'
|          /  j ' |           "./       ,.'    " /_..-"'\   \.  `.
|         /' / /| |            /         ' "    /'       \   \`.  `.
 L       / |V j | |           /               ,'          \   \ \   `.
 |      j  |  | |  L         j              ,'            /    | \   |
  L     |  |  | `.  \        |            ,'             j    /   \  |
  .    j   `. L   `._`.     j          _,'               '   '     . |
   \   |     `.\     `"`    |       _.'                 /   /      | |
    \  |       `           /   _,.-'                   /   /       j .
     \ |                  /.-"'                    _,-'  ,'       /,'
      '                                           '----"' mh
""",'','')
        self.venonat = pokemon('Venonat',48,'This pokemon is attracted to lights at night',1,['bug','poison'],\
                               [2.3,1.1,1,0.8,1.1,0.9],{},20,1.3,{31:'venomoth'},"""
                                           _.----.
                                       __,'   _,-'
                                  _.."_..---"'
                               _.'_,-'_____________,......
                    `. .   ._,_.-',--',.-...........    __;
                 __  `/ ),`','_.'..,--'_,.---;      `""'
              `.,..`"'  ,.'.-_.-',..-'"   ,-'
            _,..        ___-'           ,'
         ,-'    |     ,'   `-.         '----..
       ,'       |   ,'        \             \.
      /         '  /           L            `-
     |        ,'  j            |        ,     `.
     |    _,+----.|            |       . `.    .-.
     |   /\    ,..\L           '       |   .   |`---
     |`-| ,\___|  | \.        /        |   |  .--            .,|
     |   V     / ,   '-.....'"         |   |   `.           ,.-'`'
     |\       `-'                      `._,     _\
     '|                                         ` _   .-.--".-
  _,.. |                                       ,./`.,/   ,.-'
.' .   |,                            ,---,     "._      /
|  `     `.                         /   `.     ,--     /.----...,
 \         \                        \   ."    '.._             |
  `.        L                        `...'  `..--. -""_..    _.'
    `.      '.,`.                          ..'-.`,_      `-"'
      \       \` ',-                     .'     \\
       `.      L  `.  .             ,.-'"\       \\
         \     |    '`.`. .-. .-..,..'.   \       \\
          `-._,'         `". `-..          \       `.
                                            `. -.   |
                                              '-.+--' mh
""",'','')
        self.venomoth = pokemon('Venomoth',49,'The color of it\'s wings indicate the different kinds of poisons it has',1,['bug','poison'],\
                               [2.6,1.3,1.2,1.8,1.5,1.8],{},30,1.3,{0:0},"""
                      ,-""-.                _ _,....._
                    ,'     |            _,-"_..----""-"\\
              .   ,      ,'|         _,"_.-'            |
            ,'/  /|    ,'  |      ,-'_,'                |
           / /  /j    /    |   ,-'_,'            __,..--'
          / /  / '   /    j  ,' ,'          _.--'      /
         / /  / /   /     |,' .'         ,-'          /
        / /  j /   /     /' .'        ,-'            /
       / /   |j   /  __.' ,'       _,'             ,'
      / /  ,",|  /,-".' ,'       ,:_______________/
     / , ,','j  /", /,"/|      ,'                /
    /  |' /  |_/ / / .' |    ,'                 /
   /   |,'  ,' .' / /  j   ,'                _,`
  j   '/ ,-' .'  / /   | ,'              _.-" |
 .'   j.'  ,'|  / /    ,'          _,.--'     j
 | _.-_,../| | / /    |      _,,-'"        _./
 j  ,( )__ `.// /   ,'|  _.-'          _.-'  |
.   | `(  ) |/ /   /  ,`+        _,..-'      '
|   |   "'  | /  ,'_,'   `.  _,-'           .
|   .`.___,'--. /,'       ,+"               |
|  | `/         \     ,-'""'""-.._         .'
 .,j /           \ ,-'         \  `-.      /
  `|'      /`.    Y-"'""'---.._|     `.   /
   |     ,' / 7   |            |`-.    \ /
   |___,'  / /`.  |_           |   `.  ,'
   `.___..' / /  /  .,.__      |     `.
     `.____/,' _'   /`.  '`-.._|      Y
       `-+----'   ,'   7-..   j -.     .
         |  __.,-'    -|   `-.+   `-.  |
         |"'      ,.'` ',   /  `._   `.|
         |_  _,,.'      |`..      `.   |
          .'"          ,'  \.       `. "-.
          `        ,./"|\   \|        `.  |
           `v.^.,`.    | \   )     ,    `.|
             `._     .'   `./_\.--' .     `.
                `---'               '      /
                                     `. _,'
                                       " mh
""",'','')
        self.diglett = pokemon('Diglett',50, 'No one has ever seen the bottom of this pokemon',1,['ground','ground'],\
                               [1.3,1.1,0.5,0.7,0.9,1.9],{},20,1.3,{26:'dugtrio'},"""
                     _,.---'""'"--.._
                   ,"                `-.
                 ,'                     `.
                /     _       ,.          `.
               /     ||      |"|            \\
              /      ||      | |             \\
             /       .'      `_'              L
            j                                 |
            |        __,...._                 |
            |      ."        `.               |
            |      '           )              |
            |       `-...__,.-'               |
            |                                 |
            |                                 |
         ...|                                 |
      _,'   |                                 |
  _,-'  ___ |                                 |.-----_
-' ,.--`.  \|                                 |     . \\
,-'     ,  |--,                               |  _,'   `- -----._
      ,' ,'    - ----.            _,..       _|.',               \\
 ,-""' .-             \  ____   `'  _-'`  ,-'     `.              `-
 .--'"`   ,--:`.       --    ,"'. ,'  ,'`,_
        _'__,' |  _,..'_    ,:______,-     --.         _.
        -__..--' '      ` ..`L________,___ _,     _,.-'
                                              '" ' mh
""",'','')
        self.dugtrio = pokemon('Dugtrio',51,'A team of three digletts, this pokemon and burrow deep underground',1,['ground','ground'],\
                               [1.8,2,1,1,1.4,2.4],{},25,1.3,{0:0},"""
                                        _..-----._
                                     ,-'__      __`-.
                                   ,'  '  `    /  |  \\
                   _____          /   ,...            \\
              _.-""     `-.      |   /    `. ,-""`.    \\
             /             `.    |  |   `  || .    |    .
            j             _. \   |  `..__.' '      |    |
           .     __     ,'--. \ j       ,....`....-'    |
           |     .---. .     | \|      (__    )         |
           |   .'   . || '   |  Y         "'"'          |
           |   |      | `-..-'  |                       |
           |    `-...',.--.     |      ,--,.--""'"-.._ j
           |        ."    _|    |      .-" |    ,"'"`.`|
           |        `---"'      `.    /    '   /     |  `
           |                     L   /,-""-.   _,...     \\
       _._  L                    |  j|    _ | /     `.    L
     ,'   `-|                     L ||      | |  '   |    |
 ,--"     _||                     |j  `----'  `      |    |
"       ,',:|                     .     ,-""--.`-- -'     | _
     ,-._'  '.                    |     `-...__)         j'" `-.
    :,.._:.   `.               ,-'|                      |_,.._ ---.
               _:......--.,..-'   |                      |     `.  ,`.
          `""'' ..../__,  "----."'-\  _,-'"`._           | .   __
                                '-..- .....- .`-...,-""`-,|___.
                                                '"-----"'. mh
""",'','')
        self.machop = pokemon('Machop',66, 'This pokemon likes to build it\'s muscles and train in all kinds of martial arts',1,['fighting','fighting'],\
                               [2.5,1.6,1,0.7,0.7,0.7],{},20,1.3,{28:'machoke'},"""
                        ,."--.
                   _.../     _\""-.
                 //  ,'    ,"      :
                .'  /   .:'      __|
                || ||  /,    _."   '.
                || ||  ||  ,'        `.
               /|| ||  ||,'            .
              /.`| /` /`,'  __          '
             j /. " `"  ' ,' /`.        |
             ||.|        .  | . .      _|,--._
             ||#|        |  | #'|   ,-"       `-.
            /'.||        |  \." |  /             `
           /    '        `.----"   |`.|           |
           \  `.    ,'             `  \           |
            `._____           _,-'  `._,..        |
              `".  `'-..__..-'   _,.--'.  .       |
               ,-^-._      _,..-'       `.|       '
           _,-'     |'""'""              `|  `\    \\
       _.-'         |            `.,--    |    \    \\
  _,.""'""'-._      '      `.     .      j      '    \\
 /            `.___/.-"    ._`-._  \.    |      |     L
/  ____           /,.-'    . `._ '""|`.  `      |     |
 `.    `"-.      / _,-"     `._ `"'".  `. \     '     '
   \       `-   ."'            "`---'\   ` `-._/     /
    `-------.   |                     \   `-._      /
             \ j                      .       `...,'
              `|                       \\
               '                        \\
                .                      / \\
                |`.                   /   `._
                |    `.._____        /|      `-._
                |        |   Y.       |.         `.
                |       j     \       '.`"--....-'
             _,-'       |      |        \
          .-'           |     ,'         `.
         '              |     |            `.
         `.        __,..'     '.             \\
           `-.---"'             `-..__      _/
                                      `'""'' mh
""",'','')
        self.geodude = pokemon('Geodude',74,'Hikers will often trip over this pokemon, mistaking it for a boulder',1,['rock','ground'],\
                               [1.9,1.6,2,0.6,0.6,0.4],{},25,1.3,{25:'graveler'},"""
                                            _,.---.
                                        _,-'       `.
                                     _,'  ,          \\
                                   ,'  _,'   .        `.
                                  /  ,'     ,'          `.
         __                       .,'    _,'              `.
    _,..'  `-....___              :    ,'     '             \\
  ,'   /            :             /`.,'      /               `
 /    /  ._         |         __..|  `.    .'       ,         `.
 |   |   ,'"--._    |      ,-'    `-._`.,-'       ,:            .
.'\   \     _,'.    `'___.'           `"`.     _,' /            |
|  \   \---'       ,"'  .-""'"----.       `.  '  ,'             |
 `. `-.'          /    /                    `-..^._             '
   |._|    _.    /    /                            `._           .
   `...:--'--+..'   ,'                              /            |
       '._  `|   ,-'       _..._                   j     \       |
         |` |   /       ,-'     `-.__              |      L      |
         |  |  /      ,'                           |      |      |
         |_,'        /         _,-                  .     |      |
        ,'  ,   |  ,'        ,|            ,..._     \    |      '
       ,     \ j  '       _." |           /     `-.__'    '    ,'
        +._   '|       ,'|    |          /        ,'    .'    /
        |  `._  `-' .:|  |    '.       -'        '           j
        '    |`    ' |'  |     |                             |
         `.  |       |--'     _|        .                    |
           \ |       '----'""'           \      __,....-+----'
           | '                            `---""      .'
           `. `.                                     ,
             `" \_...-""''--..         _+          ,'
                  '            -.'  `-'  `.  ."-..'
                   `-..._            _____,.'
                         `--.....,-"' mh
""",'','')
        self.magnemite = pokemon('Magnemite',81,'This pokemon floats in the air using magnetic waves',1,['electric','electric'],\
                            [1.6,0.7,1.4,1.9,1.1,0.9],{},25,1.3,{30:'magneton'},"""
                                  _,._,._
                                 '-"._,"--,
                                  `"..-+-'
                                  :'==-:
                                  :`=-":
                                 _."-..|
     _____                  _.-'"  `""' `-._
    |  |  `""'----._      ,'                `.
    |__|            `.  ,'                    '.
    '..|""'---._     | /                        \    _.......______
          `""'--:    |/         ,.---._          \ .'.------.....__`-...
                |    j        ,'       `.         . '              |"--|
.'""|"---......-'   .|       /           \        |'     ______    |   |
|   |              / |      .      .      .       |    .'      `""`--..'
:""'|---.....___.-'.'|      |             |       |    :
 `"`+---....____,.'  `      `.           /       /|    '_
                      \ _,..  `.       ,'       / `      `""'--....,._
                      .'::__:   `-...-'        ,   `._            '   |
                      |-..--|          ,-"-. ,'       "--.....___:   j
                      `.::_,          |.-''-:                     `"'
                            `"-...____' " :.'
                                       `""' mh
""",'','')
        self.magneton = pokemon('Magneton',82,'This pokemon sends out pulses of electromagnetic wave which it uses to paralyze it\'s opponents',1,['electric','electric'],\
                            [1.6,0.7,1.4,1.9,1.1,0.9],{},25,1.3,{30:'magneton'},"""
                                 _
                              ,"'_\\
                         ,"\  `."  \       ,..._
                        '.' \   \   .     ('""`.\\     _
                         \   \  `.  |      /=.:.'  ,:`.`.
                          \   \.';  |""'""`-./   .'   .`
                           \   `"   '         `.'   ,' ,"`.
                            `.___..'            `. `..:'`./
                            /             _,.._   \    _.'
                 _....__   /            ,"     `.  ._,'
             ,-"'       `"+.           :         . |
+'"|""'-.  ,'               `.         |      "  | |
\\_|__   `:                   \         \       /  |          _,-.
      :)  |        ,.-----.    \         ._   .'   '._    _,-'`\  j
  ...,'   |       /        \    . __ _ _,".`"'   ,'   `.,"    _.`"
  \\ |  _,'      .          .   || |I ' -'|    _, _     `   ,"'  _.".
  `""'':         '     "    |   |`"'^"`"| /  ,`:://\     \  `..-' \  '
       '          \        /   ,""`--..`""-"`""':{.|      .      _,+"
        .          `-....-'   :`:'-|            |l,'      |.__.-"
         \,.                  '. :/                       |
     .-.":`.`.              ,'  "'     ,"-.   _       _,._|
     \`. \`,"`._        __,:      .    `.'/`,'.`.   .'    '
      '.`.;     "--+--'"_  `       `     `.` "' ; ,'  .  /
        `"         ||  :|.  :       `.     \_:.' :    _.'
                   ||  |||__|         `._        `..."
                   ||__||| _|            `"-....-"\\,\
                   || _| `"                  \\  \ \\'
                   `"'                        \`.-\
                                               \\.' mh
""",'','')
        self.onix = pokemon('Onix',95,'People have been known to ride on the back of this pokemon through the desert',1,['rock','ground'],\
                            [1.8, 0.9, 3.2, 0.6, 0.9, 1.4],{},30,1.3,{0:0},"""
                                                       _
                                       ___            | |
                                   .-"'   `...._      | |
                      _,--"'-.   ,' .           `.    | |
                    .'       ,`,'    \            `.  | |
                  ,'.      .','       \            | j  |
           __,..,'   `----"  `         \       _..-+.`  |..
        ,'"     .             '._  ___...-._ ,'     |   |  `--.
       /       _|              | `"        .'       |   |      `.
      /`  _.-`'  ._..----""`._ |         ,'         |   |        .
     | .-"         `-._    _,.' `.     .'          j    |         `.
  ,-""'--..._       |  '`""       `-../\     _,"''"|    |.._       ,|
 /    '.     `"----,'                 ` '._,'      |   j    `.   .' |
/_.-'"  `-.___..-."                    \ ,'   \    |   '    | `.'   '
`                |                    _.'          |  |,_   '   `. /
 .        _______|                 .-'    |.       `. '           |
  `...---"     .-'               .'       | `.                 ,  '
  ,'._     _,-"                  `        |  ,`.  ,  .    _.-'|    `.
 .    `""-'    `.                 \       `.....`.     .-',   |      .
 |             _,|                 ._ --.        |     '"--...       '
  `.--"`.....-" ,                    /".`        |   |        _____,'
    .       | .'_                   /   \        |  j       "'_,..'
     /`-...-+"   `.                 '   .'.__ -..'  |_,..   ,'  |
    '          ____.                 \  |    "`-..___,....-.    '
     .     _.""'   |                  `. .                 / .-'
      `. .'       .._                   \ \               / /
        `-._   _.'   `.                  \.--......____ .' /
          .'`""    .'  .                  .            '_.'
          |       /    |____               `"._     _,-"      ,-'"'
           `. _.,'     |    `.                 `--"'       _.--,.'
             `'--.__,."       |                          ,' .' |
                   |   ,.._   |"--._                  ,-+-.'  /
                   `..'    ``.'   ,.`.     _..__.-""'-.__.'\"'
                     `----.,"    '   .--..'   _..`-../:  _,'
                           .    /  .'  _.'\.-"  |     '-"
                            "--+--"`..'   |.   ,^.__,'
                                     `---"  `-" mh
""",'','')
        self.voltorb = pokemon('Voltorb',100,'This pokemon attacks people that mistake it for a pokeball',1,['electric','electric'],\
                            [1.9,0.6,1,1.1,1.1,2],{},25,1.3,{30:'electrode'},"""
                         __...--------...__
                    _.--'                  `"-..
                _.-'                  ,.        `-._
             _,'                    .'  \           `._
           ,"                     ,'     .             `.
         ,'                      /        `.             `.
        /                       .           \              `.
      ,'                         `.._        .               .
     /                               `-._    /`               \\
    /                                    `-._  \               \\
   /    __,........----...__                 `"-'               \\
  /.--""                    `'--.._                 ...........
 j                                 `"-._            `. /      |  `
 '                                      `._           `.      .   .
.                                          `._          `.    '   |
|                                             `.          \  /    |
|                                               `.         `'     |
|                                                 `.              |
|                                                   `.            |
'                                                     `.          |
 .                                                      .         |
                                                         \        '
  '                                                       \      '
   .                                                       \    /
    \       ____                                            .  /
     \    ."    `""-._                                       '/
      `   '           `-.                                   ,'
       `.  `.            `.                               ,'
         `.  .             `.                           .'
           `._`-.            \                        .'
              `._`._          '                    _,'
                 `._`"-._     |                 _."
                     "-.._`--'           __,.-"'
                          `""----------"' mh
""",'','')
        self.electrode = pokemon('Electrode',101,'This pokemon will self destruct if it thinks it\'s about to lose',1,['electric','electric'],\
                            [2.3,1,1.4,1.6,1.6,3],{},30,1.3,{0:0},"""

                         _,.--"'"'"''"'"''--..__
                    _.-"'                       `-._
                 _.'                                `-._
              _,'                     ._                `.
            ,'                          `._               `.
          .'                               `._              `.
         /                                    `.              \\
       ,'                             .         `.    |        `.
      /                               |           `.  |   |      .
     /                                |             \ |   |       \\
    /                                                `    | ,.-"'  \\
   /                                                                \\
  j                                                        |         .
  |                  __...--'"''""'"'"'"'`--..__           |         '
 j             _.--"'                           `-.._                 .
 |         _,-'                      .""'`--..__     `"-._            |
 |     _.-'                          |          `"-._     `._         |
 |  _.'                              |               `-._    `._      |
 |,'                                 |    |              `-._   `.    |
 |                                   |    |                  `-.  `._ |
 |                                   '    |     |               `.   `'
 |                                    `"--'.....+................'   j
 '                                                                   |
  .                                                                  '
   .                                                                /
    `                                                              /
     '                                                           ,'
      `.                                                        .
        .                                                      /
         `.                                                  ,'
           `.                                              .'
             `._                                        _.'
                `._                                 _.-'
                   `-._                         _,-"
                       `"--..__           __..-'
                               `"'"''"'"'" mh
""",'','')
        self.koffing = pokemon('Koffing',109,'This pokemon releases toxic gases when it becomes excited',1,['poison','poison'],\
                            [1.9,1.3,1.9,1.2,0.9,0.7],{},25,1.3,{35:'weezing'},"""
                               ,----.
                              '      |
                             /       '
                       __,..'         "-._        _
                  _.-""                   `-.   ," `".
         ,-._  _.'                           `"'      '
       ,'    `"                                       |
      .                                               .
       `.          _.--..               ____          '
       /         ,'    . `           ,"' .  `.         `.
      /         .         |         /         \          \\
     /          `------...'        ._____      .          \\
    .                                    `'"'"'            \\
    '                    ________                           .
   j           `.""/'"'"`        '"'"'"'--....,-            |
   |             `/.                      ,\ /              `.
   |                `-._               _.'  '                 `-.
   |                    `"-----------"'                         |
 ."                         ____                                |
|                      ,-""'    `".                            ,'
|                     .   .----.   `.                        ."
`.._                  |  '.____,'   |                        '
    |             ,". `.           ,' _                     /
    '            '   `._`.'._".__,' .' .                   /
     .            `'-._ `._     _.-'  _.'                 /
      `.               `.  `--'" _,.-'                    `
        .               ,'     ."                          '
         '        .-..-' _,.--._`"-..,-.                 ,'
        /         \    ,'       `-.    |           .-'"-"
        \          `-.'            `..'         _,'
         `.,.-"`._                           ,-'
                  `"-.                       |
                      \       ,..----.     _.'
                       `""---"        `..-" mh
""",'','')      
        self.weezing = pokemon('Weezing',110,'Formed when three koffings fuze together, this pokemon\'s gases are much more potent',1,['poison','poison'],\
                            [2.4,1.8,2.4,1.7,1.4,1.2],{},30,1.3,{35:'weezing'},"""
                  __....____,'  `-.
         ,""-..-'"          "-    |       ..      _.._
         |        _, .,           '._    /  `'""''    |
        .'         _____             `.,'     ____     `.
     _," _.'      \  |  '"--..        '       \__ `"-.   `.
    | ,'"|/        `-.______,'      `     ' |\_  `'""'  .  \\
    .'---'      _____             . '   `   |,'""'-._  ' \  .
   /   __..--""|___/ "-.._/|         ,'       ___    `. \ \ '_
  . .'...-----'""----.._.' |-.      |        | ,.`".   \ `'   |
  | `"                  "-.'-'      `.        \`._`.\   |.  .-'
."        _..._                 .              `._  ,   `.' |
 `.    ,"'_....`".               |                ""       .
  |    | |     | |             -'   `,                    /
  `,.  `._`---'_,'  ,-.    '        ' `-.             _   |
  ,\ `._  |___|  _,'  |  `    \        . /-.__     _.' `-"
  \ `.._`-._ _.-'_,.--'        |        `.    |  ,'
   `-"\ `-. ' ,'_         `-..'       .-'    /  /
       `._.---._ `"----.        .   ,'.   _.'  /
         `.     `'-.._/       -" ,-" `.`-'      `.
           `.,       .-"    _    |     | .     ) |
             '._  ,"`----""`.    |     ' `'       .
                ""           `--'       \`      ,"'
                                         `-._,-' mh
""",'','')
        self.solosis = pokemon('Solosis',577,'This pokemon is actually a single celled organism.',1,['psychic','psychic'],\
                               [2, 0.6, 0.8, 2.1, 1, 0.4],{},20,1.3,{26:'duosion'},'','','')
        
pokedex = pokedex() #actually creates the pokedex
evos = []
for value in pokedex.__dict__.items():
    evos.append(value)

moveTree = {'Bulbasaur':{6:vineWhip, 9:leechSeed, 20:poisonPowder, 34:growth, 41:sleepPowder},\
            'Ivysaur':{22:poisonPowder, 38:growth, 46:sleepPowder},\
            'Venusaur':{43:growth,55:sleepPowder},\
            'Charmander':{6:ember, 15:leer, 30:slash, 38:flamethrower},\
            'Charmeleon':{33:slash, 42:flamethrower},\
            'Charizard':{36:slash, 46:flamethrower},\
            'Squirtle':{6:bubble, 22:bite, 15:waterGun, 28:withdraw, 42:hydroPump},\
            'Wartortle':{24:bite, 31:withdraw, 47:hydroPump},\
            'Blastoise':{52:hydroPump},\
            'Caterpie':{7:harden},\
            'Metapod':{7:harden},\
            'Butterfree':{12:confusion, 15:poisonPowder, 16:stunSpore, 17:sleepPowder, 21:supersonic, 21:psybeam},\
            'Weedle':{5:tackle, 7:harden},\
            'Kakuna':{7:harden},\
            'Beedrill':{12:furyAttack, 20:twinNeedle, 35:agility, 30:pinMissile},\
            'Pidgey':{5:gust, 11:quickAttack, 15:wingAttack, 36:agility},\
            'Pidgeotto':{5:gust, 11:quickAttack, 15:wingAttack, 36:agility},\
            'Pidgeot':{5:gust, 11:quickAttack, 15:wingAttack, 36:agility},\
            'Ratata':{6:quickAttack, 12:bite, 14:hyperFang, 34:superFang},
            'Raticate':{6:quickAttack, 12:bite, 14:hyperFang, 41:superFang},\
            'Spearow':{9:leer, 15:furyAttack, 29:drillPeck, 36:agility},\
            'Fearow':{9:leer, 15:furyAttack, 29:drillPeck, 36:agility},\
            'Ekans':{10:poisonSting, 17:bite, 24:glare, 31:screech, 38:acid},\
            'Arbok':{17:bite, 27:glare, 36:screech, 47:acid},\
            'Pikachu':{7:thundershock, 9:thunderWave, 16:quickAttack, 26:swift},\
            'Sandshrew':{17:slash, 24:poisonSting, 31:swift, 38:furySwipes},\
            'Sandslash':{27:poisonSting, 36:swift, 47:furySwipes},\
            'Nidoran F':{8:scratch, 14:poisonSting, 21:tailWhip, 29:bite, 36:furySwipes, 43:doubleKick},\
            'Nidorina':{23:tailWhip, 32:bite, 41:furySwipes, 50:doubleKick},\
            'Nidoqueen':{23:bodySlam},\
            'Nidoran M':{8:hornAttack, 14:poisonSting, 29:furyAttack, 43:doubleKick},\
            'Nidorino':{8:hornAttack, 14:poisonSting, 32:furyAttack, 50:doubleKick},\
            'Nidoking':{},\
            'Clefairy':{13:sing, 18:doubleSlap},\
            'Clefable':{},\
            'Vulpix':{16:quickAttack, 28:confuseRay, 35:flamethrower},\
            'Ninetales':{},\
            'Jigglypuff':{9:pound, 19:defenseCurl, 24:doubleSlap, 34:rest, 34:bodySlam},\
            'Wigglytuff':{},\
            'Zubat':{1:leechLife, 10:supersonic, 15:bite, 21:confuseRay, 28:wingAttack},\
            'Golbat':{10:supersonic, 15:bite, 21:confuseRay, 32:wingAttack},\
            'Oddish':{1:absorb, 15:poisonPowder, 17:stunSpore, 19:sleepPowder, 24:acid},\
            'Gloom':{28:acid},\
            'Vileplume':{},\
            'Paras':{13:stunSpore, 20:leechLife, 27:spore, 34:slash, 41:growth},\
            'Parasect':{30:spore, 39:slash, 48:growth},\
            'Venonat':{24:poisonPowder, 27:leechLife, 30:stunSpore, 35:psybeam, 38:sleepPowder, 43:psychic},\
            'Venomoth':{24:poisonPowder, 27:leechLife, 30:stunSpore, 35:psybeam, 38:sleepPowder, 43:psychic},\
            'Diglett':{15:growl, 31:slash},\
            'Dugtrio':{},\
            'Geodude':{11:defenseCurl, 16:rockThrow, 21:selfdestruct, 26:harden, 31:earthquake, 36:explosion},\
            'Magnemite':{21:sonicBoom, 25:thundershock, 29:supersonic, 35:thunderWave, 41:swift, 47:screech},\
            'Magneton':{21:sonicBoom, 25:thundershock, 29:supersonic, 35:thunderWave, 41:swift, 47:screech},\
            'Onix':{19:rockThrow, 33:slam, 43:harden},\
            'Voltorb':{17:sonicBoom, 22:selfdestruct, 36:swift, 43:explosion},\
            'Electrode':{17:sonicBoom, 22:selfdestruct, 40:swift, 50:explosion},\
            'Koffing':{1:smog, 32:sludge, 40:selfdestruct, 45:haze, 48:explosion},\
            'Weezing':{1:smog, 32:sludge, 43:selfdestruct, 45:haze, 53:explosion},\
            }
