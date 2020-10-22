#Python Code to read the file poker-hand.txt


import sys


def poker(hands):
    "Return the best hand"
    return max(hands, key=hand_rank)

# functions to find hand ranks

def hand_rank(hand):
    ranks = [card[0] for card in hand]
    ranks.sort(reverse=True)
    if straight(ranks) and flush(hand) and max(ranks) == 14:   #Royal Flush
        return (9)                                  
    elif straight(ranks) and flush(hand):          # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6,kind(3,ranks),kind(2,ranks))
    elif flush(hand):                              # flush
        return (5,ranks)
    elif straight(ranks):                          # straight
        return (4,max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3,kind(3,ranks),ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2,two_pair(ranks),ranks)
    elif kind(2, ranks):                           # kind
        return (1,kind(2,ranks),ranks)
    else:                                          # high card
        return (0,ranks)


def straight(ranks):
	"Return True if the ordered ranks from a 5-card straight"
	return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def flush(hand):
	"Return True if all the cards have the same suit"
	return len(set([suit for value,suit in hand])) == 1

def kind(n,ranks):
    "Return n(e.g. 2 or 3 of a kind) number cards of a same value"
    for r in ranks:
        if ranks.count(r) == n: return r
    return None


def two_pair(ranks):
    "Two pair of same values"
    pair = kind(2,ranks)
    lowpair = kind(2,list(reversed(ranks)))
    if pair and lowpair !=pair:
        return (pair,lowpair)
    else:
        return None


def assginIntValue(card):
    "To assign integer value for suits"
    switcher = {"T": 10, "J": 11, "Q": 12,"K": 13,"A": 14}
    return switcher.get(card)  if switcher.get(card) else int(card)

def playPoker(p1, p2):
    "p1 = Player 1, p2 = Player 2"
    return int(poker([p1, p2]) == p1)

if len(sys.argv) == 2:
    pokerHandFile = open(sys.argv[1], 'r')
    enteries = pokerHandFile.readlines()

    "Assigning values to tuples"
    player1Won=0
    for entry in enteries:
        cards = [(assginIntValue(sets[0]), sets[1]) for sets in entry.split(' ')]
        player1Won = player1Won + playPoker(cards[0:5], cards[5:])


    print(f"Player 1: {player1Won}")
    print(f"Player 2: {len(enteries) - player1Won}")
