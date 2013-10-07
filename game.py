'''
The Las Vegas board game consists of:
    
    * Six casinos, one for each dice value
    * Eight six-sided dice per player
    * Cash cards:
        $60,000 (5)
        $70,000 (5)
        $80,000 (5)
        $90,000 (5)
        $10,000 (6)
        $40,000 (6)
        $50,000 (6)
        $20,000 (8)
        $30,000 (8)
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
    Shuffle the cash cards
    Repeat setup, move starting card to next player

Winner is the player with the most money after 4 rounds
'''
