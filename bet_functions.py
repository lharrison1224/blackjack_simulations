import config
import math

def get_bet(running_count, current_shoe_size):

    # allow for multiple betting systems
    if config.BETTING_SYSTEM is "MIT":
        '''
            MIT system formula (true count >= 2)

                bet = (true_count - 1) * (betting_unit)

            Examples (assume table_min = 5, betting_unit = 25)

                true_count = 3 => Bet is $50
                true_count = 2 => Bet is $25
                true_count = 1 => Bet is $5
                true_count = 0 => Bet is $5
                true_count = -1 => Bet is $5
                true_count = 10 => Bet is $225

            This is a linear system that is less volatile than other systems
        '''

        # calculate the true count, i.e. running_count scaled to ~1 deck in size
        true_count = int(math.floor(running_count/(current_shoe_size/52)))

        # only care about true counts that are bigger than one
        if true_count <= 1:
            return config.TABLE_MIN
        else:
            return (true_count - 1) * config.BETTING_UNIT

def player_lose(player_balance, bet):
    return player_balance - bet

def player_push(player_balance, bet):
    return player_balance

def player_win(player_balance, bet):
    return player_balance + bet

def player_win_blackjack(player_balance, bet):
    return player_balance + (config.BLACKJACK_PAYOUT * bet)
