# ACM 2005 Programming Contest Problem B
# Marcus Greathouse
# Geneology Searcher - pulls in test scenarios with geneology type data to count the number of spawn people in the datasbase have

#input
cases = int(input())
for i in range(cases):
	#pull the info for the case in and split it into useable info
	case_info = list(input().split())
	lines = int(case_info[0])
	gens = int(case_info[1])

	#store the parent-child info
	families = []

	#grab the family info
	for j in range(lines):
		families += [input().split()]

	#solve problem

	#display
	print('Tree {}:'.format(i + 1))
	for j in range(len(families)):
		if int(families[j][1]) > 0:
			kids = ''
			for k in range(2, int(families[j][1]) + 2):
				kids += (' ' + families[j][k])
			print('{} had {} kid(s) who was/were called{}.'.format(families[j][0], families[j][1], kids))
		else:
			print('{} had no children'.format(families[j][0]))
	print()
