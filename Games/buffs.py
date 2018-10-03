def shout_buff(turns, add_turns=0, add=False):
    if add == False and turns >0:
        turns -=1
    elif add == True:
        turns+=add_turns
    return(turns)



    
