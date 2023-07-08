import random

SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
RANKS = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
VALUES = {
    'Ace': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13
}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return None

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def receive_card(self, card):
        self.cards.append(card)

    def show_cards(self):
        return ', '.join(str(card) for card in self.cards)

def play_round():
    deck = Deck()
    deck.shuffle()

    players = []
    num_players = int(input('Enter the number of players: '))

    for i in range(num_players):
        name = input(f'Enter the name of player {i+1}: ')
        players.append(Player(name))

    for _ in range(2):
        for player in players:
            player.receive_card(deck.deal())

    for player in players:
        print(f'{player.name}: {player.show_cards()}')

def play_poker():
    print('Welcome to Texas Hold\'em Poker!')
    play_round()

play_poker()