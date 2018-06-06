
def getLineChecksum(lineContent):
	high = 0
	low = 999999999
	for i in range(len(lineContent)):
		if lineContent[i] < low:
			low = lineContent[i]
		if lineContent[i] > high:
			high = lineContent[i]
	return high-low

def getAltChecksum(lineContent):
	for i in range(len(lineContent)):
		for j in range(len(lineContent)):
			if i != j:
				if lineContent[i]%lineContent[j] == 0:
					return int(lineContent[i]/lineContent[j])
	return

with open('P2Input.txt') as f:
	checksum = 0
	checksum2 = 0
	for line in f:
		lineContent = line.split()
		lineContent = [int(i) for i in lineContent]
		checksum += getLineChecksum(lineContent)
		checksum2 += getAltChecksum(lineContent)
	print('Problem 2 Part 1 solution is: {}'.format(checksum))
	print('Problem 2 Part 2 solution is: {}'.format(checksum2))
		