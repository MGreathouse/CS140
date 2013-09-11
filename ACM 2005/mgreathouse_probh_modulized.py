# ACM 2005 Programming Contest Problem H
# Marcus Greathouse
# Two Ends - puls in a list of numbers that represent cards that are picked from either end to try and create the largest totsl


def main():
    #get input
    case = input()
    #set counter
    game = 1
    #loop until trailing setinal
    while case.split() != ['0']:
        data = read_data(list(case.split()))
        handle_data(game, data)

        #setup next test case
        game += 1
        case = input()


def read_data(deck):
    #return variable
    data = {}
    #convert to numbers
    for i in range(len(deck)):
        deck[i] = int(deck[i])

    # grab the number of choices out of the list
    data['number'] = deck.pop(0)
    data['deck'] = deck

    return data


def handle_data(game, data):
    # display results
    print('Game {}:\n{}'.format(game, data['deck']))

if __name__ == '__main__':
    main()
