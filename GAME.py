import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Cards:

    def __init__(self,suit,rank):

        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):

        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self):

        self.all_cards=[]
        for suit in suits:
            for rank in ranks:

                self.all_cards.append(Cards(suit,rank))

    def deal_one(self):

        return self.all_cards.pop()

    def shuffle_cards(self):

        random.shuffle(self.all_cards)


class Player:

    def __init__(self,name):

        self.name=name
        self.player_cards=[]

    def add_cards(self,new_card):

        if type(new_card)==type([]):

            self.player_cards.extend(new_card)

        else:

            self.player_cards.append(new_card)

    def remove_card(self):

        return self.player_cards.pop()


player_one=Player('Player1')

player_two=Player('Player2')

new_deck=Deck()

new_deck.shuffle_cards()

for _ in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

round=0
game_mode=True
while game_mode:

    round+=1
    print(f'Rond No. {round}')

    if len(player_one.player_cards)==0:
        print('Player Two has won. ')
        game_mode=False
        break

    elif len(player_two.player_cards)==0:
        print('PLayer One has won. ')
        game_mode=False
        break

    player_one_card=[]
    player_one_card.append(player_one.remove_card())

    player_two_card=[]
    player_two_card.append(player_two.remove_card())

    comparision=True

    while comparision:

        if player_one_card[-1].value>player_two_card[-1].value:
            player_one.add_cards(player_one_card)
            player_one.add_cards(player_two_card)
            comparision=False
            break

        elif player_two_card[-1].value>player_one_card[-1].value:
            player_two.add_cards(player_one_card)
            player_two.add_cards(player_two_card)
            comparision=False
            break

        else:
            print('War has started!!')

            if len(player_one.player_cards)<5:
                print('Player 2 wins ')
                game_mode=False
                break

            elif len(player_two.player_cards)<5:
                print('Player 1 wins ')
                game_mode=False
                break

            else:

                for _ in range(5):
                    player_one_card.append(player_one.remove_card())
                    player_two_card.append(player_two.remove_card())
