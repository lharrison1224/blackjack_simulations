import deck
import config
import card_functions as cf
import bet_functions as bf
from random import randint

def main():
    # loop for multiple shoes
    for shoe_number in range(config.NUM_SHOES):

        ##### ACTIONS RELATED TO DECK
        # initialize the shoe
        shoe = deck.create_shoe(config.NUM_DECKS)
        # initialize running count
        running_count = 0
        # randomly generate a cut card, i.e. num cards that must be dealt
        cut_card = len(shoe) - randint(int(len(shoe)*config.MIN_DECK_PENETRATION), int(len(shoe)*config.MAX_DECK_PENETRATION))

        ##### ACTIONS RELATED TO BETTING
        # give player initial amount of chips
        player_balance = config.MAX_BANKROLL
        # to be toggled if player_balance hits <= 0
        out_of_money = False

        hand_number = 0
        # set up loop for hands through deck
        while len(shoe) > cut_card and not out_of_money:

            # if the player doesn't have enough money to play the hand
            if player_balance <= 0:
                out_of_money = True
                break

            # get the bet based on count and remaining deck
            current_bet = bf.get_bet(running_count, len(shoe))
            # if the player does not have enough money to make optimal bet, bet all
            if current_bet > player_balance:
                current_bet = player_balance

            # deal
            player_hand, dealer_hand, running_count, hole_card_count = cf.initial_deal(shoe, running_count)

            # if dealer has blackjack and player has no blackjack
            if cf.check_blackjack(dealer_hand) and not cf.check_blackjack(player_hand):
                player_balance = bf.player_lose(player_balance, current_bet)
            # if both dealer and player have blackjack
            elif cf.check_blackjack(dealer_hand) and cf.check_blackjack(player_hand):
                player_balance = bf.player_push(player_balance, current_bet)
            # if player has blackjack and dealer has no blackjack
            elif cf.check_blackjack(player_hand) and not cf.check_blackjack(dealer_hand):
                player_balance = bf.player_win_blackjack(player_balance, current_bet)
            # if no blackjacks
            else:







            # add this at very end, will not know what this is until hand over
            running_count += hole_card_count
            # increment the number of hands played
            hand_number += 1

        # if the player is out of money don't play any more shoes
        if out_of_money:
            print("Player ran out of money after {} hands in shoe {}".format(hand_number, shoe_number+1))
            break









if __name__=="__main__":
    main()
