from collections import Counter

def countWords(words):
	for i in range(len(words)):
		if words.count(words[i])>1:
			return False
		if i == len(words)-1:
			return True

def countAnagrams(words):
	letterCounts = []
	for i in range(len(words)):
		letterNum =  Counter(words[i])
		if letterNum in letterCounts:
			return False
		letterCounts.append(letterNum)
	return True

with open('P4Input.txt') as f:
	nonRepeat = 0
	nonAnagram =0
	for line in f:
		words = line.split()
		if countWords(words) == True:
			nonRepeat +=1
		if countAnagrams(words) == True:
			nonAnagram +=1
	print('Problem 4 Part 1 solution is: {}'.format(nonRepeat))
	print('Problem 4 Part 2 solution is: {}'.format(nonAnagram))