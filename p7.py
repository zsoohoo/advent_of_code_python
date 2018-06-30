import re, collections

children = {}
weights = {}
names = []
found = False

def findRoot(children, names):
	root = ''
	for name in names:
		isChild = False
		for key, value in children.items():
			if name in value:
				isChild = True
				break;
		if not isChild:
			root = name
	return root

def getCorrectWeight(parent):
	node = parent
	global found
	childNodes = children[node]
	runningWeight = weights[node]
	childWeight = []
	if childNodes:
		for child in childNodes:
			childNodeWeight = getCorrectWeight(child)
			childWeight.append(childNodeWeight)
			runningWeight += childNodeWeight
		#print(node)
		#print(childNodes)
		if found is False:
			leastCommon = collections.Counter(childWeight).most_common()[-1]
			mostCommon = collections.Counter(childWeight).most_common()[0]
			if leastCommon != mostCommon:
				incorrectNode = childNodes[childWeight.index(leastCommon[0])]
				difference = mostCommon[0]-leastCommon[0]
				correctValue = weights[incorrectNode] + difference
				print('Problem 5 Part 2 solution: {}'.format(correctValue))
				found = True

	return runningWeight

with open('P7Input.txt') as f:
	for line in f:
		name, weight, *nodes = re.findall('\w+',line)
		names.append(name)
		weights[name] = int(weight)
		children[name] = nodes
	root = findRoot(children, names)
	print('Problem 5 Part 1 solution: {}'.format(root))
	getCorrectWeight(root)