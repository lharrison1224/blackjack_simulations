def count_value(card):
    if card.value < 7:
        return 1
    elif card.value > 9:
        return -1
    else:
        return 0

def get_card(hand, shoe):
    card = shoe.pop()
    count_change = count_value(card)
    hand.append(card)
    return count_change

def initial_deal(shoe, running_count):
    player_hand = []
    dealer_hand = []

    running_count += get_card(player_hand, shoe)
    running_count += get_card(player_hand, shoe)
    hole_card_count = get_card(dealer_hand, shoe)
    running_count += get_card(dealer_hand, shoe)

    return player_hand, dealer_hand, running_count, hole_card_count

def hand_value(hand):
    hand_total = 0
    for card in hand:
        hand_total += card.value
    return hand_total

def check_blackjack(hand):
    # if hand doesn't have 2 cards can't be blackjack
    if len(hand) == 2 and hand_value(hand) == 21:
        return True

    # return false by default
    return False

def check_aces(hand):
    for card in hand:
        if card.value == 11:
            return True
    return False
