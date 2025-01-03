def bet_sizing(count, deck, neg_2, neg_1, zero, one, two, three, four, five, six, seven, eight):
    decks_remaining = len(deck) // 52
    # print(count, decks_remaining)
    if decks_remaining:
        count = count // decks_remaining
    else:
        count = count // 0.5

    # print(count)
    # print('---')
    bet_size = {
        -2: neg_2,
        -1: neg_1,
        0: zero,
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
    }

    if count < -2:
        # print(bet_size[-2])
        return bet_size[-2]
    elif count > 8:
        # print(bet_size[8])
        return bet_size[8]
    else: 
        # print(bet_size[count])
        return bet_size[count]
