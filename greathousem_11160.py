# http://uva.onlinejudge.org/external/111/11160.html
# 11160 reader

# input
cases = int(input())
for case in range(cases):
	n = int(input())
	maze = []
	for rows in range(n):
		row = input()
		maze_row = []
		for square in range(n):
			maze_row += row[square]
		maze += [maze_row]

	# output
	print('Case {}:\n{}'.format(case + 1, maze))