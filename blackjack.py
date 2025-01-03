from game import Game
from stats import Stats
from basic_strategy import decision
from deviations import deviated_decision
from bet_size import bet_sizing
import numpy as np
import matplotlib.pyplot as plt

def main(startChips, hands, decks, deckPenetration, H17, DAS, blackJackPayout, minBet, counting, hands_per_hour, neg_2=None, neg_1=None, zero=None, one=None, two=None, three=None, four=None, five=None, six=None, seven=None, eight=None,):
    stats = Stats(startChips)
    hands_completed = 0
    hands_to_be_done = hands

    while hands_completed < hands_to_be_done:
        game = Game(decks, deckPenetration, H17, DAS, blackJackPayout)

        
        while game.deckPenetration < len(game.deck):
            if counting:
                bet_size = bet_sizing(game.count, game.deck, neg_2, neg_1, zero, one, two, three, four, five, six, seven, eight)
            else:
                bet_size = minBet

            game.deal_player_start()
            game.deal_dealer_start()

            blackjack = game.check_blackjack()
            if blackjack:
                if blackjack == 'D':
                    game.count -= 1
                    stats.chips.append(stats.chips[-1]-bet_size)
                    stats.losses += 1
                    hands_completed += 1
                else:
                    game.count_card(game.dealer[1])
                    stats.chips.append(stats.chips[-1]+bet_size*game.payout)
                    stats.wins += 1
                    hands_completed += 1
            else:
                hand_choices = []
                while game.current_index < len(game.player.cards):
                    if counting:
                        choice = deviated_decision(game, game.deck, game.count)
                    else:
                        choice = decision(game)
                    if choice == 'H':
                        game.hit()
                    elif choice == 'S':
                        hand_choices.append(1)
                        game.current_index += 1
                    elif choice == 'P':
                        game.split()
                    elif choice == 'D':
                        game.hit()
                        hand_choices.append(2)
                        game.current_index += 1

                hand_results = game.check_winner()

                for hand in range(len(hand_results)):
                    if hand_results[hand] == 'W':
                        stats.chips.append(stats.chips[-1] + (bet_size * hand_choices[hand]))
                        stats.wins += 1
                        # print('Won', (bet_size * hand_choices[hand]))
                    elif hand_results[hand] == 'L':
                        stats.chips.append(stats.chips[-1] - (bet_size * hand_choices[hand]))
                        stats.losses += 1
                        # print('Lost', (bet_size * hand_choices[hand]))
                    else:
                        stats.ties += 1
                        stats.chips.append(stats.chips[-1])
                        # print('Push')
                    
                # print(game.dealer)
                # print(game.player.cards)
                # print(hand_results)
                # print('-----------------')

                game.end_hand()
                hands_completed += 1


    x = [num for num in range(hands_to_be_done)]
    
    # Plot the line
    plt.plot(x, stats.chips[:hands_to_be_done])

    # Customize the plot
    plt.title('Graph')
    plt.xlabel('Hands')
    plt.ylabel('$')
    plt.figtext(0.5, 0.3, f"W {round((stats.wins/(stats.wins+stats.losses+stats.ties)* 100), 2)}%", ha="center")
    plt.figtext(0.5, 0.225, f"L {round((stats.losses/(stats.wins+stats.losses+stats.ties)* 100), 2)}%", ha="center")
    plt.figtext(0.5, 0.15, f"T {round((stats.ties/(stats.wins+stats.losses+stats.ties)* 100), 2)}%", ha="center")

    # Show the plot


    print('End chip value:', stats.chips[hands_to_be_done])
    print('W', round((stats.wins/(stats.wins+stats.losses+stats.ties)* 100), 2), '%')
    print('L', round((stats.losses/(stats.wins+stats.losses+stats.ties)* 100), 2), '%')
    print('T', round((stats.ties/(stats.wins+stats.losses+stats.ties)* 100), 2), '%')
    print('EV', f'${round((stats.chips[hands_to_be_done]/hands_to_be_done)*hands_per_hour, 2)}/hr')
    print('Hands', hands_to_be_done)

    plt.show()
     