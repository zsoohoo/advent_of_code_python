from math import sqrt, ceil, floor

with open('P3Input.txt') as f:
	line = f.readline()
	n = int(line)
	distance = -1
	if n == 1:
		distance = 0
	root = sqrt(n)
	nhps = ceil(root)**2 #Next highest perfect square
	corner = nhps - (ceil(root)-1) #1st corner lower than NHPS for no perfect squares
	corner2 = floor(root)**2+1 #corner furthest from NHPS (last perfect square +1)
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
	print('Problem 3 Part 1 solution is: {}'.format(distance))