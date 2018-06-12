with open('P4Input.txt') as f:
	count = 0
	for line in f:
		words = line.split()
		for i in range(len(words)):
			if words.count(words[i])>1:
				break
			if i == len(words)-1:
				count += 1
	print('{} valid passphrases in the file'.format(count))
