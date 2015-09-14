import string

def compareItems((w1,c1), (w2,c2)):
	if c1 > c2:
		return - 1
	elif c1 == c2:
		return cmp(w1, w2)
	else:
		return 1

def main():
	print "Word Frequency Analyzer"
	print "This prints a report on the n most frequent words.\n"

	fname = raw_input("File to analyze: ")
	text = open(fname,'r').read()
	text = string.lower(text)
	for ch in """!"#$%&()*+,-./:;<=>?@[\\]?_'`{|}?""":
		text = string.replace(text, ch,' ')
		words = string.split(text)

	counts = {}
	for w in words:
		try:
			counts[w] = counts[w] + 1
		except KeyError:
			counts[w] = 1

	n = input("Output analysis of how many words? ")
	items =counts.items()
	items.sort(compareItems)
	for i in range(n):
		print "%-10s%5d" % items[i]

if __name__ == '__main__': main()
