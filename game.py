import deck
import hand
import chips
import game_functions

while True:
    print('WELCOME TO BLACKJACK')

    deck = deck.Deck()
    deck.shuffle_deck()

    player_hand = hand.Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = hand.Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = chips.Chips()

    game_functions.take_bet(player_chips)

    game_functions.show_some(player_hand, dealer_hand)

    while game_functions.playing:
        game_functions.hit_or_stand(deck, player_hand)
        game_functions.show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            game_functions.player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < dealer_hand.value:
            game_functions.hit(deck, dealer_hand)
        game_functions.show_all(player_hand, dealer_hand)
        if dealer_hand.value > 21:
            game_functions.dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            game_functions.dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            game_functions.player_wins(player_hand, dealer_hand, player_chips)
        else:
            game_functions.push(player_hand, dealer_hand)
    print('\n Player total chips are at {}'.format(player_chips.total))

    new_game = input('Would you like to play another hand? y/n')

    if new_game[0].lower() == 'y':
        game_functions.playing = True
        continue
    else:
        print('Thank you for playing!')
        break
