import random
from os import system
from art import logo


def cls():
    system('cls')


def play_blackjack():
    start_game = input('Do you want to play a game of Blackjack? Type \'y\', or \'n\': ')
    if start_game == 'y':
        cls()
        blackjack()


def deal_cards():
    starting_card = []
    for _ in range(2):
        starting_card.append(random.choice(cards))
    return starting_card


def detect_blackjack(dealt_cards):
    sum_cards = sum(dealt_cards)
    if 11 in dealt_cards and sum_cards == 21:
        return True
    else:
        return False


def add_card(old_cards):
    new_deck = old_cards
    new_deck.append(random.choice(cards))
    return new_deck


def user_win(user_final_deck, computer_final_deck):
    if user_final_deck > computer_final_deck:
        return True
    elif computer_final_deck > user_final_deck:
        return False
    elif computer_final_deck == user_final_deck:
        return 'It\'s a draw'


def total_score(final_cards):
    final_sum = sum(final_cards)
    if final_sum > 21 and 11 in final_cards:
        for index in range(len(final_cards)):
            if final_cards[index] == 11:
                final_cards[index] = 1
        final_sum = sum(final_cards)
        return final_sum
    return final_sum


def blackjack():
    print(logo)

    continue_add_card = True

    user_deck = deal_cards()
    total_user_deck = total_score(user_deck)
    print(f'    Your Cards: {user_deck}, current score: {total_user_deck}')

    computer_deck = deal_cards()
    computer_first_card = computer_deck[0]
    print(f'    Computer\'s first card {computer_first_card}')

    # Check if Computer or Player has a Blackjack
    if detect_blackjack(computer_deck):
        print(f'    Your final hand: {user_deck}, final score: {sum(user_deck)}')
        print(f'    Computer\'s final hand: {computer_deck}, final score: {sum(computer_deck)}')
        print('You Lose, Opponent has Blackjack')
        play_blackjack()
    elif detect_blackjack(user_deck):
        print(f'    Your final hand: {user_deck}, final score: {sum(user_deck)}')
        print(f'    Computer\'s final hand: {computer_deck}, final score: {sum(computer_deck)}')
        print('You Win With a Blackjack!')
        play_blackjack()

    while continue_add_card:
        get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

        if get_another_card == 'y':
            user_deck = add_card(user_deck)
            total_cards_user = total_score(user_deck)
            total_cards_computer = total_score(computer_deck)
            print(f'    Your Cards: {user_deck}, current score: {total_cards_user}')
            print(f'    Computer\'s first card {computer_first_card}')
            if total_cards_user > 21:
                continue_add_card = False
                print(f'    Your final hand: {user_deck}, final score: {total_cards_user}')
                print(f'    Computer\'s final hand: {computer_deck}, final score: {total_cards_computer}')
                print('You went over. You lose')
                play_blackjack()

        elif get_another_card == 'n':
            # continue_add_card = False
            total_cards_user = total_score(user_deck)
            total_cards_computer = total_score(computer_deck)
            while total_cards_computer <= 16:
                computer_deck = add_card(computer_deck)
                total_cards_computer = total_score(computer_deck)
            print(f'    Your final hand: {user_deck}, final score: {total_cards_user}')
            print(f'    Computer\'s final hand: {computer_deck}, final score: {total_cards_computer}')

            if total_cards_computer > 21:
                print('Opponent went over. You Win')
            elif user_win(total_cards_user, total_cards_computer) == 'It\'s a draw':
                print('It\'s a Draw!')
            elif user_win(total_cards_user, total_cards_computer):
                print('You Win')
            elif not user_win(total_cards_user, total_cards_computer):
                print('You lose')
            continue_add_card = False
            play_blackjack()


if __name__ == '__main__':
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    play_blackjack()
