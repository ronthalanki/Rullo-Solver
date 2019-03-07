def get_puzzle(puzzle_name):
	file = open("test-cases/" + puzzle_name + ".txt", "r")
	
	size = int(file.readline())
	row_target = get_array(file.readline())
	col_target = get_array(file.readline())
	nums = []
	for _ in range(size):
		nums.append(get_array(file.readline()))

	print size
	print row_target
	print col_target
	print nums

def get_array(input_string):
	return [int(i) for i in input_string.split()]	

get_puzzle("1-sanity-check")