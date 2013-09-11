# ACM 2005 Programming Contest Problem G
# Marcus Greathouse
# Swamp Things - takes in sets of coordinates and the longest line and when processed should remove the longest line that has at least four points

# get input
case = int(input())
counter = 1

while case != 0:
    points = []

    for i in range(case):
        points += [input().split()]

    for i in range(case):
        points[i][0] = int(points[i][0])
        points[i][1] = int(points[i][1])

    # solve problem

    #display results
    print('Photo {}:\n{}'.format(counter, points))

    #get next case
    case = int(input())
    counter += 1
