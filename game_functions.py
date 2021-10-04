playing = True


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry please provide an integer')
        else:
            if chips.bet > chips.total:
                print('Sorry, your bet can\'t exceed {}'.format(chips.total))
            else:
                break


def hit(deck, hand):
    single_hand = deck.deal()
    hand.add_card(single_hand)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing
    while True:
        x = input('Hit or Stand? Enter H or S: ')

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print('Player stands Dealer\'s Turn')
            playing = False
        else:
            print('Sorry. I did not understand that, please enter h or s only!!')
            continue

        break


def show_some(player, dealer):
    print('DEALERS HAND: ')
    print('one card hidden!')
    print(dealer.cards[1])
    print('\n')
    print('PLAYERS HAND: ')
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    print('DEALERS HAND: ')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('PLAYERS HAND: ')
    for card in player.cards:
        print(card)


def player_busts(player, dealer, chips):
    print('BUST PLAYER!')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('PLAYER WINS!')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('PLAYER WINS! DEALER BUSTED!!')
    chips.lose_bet()


def dealer_wins(player, dealer, chips):
    print('DEALER WINS!')
    chips.lose_bet()


def push(player, dealer):
    print('Dealer and Player tie! PUSH!!')
