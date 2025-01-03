from blackjack import main

# Bet spreads per count
neg_2 = 0
neg_1 = 0
zero = 25
one = 100
two = 200
three = 500
four = 800
five = 1000
six = 1000
seven = 1000
eight = 1000

# Is the player counting or not(false will just use basic strategy and the same bet size)
counting = True  
bet_size = 25

# Starting chips
chips = 10000

# Number of hands to do
hands = 100000

# Number of decks
decks = 6

# Deck penetration(how much of the deck if left until the deck is shuffled)
deckPenetration = 0.2

# BlackJack Payout
blackJackPayout = 3/2

# Hands per hour(used to estimate EV)
hands_per_hour = 80

main(chips, hands, decks, deckPenetration, True, True, 
     blackJackPayout, bet_size, counting, hands_per_hour, 
     neg_2, neg_1, zero, one, two, three, four, five, six, seven, eight)
