def stepThrough(commands, mode):
	offset = [0] * len(commands)
	current = 0
	iterations = 0
	highest = 0
	if mode == 0:	
		while current < len(commands):
			move = commands[current] + offset[current]
			offset[current] += 1
			current += move
			iterations += 1
		return iterations
	else:
		while current < len(commands):
			move = commands[current] + offset[current]
			if move > 2:
				offset[current] -= 1
			else:
				offset[current] += 1
			current += move
			iterations += 1
		return iterations

with open('P5Input.txt') as f:
	commands = [int(line.rstrip()) for line in f]
	#commands = [0,3,0,1,-3]
	print('Problem 5 Part 1 solution is: {}'.format(stepThrough(commands, 0)))
	print('Problem 5 Part 2 solution is: {}'.format(stepThrough(commands, 1)))
