# http://uva.onlinejudge.org/external/111/11191.html
# 11191 reader
# Programmer: Marcus Greathouse

# input
cases = int(input())
for case in range(cases):
	seq_length = int(input())
	test_case = []
	data = input().split()
	for j in range(len(data)):
		data[j] = int(data[j])
	test_case = data
		
	# output
	print('Case {}:\n{}'.format(case + 1, test_case))