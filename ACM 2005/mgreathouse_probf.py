# ACM 2005 Programming Contest Problem G
# Marcus Greathouse
# Square Count - reads in rooms of coords that will ultimately have the square tiles inside of them all counted for as many possible squares that can be made

# get input
num_rooms = int(input())
case = 1

while num_rooms != 0:
    rooms = []
    for i in range(num_rooms):
        room = [input().split()]
        room = [int(room[0][j]) for j in range(len(room[0]))]
        rooms += [room]

    #display rooms
    print('Case {}:\n{}'.format(case, rooms))

    #get next case
    num_rooms = int(input())
    case += 1
