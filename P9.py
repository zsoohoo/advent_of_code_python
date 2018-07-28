with open('P9Input.txt') as f:
	isGarbage = False
	groupCount = 0
	totalCount = 0
	garbageCount = 0
	big = 0
	negateNext = False
	for line in f:
		for char in line:
			if char == '<' and not isGarbage:
				isGarbage = True
			elif isGarbage:
				if negateNext:
					negateNext = False
				elif char == '!':
					negateNext = True
				elif char == '>':
					isGarbage = False
				else:
					garbageCount += 1
			else:
				if char == '{':
					groupCount += 1
				elif char == '}':
					totalCount += groupCount
					groupCount -= 1
	print('Problem 9 total group score is: {}'.format(totalCount))
	print('Problem 9 non-cancelled character count is: {}'.format(garbageCount))