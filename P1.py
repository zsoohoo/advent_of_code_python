
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
	print(total)