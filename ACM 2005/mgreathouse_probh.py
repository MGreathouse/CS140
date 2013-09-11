# ACM 2005 Programming Contest Problem H
# Marcus Greathouse
# Two Ends - puls in a list of numbers that represent cards that are picked from either end to try and create the largest totsl

#get input
case = input()

#set counter
game = 1

#loop until trailing setinal
while case.split() != ['0']:
    deck = list(case.split())

    #convert to numbers
    for i in range(len(deck)):
        deck[i] = int(deck[i])

    # grab the number of choices out of the list
    num_cards = deck.pop(0)

    # solve the problem

    # display results
    print('Game {}:\n{}'.format(game, deck))

    #setup next test case
    game += 1
    case = input()
