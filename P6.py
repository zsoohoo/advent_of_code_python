def redistribute(startingList):
	largest, toRedistribute = 0, 0
	for index, block in enumerate(startingList):
		if block > largest:
			toRedistribute = index
			largest = block
	addToAll = int(startingList[toRedistribute]/16)
	conditionalAdd = startingList[toRedistribute]%16
	startingPoint = (toRedistribute+1)%16
	newList = [i+addToAll for i in startingList]
	newList[toRedistribute] = addToAll
	for i in range(0, conditionalAdd):
		index = (i +startingPoint)%16
		newList[index] += 1
	return newList

with open('P6Input.txt') as f:
	line = f.readline()
	startingBlocks = line.split()
	startingBlocks = [int(i) for i in startingBlocks]
	previousConfigs = [list(startingBlocks)]
	iterations = 0
	currentConfig = startingBlocks
	cyclesBeforeRep =0
	while True:
		iterations += 1
		currentConfig = redistribute(currentConfig)
		if currentConfig in previousConfigs:
			cyclesBeforeRep = iterations - previousConfigs.index(currentConfig)
			break
		previousConfigs.append(list(currentConfig))
	print(iterations)
	print(cyclesBeforeRep)