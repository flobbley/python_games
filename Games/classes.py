from random import *
class character(object):
    """
    a character is any game entity that can be used by the player
    """
    def __init__(self, name, race, stg, ing, cha, spd, hlth):
        self.name = name
        self.race = race
        self.stg = stg
        self.ing = ing
        self.cha = cha
        self.spd = spd
        self.hlth = hlth
        
    def __str__(self):
        return str([self.name, self.race, self.stg, self.ing, self.cha ,self.spd, self.hlth])

    def checkStg(self,difficulty):
        """
        Perform a strength check
        """
        roll = randint(1,self.stg)
        if roll > difficulty:
            return True
        else:
            return False
        
    def checkIng(self,difficulty):
        """
        Perform an intelligence check
        """
        roll = randint(1,self.ing)
        if roll > difficulty:
            return True
        else:
            return False
        
    def checkCha(self,difficulty):
        """
        Perform a charisma check
        """
        roll = randint(1,self.cha)
        if roll > difficulty:
            return True
        else:
            return False

    def checkSpd(self,difficulty):
        """
        Perform a speed check
        """
        roll = randint(1,self.spd)
        if roll > difficulty:
            return True
        else:
            return False

    def checkHlth(self,difficulty):
        """
        Perform a health check
        """
        roll = randint(1,self.hlth)
        if roll > difficulty:
            return True
        else:
            return False



    
