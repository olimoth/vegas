'''
The Las Vegas board game consists of:
    
    * Six casinos, one for each dice value
    * Eight six-sided dice per player
    * Between 2 and 5 players

Setup:
    
    For each casino, draw money cards until it is >= $50,000
    Assign the starting player card to someone (randomly?)

For each player:
    If they still have dice:
        Roll all their dice
        Choose a dice value to play
        Put all of those dice on the matching casino

End of round:
    For each card on the casino in decending order of value:
        Award to player with largest number of dice, if no other player has the same number of dice

Winner is the player with the most money after 4 rounds
'''
