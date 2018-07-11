import deck
import constants
import card_functions
import bet_functions
from random import randint

def main():
    # loop for multiple shoes
    for shoe_number in range(constants.NUM_SHOES):

        ##### ACTIONS RELATED TO DECK
        # initialize the shoe
        shoe = deck.create_shoe(constants.NUM_DECKS)
        # initialize running count
        running_count = 0
        # randomly generate a cut card, i.e. num cards that must be dealt
        cut_card = len(shoe) - randint(int(len(shoe)*constants.MIN_DECK_PENETRATION), int(len(shoe)*constants.MAX_DECK_PENETRATION))

        ##### ACTIONS RELATED TO BETTING
        # give player initial amount of chips
        player_balance = constants.MAX_BANKROLL
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
            current_bet = bet_functions.get_bet(running_count, len(shoe))
            # if the player does not have enough money to make optimal bet
            if current_bet > player_balance:
                current_bet = player_balance
            # subtract the bet from the players hand
            player_balance -= current_bet

            # deal
            player_hand, dealer_hand, running_count, hole_card_count = card_functions.initial_deal(shoe, running_count)




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
