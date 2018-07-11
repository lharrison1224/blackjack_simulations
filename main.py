import deck
import constants
import card_functions
import bet_functions
from random import randint

def main():
    for _ in range(constants.NUM_SHOES):

        # initialize the shoe
        shoe = deck.create_shoe(constants.NUM_DECKS)
        # store the initial size of the deck
        start_size = len(shoe)
        # initialize running count
        running_count = 0
        # randomly generate a cut card, i.e. num cards that must be dealt
        cut_card = len(shoe) - randint(int(len(shoe)*constants.MIN_DECK_PENETRATION), int(len(shoe)*constants.MAX_DECK_PENETRATION))

        # set up loop for hands through deck
        while len(shoe) > cut_card:
            # get the bet based on count and remaining deck
            #current_bet = bet_functions.get_bet(running_count, start_size, len(shoe))
            # deal
            player_hand, dealer_hand, running_count, hole_card_count = card_functions.initial_deal(shoe, running_count)


            # add this at very end, will not know what this is until hand over
            running_count += hole_card_count












if __name__=="__main__":
    main()
