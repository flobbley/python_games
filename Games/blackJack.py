from random import *

class card(object):
    """
    cards in the deck, 4 copies of each
    """
    def __init__(self, value, pic):
        self.value = value
        self.pic = pic
    def getVal(self):
        return self.value
    def getPic(self):
        return self.pic
    def __repr__(self):
        return str(self.pic)
    def __str__(self):
        return str(self.pic)
    def __add__(self, other):
        total = self.value + other.value
        return total
    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)
def deal(deck):
    """
    Deals the cards, first to the player then to the dealer
    """
    #repeat deal two times for each player
    #select card at random from deck and place in players hand
    #select card at random from deck and place in dealers hand
    player_hand =[]
    dealer_hand = []
    for x in range(1,3):
        #Player Hand
        dealt = choice(deck)
        player_hand.append(dealt)
        deck.remove(dealt)

        #Dealer Hand
        dealt = choice(deck)
        dealer_hand.append(dealt)
        deck.remove(dealt)
    a=player_hand[0].getPic()
    b=player_hand[1].getPic()
    c=dealer_hand[0].getPic()
    print('You:')
    print(a,b)
    print('Your total:',player_hand[0]+player_hand[1])
    input()
    print('Dealer:')
    print(c,'| |')
    print()
    return [player_hand, dealer_hand, deck]

def betting(bank_track, winCond):
    """
    Handles all betting, expects a list starting with the last bet amount,
    then the player's bank, then the dealers bank. Then the win condition of the previous round
    """
    bet = bank_track[0]
    bank1 = bank_track[1]
    bank2 = bank_track[2]
    if winCond == 2:
        bank1 += bet
        bank2 -= bet
        if bank2 <= 0:
            print('The Dealer ran out of money!')
            input('Press ENTER to end the game')
            return [bet, bank1, bank2]
    elif winCond == 3:
        bank1 -= bet
        bank2 += bet
        if bank1 <= 0:
            print('You\'ve gone bankrupt!')
            input('Press ENTER to end the game')
            return [bet, bank1, bank2]
    print('You have',bank1,'dollars')
    print('The dealer has',bank2,'dollars')
    valid = False
    while not valid:
        print('\nHow much would you like to bet?')
        bet = int(input('5\n10\n25\n50\n'))
        if bet in [5, 10, 25, 50]:
            valid = True
        else:
            print('Invalid entry')
    return [bet, bank1, bank2]

def printHand(hand):
    cards = []
    for card in hand:
        print(card.getPic(),end='')
    return ''
def getDeck():
    """
    prepares the deck automatically
    """
    #generate all cards in a suite and places them in a list
    deck = []
    for y in range(1,5):
        for x in range(2,15):
            if x <11:
                a = card(x,'|'+str(x)+'|')
                deck.append(a)
            elif x == 11:
                a = card(10,'|J|')
                deck.append(a)
            elif x == 12:
                a = card(10, '|Q|')
                deck.append(a)
            elif x == 13:
                a = card(10, '|K|')
                deck.append(a)
            elif x == 14:
                a = card(11, '|A|')
                deck.append(a)
    return deck

def hit(hand, deck):
    """
    adds card to hand and deletes from deck
    """
    dealt = choice(deck)
    hand.append(dealt)
    deck.remove(dealt)
    return [hand, deck]

def total(hand):
    """
    totals the values of cards in the hand
    """
    values = []
    for item in hand:
        x = item.getVal()
        values.append(x)
    total = sum(values)
    return total

def aceTotal(hand, aces):
    """
    calculates the total if aces are in hand, can only be used if aces are in the hand
    """
    run_tot = total(hand)
    for x in range(1,aces+1):
        run_tot -= 10
        if run_tot <= 21:
            return run_tot
    return run_tot
        
        
def aceCheck(hand):
    """
    checks for ace in hand
    """
    aces = 0
    for item in hand:
        if item.getVal() == 11:
            aces += 1
    return aces
        
def autoWin(player_hand, dealer_hand):
    ptotal = total(player_hand)
    dtotal = total(dealer_hand)
    if ptotal == 21 and dtotal == 21:
        return 1
    elif ptotal ==21 and dtotal != 21:
        return 2
    elif dtotal == 21 and ptotal != 21:
        return 3
    else:
        return 0
    
def card_count(hand, count):
    for card in hand:
        if card.getVal() < 6 or card.getVal() == 11:
            count+=1
        elif card.getVal() > 9:
            count-=1
    return count
        

def blackJack():
    print('+++++++++++++++++++++\n')
    print('Welcome to Blackjack!\n')
    print('+++++++++++++++++++++\n')
    deck = getDeck()
    win = 0
    loss = 0
    winCond = 1
    count = 0
    ccvalid = False
    while not ccvalid:
        cc = input('Would you like to see the card count?\n1. Yes\n2. No\n')
        if cc == '1':
            ccvalid = True
            cardCount = True
        elif cc == '2':
            ccvalid = True
            cardCount = False
        else:
            print('Invalid Input')
    playing = True
    bank_track = [0, 200, 200]
    #Player Turn
    while playing:
        print(win,'wins', loss, 'losses\n')
        bank_track = betting(bank_track, winCond)
        if bank_track[1] <= 0 or bank_track[2] <=0:
            break    
        hands = deal(deck)
        player_hand = hands[0]
        dealer_hand = hands[1]
        count = card_count(player_hand, count)
        count_display = card_count(dealer_hand[:1], count)
        count = card_count(dealer_hand, count)
        if cardCount:
            print('Current Count:',count_display)
        deck = hands[2]
        valid = False
        ptotal = 0
        dtotal = 0
        winCond = autoWin(player_hand, dealer_hand)
        if winCond != 0:
            print(printHand(dealer_hand))
            valid = True
        while not valid:
            print('What would you like to do?')
            action = input('1. Hit\n2. Stay\n')
            
            if action == '1':
                update = hit(player_hand, deck)
                player_hand = update[0]
                deck = update[1]
                countAdd = []
                countAdd.append(player_hand[-1])
                count_display = card_count(countAdd, count_display)
                count = card_count(countAdd, count)
                #checks total

                ptotal = total(player_hand)
                print(printHand(player_hand))
                if cardCount:
                    print('Current count:', count_display)
                print()
                if ptotal > 21:
                    acep = aceCheck(player_hand)
                    if acep == 0:
                        winCond = 3
                        print('Bust!')
                        break
                    else:
                        ptotal = aceTotal(player_hand, acep)
                        print('Total:', ptotal)
                        if ptotal > 21:
                            winCond = 3
                            print('\nBust!')
                            break
                else:
                    print('Total:', ptotal)
            elif action == '2':
                ptotal = total(player_hand)
                acep = aceCheck(player_hand)
                if ptotal > 21 and acep > 0:
                    ptotal = aceTotal(player_hand, acep)
                valid = True
            else:
                print('Invalid Input')
        #Dealer Turn
        if winCond == 0:
            bust = False
            print('Dealer\'s Turn')
            print(printHand(dealer_hand))
            dtotal = total(dealer_hand)
            print('Dealer total:',dtotal)
            if cardCount:
                print('Current Count:',count)
            if dtotal > 21:
                ace = aceCheck(dealer_hand)
                dtotal = aceTotal(dealer_hand, ace)
            while dtotal < 17:
                print('\nDealer hit\'s')
                input()
                update2 = hit(dealer_hand, deck)
                dealer_hand = update2[0]
                deck = update2[1]
                countAdd = []
                countAdd.append(dealer_hand[-1])
                count = card_count(countAdd, count)
                dtotal = total(dealer_hand)
                print(printHand(dealer_hand))
                if cardCount:
                    print('Current Count:',count)
                if dtotal > 21:
                    ace = aceCheck(dealer_hand)
                    if ace == 0:
                        print('\nDealer busts!')
                        bust = True
                        winCond = 2
                    else:
                        dtotal = aceTotal(dealer_hand, ace)
                        if dtotal > 21:
                            print('\nDealer busts!')
                            bust = True
                            winCond = 2
                        
                print('Dealer total:',dtotal)
            if dtotal == ptotal:
                winCond = 1
            elif ptotal > dtotal:
                winCond = 2
            elif ptotal < dtotal and bust == False:
                winCond = 3
        if winCond == 3:
            print('\nYou lose this hand')
            loss += 1
        elif winCond == 1:
            print('\nIt\'s a Push')
        elif winCond == 2:
            print('\nYou win this hand!')
            win +=1

        #play another hand
        valid2 = False
        while not valid2:
            keepplaying = input('\nWould you like to play another hand?\n1. Yes \n2. No\n')
            if keepplaying == '1':
                print()
                valid2 = True
                decklen = len(deck)
                if decklen <8:
                    print('Look\'s like we\'ve got to shuffle the deck')
                    input()
                    deck = getDeck()
                    count = 0
            elif keepplaying == '2':
                valid2 = True
                print('Goodbye!')
                input('Press ENTER to end')
                playing = False
                


##a = card(4,'|4|')
##b = card(7,'|7|')
##c = card(8,'|8|')
##d = card(11,'|A|')
##e = card(11,'|A|')
##hand = [d, e]
##aces = aceCheck(hand)
##print(aceCheck(hand))
##print(aceTotal(hand, aces))
