from random import shuffle

class Card:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def create_shoe(num_decks):
    shoe = []
    names = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                "Ten", "Jack", "Queen", "King", "Ace"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

    for deck in range(num_decks):
        for card in range(52):
            shoe.append(Card(names[card%13], values[card%13]))

    # shuffle the decks in place
    shuffle(shoe)
    return shoe
