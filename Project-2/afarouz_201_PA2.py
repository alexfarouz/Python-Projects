'''
-------------------------------------------------------------------------------
Name: Alexander Farouz
Assignment: PA 2
Due Date: 9/19/22
-------------------------------------------------------------------------------
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by professor and class syllabus.
-------------------------------------------------------------------------------
Comments and Assumptions: A note to the grader as to any problems or
uncompleted aspects of the assignment, as well as any assumptions about the #
meaning of the specification. You can write in N/A if you don’t have any
comments/assumptions.
-------------------------------------------------------------------------------
NOTE: width of source code should be <=80 characters to be readable on-screen.
12345678901234567890123456789012345678901234567890123456789012345678901234567890
10 20 30 40 50 60 70 80
-------------------------------------------------------------------------------
'''

def gas_price(prev_price, new_price):
    
    '''
    The following block of code takes the inputs for the previous price
    and the new price, and compares them to determine how much gas you
    should put in your car depending on the change in price.

    If the new price <= previous price you should put a full tank

    If the price increases by < 20%, you should put 3/4 of a tank

    If the price increases by 20% or more but less than 80%, you should
    put half a tank
    
    If the price increases by 80% or more but less than 100%, you should
    put 1/4 of a tank

    If the price increases by 100% or more, you should not put any gas
    in your car
    '''
    
    if new_price <= prev_price:
        gas_price = str('Full Tank')
    elif new_price < (prev_price * 1.2) and new_price > prev_price:
        gas_price = str('3/4 Tank')
    elif new_price < (prev_price * 1.8) and new_price >= (prev_price * 1.2):
        gas_price = str('Half Tank')
    elif new_price < (prev_price *  2) and new_price >= (prev_price * 1.8):
        gas_price = str('1/4 Tank')
    else:
        gas_price = str('Go Home')
    return gas_price
    
def level(num_coins, difficulty):
    
    '''
    The following block of code takes the inputs for the number of
    coins collected, and the difficulty, and finds the level the
    player is at depending on the difficulty.

    If the difficulty is "Beginner" or "Amateur", every 4 coins
    collected translates to 1 level

    If the difficulty is "Intermediate" or "Pro", every 6 coins
    collected translates to 1 level

    If the difficulty is "Expert", every 8 coins collected translates
    to 1 level

    If the difficulty is "Legendary", every 10 coins collected
    translates to 1 level
    '''
    
    if difficulty == "Beginner" or "Amateur":
        result = num_coins // 4
    if difficulty == "Intermediate":
        result = num_coins // 6
    if difficulty == "Pro":
        result = num_coins // 6
    if difficulty == "Expert":
        result = num_coins // 8
    if difficulty == "Legendary":
        result = num_coins // 10
    
    return result

def card_game(player1_card, player2_card, tiebreak_with_card):
    
    '''
    The following block of code determines the card number for 'player 1'
    and 'player 2'.

    The if statement calculates whether or not the card is above 13 which
    represents the amount of cards in each suit. If the card is above 13
    there are ranges as to how many times 13 should be subtracted from the
    input number to determine the card number. For example, if the input x
    13 < x <= 26 you only subtract 13 to determine the card number.
    '''
    
    if player1_card <= 13:
        card1 = player1_card
    elif player1_card > 13 and player1_card <= 26:
        card1 = player1_card - 13
    elif player1_card > 26 and player1_card <= 39:
        card1 = player1_card - 26
    else:
        card1 = player1_card - 39
        
    if player2_card <= 13:
        card2 = player2_card
    elif player2_card > 13 and player2_card <= 26:
        card2 = player2_card - 13
    elif player2_card > 26 and player2_card <= 39:
        card2 = player2_card - 26
    else:
        card2 = player2_card - 39

    '''       
    The following block of code determines the suit each card is in
    for 'player 1' and 'player 2'.

    Suit 1 correlates with cards 1-13
    Suit 2 coreelates with cards 14-26
    Suit 3 coreelates with cards 27-39
    Suit 4 coreelates with cards 40-52
    '''
    
    if player1_card <= 13:
        suit1 = 1
    elif player1_card > 13 and player1_card <= 26:
        suit1 = 2
    elif player1_card > 26 and player1_card <= 39:
        suit1 = 3
    else:
        suit1 = 4
    if player2_card <= 13:
        suit2 = 1
    elif player2_card > 13 and player2_card <= 26:
        suit2 = 2
    elif player2_card > 26 and player2_card <= 39:
        suit2 = 3
    else:
        suit2 = 4
    
    '''
    The following block of code determines which player is the winner
    depending on the method being used.

    If tiebreak_with_card is true, it compares the card number found
    above and the winner is determined depending on which player has
    the higher card with a tie occurring if the card number is the same.

    If tiebreak_with_card is false, it compares the suit number found
    above and the winner is determined depending on which player has
    the lower suit with a tie occurring if the suit number is the same.
    '''
    
    if tiebreak_with_card == True:
        if card1 > card2:
            winner = str('Player 1 Wins')
        elif card1 < card2:
            winner = str('Player 2 Wins')
        else:
            winner = str('Tie')
    else:
        if suit1 > suit2:
            winner = str('Player 2 Wins')
        elif suit1 < suit2:
            winner = str('Player 1 Wins')
        else:
            winner = str('Tie')
            
    return winner
    