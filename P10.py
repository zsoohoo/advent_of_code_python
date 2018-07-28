def processLengths(lengths, iterations):
	curPos = 0
	skipSize = 0
	elements = []
	for i in range(256):
		elements.append(i)
	for i in range(iterations):
		for length in lengths:
			if length < 256:
				for i in range((length/2)):
					temp = elements[(curPos+i)%256]
					elements[(curPos+i)%256] = elements[(curPos+length-i-1)%256]
					elements[(curPos+length-i-1)%256] = temp
				curPos = (curPos + skipSize + length)
				skipSize += 1
	return elements

with open('P10Input.txt') as f:
	input = f.readline()
	lengthsAsString = input.split(",")
	lengths = []
	for length in lengthsAsString:
		lengths.append(int(length))
	sortedElements = processLengths(lengths, 1)
	print('Problem 10 Part 1 Solution: {}'.format(sortedElements[0]*sortedElements[1]))
	knotHashLengths = []
	for ch in input:
		knotHashLengths.append(ord(ch))
	knotHashLengths.extend([17, 31, 73, 47, 23])
	sparseHash = processLengths(knotHashLengths, 64)
	denseHash = ''
	for i in range(16):
		currentValue = 0
		for j in range(16):
			currentValue = currentValue ^ sparseHash[16*i+j]
		denseHash += hex(currentValue)[2:].zfill(2)
	print('Problem 10 Part 2 Solution: {}'.format(denseHash))


