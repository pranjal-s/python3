def linecount(filename):
	count = 0
	for line in open(filename):
		count += 1
	return count

if __name__ == '__main__':           # if this program is run by itself
	print(linecount('wc.py'))
