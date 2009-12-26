from time import time

HIGH, PAIR, TWO_PAIR, TRIPLE, STRAIGHT, FLUSH, FULL_HOUSE, QUAD, GAP, STRAIGHT_FLUSH = range(10)

def handToDict(hand):
    dHand = {}
    for card in hand:
        num, suit = card
        if num not in dHand:
            dHand[num] = []
        dHand[num].append(suit)
    return dHand

def numPairs(dHand):
    count = 0
    for k,v in dHand.items():
        if len(v) == 2:
            count += 1
    return count

def hasN(dHand,N):
    for v in dHand.values():
        if len(v) >= N:
            return True
    return False

hasTriple = lambda x: hasN(x,3)
hasQuad = lambda x: hasN(x,4)
ofAKind = lambda x: hasN(x,2)

def get34TieBreaker(dHand, n):
    for k,v in dHand.items():
        if len(v) == n:
            return k

def sort_key((x,y)):
    return (len(y),x)

def scoreOfAKind(dHand):
    if (hasQuad(dHand)):
        return (QUAD, get34TieBreaker(dHand, 4))
    elif hasTriple(dHand):
        score = TRIPLE
        score += numPairs(dHand) * 3
        return (score, get34TieBreaker(dHand, 3))
    else:
        return (numPairs(dHand), [k for (k,v) in sorted(dHand.items(), key=sort_key, reverse=True)])

def score(aCards):
    dHand = handToDict(aCards)
    if (ofAKind(dHand)):
        return scoreOfAKind(dHand)
    hand = sorted(aCards, reverse=True)
    score = 0
    # Check to see if it's a straight
    if (hand[4][0] == hand[0][0] - 4):
        score = STRAIGHT

    # Check to see if it's a flush
    suit = hand[0][1]
    for card in hand:
        if card[1] != suit:
            break
    else:
        score += FLUSH

    return (score, [num for (num,suit) in hand])

CLUBS, DIAMONDS, HEARTS, SPADES = range(4)
JACK,QUEEN,KING,ACE = range(11,15)
C = CLUBS
D = DIAMONDS
H = HEARTS
S = SPADES
J = JACK
Q = QUEEN
K = KING
A = ACE
T = 10

start_time = time()
test_hands = [(((5,HEARTS),(5,CLUBS),(6,SPADES),(7,SPADES),(KING,DIAMONDS)),
               ((2,CLUBS),(3,SPADES),(8,SPADES),(8,DIAMONDS),(10,DIAMONDS))),
              (((5,D),(8,C),(9,S),(J,S),(A,C)),
               ((2,C),(5,C),(7,D),(8,S),(Q,H))),
              (((2,D),(9,C),(A,S),(A,H),(A,C)),
               ((3,D),(6,D),(7,D),(T,D),(Q,D))),
              (((4,D),(6,S),(9,H),(Q,H),(Q,C)),
               ((3,D),(6,D),(7,H),(Q,D),(Q,S))),
              (((2,H),(2,D),(4,C),(4,D),(4,S)),
               ((3,C),(3,D),(3,S),(9,S),(9,D)))]


for pair in test_hands:
    print score(pair[0]), score(pair[1])
    if score(pair[0]) > score(pair[1]):
        print "Player 1 wins"
    elif score(pair[0]) < score(pair[1]):
        print "Player 2 wins"
    else:
        print "You screwed up!"

end_time = time()

print "Took", end_time-start_time, "seconds."
