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
    running_count += get_card(dealer_hand, shoe)
    hole_card_count = get_card(dealer_hand, shoe)

    return player_hand, dealer_hand, running_count, hole_card_count
