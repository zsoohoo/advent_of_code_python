
with open('P1Input.txt') as f:
	line = f.readline()
	line = line.rstrip()
	total = 0
	for i in range(len(line)):
		if i < len(line)-1:
			curr = int(line[i])
			nxt = int(line[i+1])
			if curr == nxt:
				total += curr

		elif i == len(line)-1:
			first  = int(line[0])
			last = int(line[i])
			if first == last:
				total += last
	print('Problem 1 Part 1 solution is: {}'.format(total))
	total = 0
	halfLen = int(len(line)/2)
	for i in range(halfLen):
		if i < halfLen-1:
			curr = int(line[i])
			nxt = int(line[i+halfLen])
			if curr == nxt:
				total += curr*2
	print('Problem 1 Part 2 solution is: {}'.format(total))