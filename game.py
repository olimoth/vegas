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
import random

DICE_SIDES = 6

class Dice(object):
    def __init__(self, owner):
        self.owner = owner
        self.value = None

    def __repr__(self):
        return '{}: {}'.format(self.owner, self.value)

    def roll(self):
        self.value = random.randint(1, DICE_SIDES)

class Casino(object):
    def __init__(self):
        self.cards = []
        self.dice = []

    def total_value(self):
        return sum(self.cards)

class Round(object):
    def __init__(self):
        self.casinos = {value:Casino() for value in range(1, DICE_SIDES+1)} 

    def deal_cards(self, cards):
        for value, casino in self.casinos.iteritems():
            casino.dice = []
            while casino.total_value() < 5:
                cardindex = random.randint(0, len(cards)-1)
                casino.cards.append(cards.pop(cardindex))

    def play_turns(self, players):
        for player in players:
            player.init_dice()
        while any([player.has_dice_left() for player in players]):
            for player in players:
                if not player.has_dice_left():
                    continue
                print '\n{}\'s turn'.format(player.name)
                played_dice = player.get_turn(self.casinos)
                self.casinos[played_dice[0].value].dice.append(played_dice)

class InteractivePlayer(object):
    def __init__(self, name):
        self.name = name
        self.init_dice()

    def init_dice(self):
        self.dice = [Dice(self.name) for _ in range(8)]

    def has_dice_left(self):
        if len(self.dice) > 0:
            return True
        else:
            return False

    def get_turn(self, casinos):
        '''
        Takes a list of casinos, {num: casino} 
        Returns which of its dice it is going to play
        '''
        for dice in self.dice:
            dice.roll()
        print 'dice: {}'.format([d.value for d in self.dice])
        print 'casinos:'
        for value, casino in casinos.iteritems():
            print '\t{}'.format(value)
            for dice in casino.dice:
                print '\t\t{}'.format(dice)
        desired_dice = int(raw_input('{}, play which dice: '.format(self.name)))
        played_dice = [d for d in self.dice if d.value == desired_dice] # TODO: error check
        for dice_to_remove in played_dice:
            self.dice.remove(dice_to_remove)
        return played_dice

class Game(object):
    def __init__(self, players):
        self.players = players
        self.cards = (
            [6] * 5 +
            [7] * 5 +
            [8] * 5 +
            [9] * 5 +
            [1] * 6 +
            [4] * 6 +
            [5] * 6 +
            [2] * 8 +
            [3] * 8
            )
        self.rounds = [Round() for _ in range(4)]

    def play(self):
        for round_num, cur_round in enumerate(self.rounds):
            print '\nround {}'.format(round_num+1)
            cur_round.deal_cards(self.cards)
            cur_round.play_turns(self.players)
               
if __name__ == '__main__':
    player_one = InteractivePlayer('alice')
    player_two = InteractivePlayer('boab')
    game = Game([player_one, player_two])
    game.play()

