import operator

with open('P8Input.txt') as f:
	instructions = []
	registers = []
	regValue = []
	largestValueEver = 0
	for line in f:	
		content = line.rsplit()
		instructions.append(tuple(content))
		if content[0] not in registers:
			registers.append(content[0])
			regValue.append(0)
	#registers to change, inc/dec, amount, skip, registers to check, operator, value
	for i in range(len(instructions)):
		stringToEval = str(regValue[registers.index(instructions[i][4])]) + instructions[i][5] + instructions[i][6]
		if eval(stringToEval):
			indexToChange = registers.index(instructions[i][0])
			if instructions[i][1] == 'inc':
				regValue[indexToChange] += int(instructions[i][2])
			else:
				regValue[indexToChange] -= int(instructions[i][2])
			if regValue[indexToChange] > largestValueEver:
				largestValueEver = regValue[indexToChange]
	largestValue = 0
	for val in regValue:
		if val > largestValue:
			largestValue = val
	print('Problem 8 Part 1 solution: {}'.format(largestValue))
	print('Problem 8 Part 2 solution: {}'.format(largestValueEver))