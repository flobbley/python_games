import os, keyboard, time, random
def gridSet(x, y, positions, apple):
    """
    Draws grid with all relevant characters
    """
    appleChar = 'x'
    spaceChar = ' '
    char = 'O'
    down = 0
    for height in range(y): #begins building grid by row
        right = 0
        down += 1
        line = ''
        for width in range(x): #for each row adds spaces
            right += 1
            if [right, down] in positions: #adds symbol for snake if coord is snake
                line+=char
            elif [right, down] == apple: #adds symbol for apple if coord is apple
                line+=appleChar
            else:
                line+=spaceChar #otherwise adds empy char
        print(line)

def appleRandom(x,y):
    """
    Gives random coordinates for a new apple
    """
    appleX = random.randint(1,x)
    appleY = random.randint(1,y)
    apple = [appleX, appleY]
    return apple
    
def applePlacer(x,y,positions):
    """
    Places a new apple on the grid, tries to randomly place apples
    until the apple is in an unoccupied square
    """
    while True:
        apple = appleRandom(x,y)
        if apple not in positions:
            return apple

def moveChar(x,y,positions, direction, apple, score):
    """
    Moves the snake around the grid and keeps track of score
    """
    direction = directionChanger(direction) #checks if the player is changing direction
    pos1 = [positions[len(positions)-1][0],positions[len(positions)-1][1]] #creates a copy coordinate of the front of player snake
    if direction == 'up': #moves the front coordinate in the relevant direction temporarily until conditions can be checked
        pos1[1] -= 1
    elif direction == 'down':
        pos1[1] +=1
    elif direction == 'left':
        pos1[0] -=1
    elif direction == 'right':
        pos1[0] +=1
    if pos1[0] >x: #checks if the front coordinate hit a wall
        pos1[0] = x
        return False
    if pos1[0]<1:
        pos1[0]=1
        return False
    if pos1[1] >y:
        pos1[1] = y
        return False
    if pos1[1]<1:
        pos1[1] = 1
        return False
    if pos1 in positions:#checks if the front coordinate hit the snake
        return False
    else:
        positions.append(pos1)#moves the front position permanently 
        if pos1 == apple: #checks if snake ate an apple, snake is lengthened by not removing back coordinate
            score += 100
            apple = applePlacer(x,y,positions)#places new apple
        else:
            positions = positions[1:]#if an apple is not eaten, the snake "moves" by removing the back coordinate after a new front coordinate is added
    return positions, direction, apple, score

def directionChanger(direction):
    """
    Checks if the player is changing direction by checking if the player is pressing a key
    """
    if keyboard.is_pressed('w'):
        direction = 'up'
    elif keyboard.is_pressed('s'):
        direction = 'down'
    elif keyboard.is_pressed('a'):
        direction = 'left'
    elif keyboard.is_pressed('d'):
        direction = 'right'
    return direction

def snake(x, y):
    """
    Main Game
    """
    while True: #plays until the player wants to quit
        pos1 = [x//2, y//2] #sets inial conditions
        pos2 = [pos1[0]+1, pos1[1]]
        pos3 = [pos1[0]+2, pos1[1]]
        positions = [pos3, pos2, pos1]
        direction = 'up'
        apple = applePlacer(x,y,positions)
        score = 0
        while True: #Cycles through drawing grid and getting player input
            os.system('cls')
            gridSet(x, y, positions, apple)
            time.sleep(.15) #delay after input and drawing grid
            try:
                positions, direction, apple, score = moveChar(x, y, positions, direction, apple, score)
                #if moveChar returns False, will give a TypeError. This means a Game Over has happened
            except TypeError:
                print('Game Over!')
                input()
                break
            print('Score:', score)
        print('Would you like to play again? y/n') #prompt player to play again if they lose
        again = input()
        if again == 'n':
            print('Bye!')
            input()
            break
print(snake(30, 25))
