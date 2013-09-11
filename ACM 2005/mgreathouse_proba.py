# ACM 2005 Programming Contest Problem A
# Marcus Greathouse
# Acronym Maker - pulls in test scenarios with unimportant words to ignore

#input
cases = int(input())

#loop until trailing setinal
while cases != 0:
	# insiginificant words
	insigs = []
	for i in range(cases):
		insigs += [input()]

	# get test case
	case = input()

	while case != 'LAST CASE':	
		# break the case up into individual words
		case = list(case.split())

		# hold only significant parts
		sigs = []
		for i in range(len(case)):
			valid = True
			for j in range(len(insigs)):
				if case[i] == insigs[j]:
					valid = False
					break
			if valid:
				sigs += [case[i]]

		#grab case acronym
		acry = sigs.pop(0)

		#output significant
		print('Case "{}":\n{}'.format(acry, sigs))
		case = input()

	cases = int(input())
