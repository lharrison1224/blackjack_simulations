import config
import card_functions as cf

def get_action(hand, dealer_upcard):
    '''Returns
        0 - stand
        1 - hit
        2 - double
        3 - split
        4 - surrender
    '''
    # get the value out of the Card class
    upcard = dealer_upcard.value

    # see if the hand can be split
    if len(hand) == 2 and hand[0].value == hand[1].value:
        if hand[0].value == 8 or hand[0].value == 11:
            return 3
        if hand[0].value == 10:
            return 0
        if hand[0].value == 9:
            if upcard <= 6 or (upcard >= 8 and upcard <= 9):
                return 3
            if upcard == 7 or upcard == 10 or upcard == 11:
                return 0
        if hand[0].value == 7:
            if upcard <= 7:
                return 3
            return 1
        if hand[0].value == 6:
            if upcard <= 6:
                return 3
            return 1
        if hand[0].value == 5:
            if upcard <= 9:
                return 2
            return 1
        if hand[0].value == 4:
            if upcard == 5 or upcard == 6:
                return 3
            return 1
        if hand[0].value == 3 or hand[0].value == 2:
            if upcard <= 7:
                return 3
            return 1

    # check to see if hand is a soft hand
    if check_aces(hand):
        # need to calculate total of other cards
        non_ace_total = 0
        for card in hand:
            if card.value != 11:
                non_ace_total += card.value

        if non_ace_total == 9 or non_ace_total == 10:
            return 0
        if non_ace_total == 8:
            if upcard != 6:
                return 0
            if len(hand) == 2:
                return 2
            else:
                return 0
        if non_ace_total == 7:
            if upcard <= 6:
                if len(hand) == 2:
                    return 2
                else:
                    return 0
            if upcard >= 7 and upcard <= 8:
                return 0
            return 1

    # only consider if surrender is allowed
    if config.SURRENDER_ALLOWED:
        value = cf.hand_value(hand)

        if value == 16 and upcard >= 9:
            return 4

        if value == 15 and upcard == 10:
            return 4

    # if control makes it here, hand is typical hard hand
    


#
#
# def get_action_with_deviations(hand, running_count, shoe_size):
#     # according to basic strategy and "Illustrious 18" deviations
