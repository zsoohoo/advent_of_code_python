from math import sqrt, ceil, floor

def getRootAndCorners(number):
	root = sqrt(number)
	nhps = ceil(root)**2 #Next highest perfect square
	corner = nhps - floor(root) #1st corner lower than NHPS for non perfect squares
	corner2 = floor(root)**2+1 #corner furthest from NHPS (last perfect square +1)
	return [root, nhps, corner, corner2]

def getDistance(n):
	distance = -1
	if n == 1:
		return 0
	root, nhps, corner, corner2 = getRootAndCorners(n)
	if ceil(root)%2 ==0:
		cf = ceil(root) #generally on ceiling or floor is used depending on next highest whole
	else:
		cf = floor(root)
	#Check Corners first
	if root%2 == 0 or root%2 ==1: #Perfect Squares
		distance = root-1
	elif n == corner and ceil(root)%2 == 0: #Even corner
		distance = cf
	elif (n == corner and ceil(root)%2 == 1) or n == corner2: #Odd corner or Last perfect square+1
		distance = floor(root)

	#Check which side 
	if corner2 < n < corner: #Left/Right
		if ceil(root)%2 ==0: #Right
			center = corner - cf/2
			distance =cf/2 + abs(center-n)
		else: #Left
			center = corner - cf/2
			distance = cf/2 + abs(center-n)
	elif corner < n < nhps:
		if ceil(root)%2 ==0: #Top
			center = corner + cf/2
			distance = cf/2 + abs(center-n) 
		else: #Bottom
			center = corner + cf/2
			distance = cf/2 + abs(center-n)
	distance = int(distance)
	return distance

def findAdjacent(start):
	if start == 1:
		return [0]
	elif start == 2:
		return [1]
	root, nhps, corner, corner2 = getRootAndCorners(start)
	flr = floor(root)
	previousRing = (flr-2)**2
	clng = ceil(root)
	oneLess = start-1
	
	if start == corner2: #Corners have 2 adjacent
		return [previousRing + 1, oneLess]
	elif corner == start: 
		return [previousRing + clng-2, oneLess]

	if start == corner -1: #3 adjacent only occurs immediately preceding a corner
		if flr == 2: #exception for 6
			return [1,4,5]
		return [previousRing + clng-3, previousRing + clng-2, oneLess]
	elif root%2 ==0 or root%2 ==1: #Perfect squares occur before corners too
		if root == 2: #exception for 4
			return [1,2,3]
		return [int((root-2)**2), int((root-2)**2 + 1), oneLess]
	
	if start == corner+1:
		return [previousRing + flr-1, previousRing + flr, 
		oneLess-1, oneLess]
	elif start == corner2+1:
		return [previousRing + 1, previousRing + 2, oneLess-1, oneLess]
	
	if start < corner:
		offset = start - corner2
		return [previousRing + offset-1, previousRing + offset, previousRing + offset+1, oneLess]
	else:
		offset = nhps - start
		return [(ceil(root)-2)**2 - offset, (ceil(root)-2)**2 - offset+1, (ceil(root)-2)**2 - offset+2, oneLess]
	return ['Error'] #if this is printed something probably went wrong
#start - last corner = offset?  
	

def findNextHigher(n):
	if n < 1:
		return 1
	loopNum = 2
	totals = [1]
	while totals[-1] <= n:
		value = 0
		adjacencyList = findAdjacent(loopNum)
		for i in adjacencyList:
			value += totals[i-1]
		totals.append(value)
		loopNum += 1
	return totals[-1]


with open('P3Input.txt') as f:
	line = f.readline()
	n = int(line)
	distance = getDistance(n)
	nextHigher = findNextHigher(n)
	print('Problem 3 Part 1 solution is: {}'.format(distance))
	print('Problem 3 Part 2 solution is: {}'.format(nextHigher))