import string

sonnets = open("sonnets.txt").readlines()
word_set = set([elt.strip() for elt in open("sowpods.txt")])
sonnets_set = set()

def strip_punctuation(word):
	# Remove surrounding punctuation. If there's an apostrophe in the 
	# middle of the word, skip it
	word.replace("-", " ")
	apostrophe_index = word.find("'")
	if apostrophe_index != -1:
		return None
	return word.strip(strign.punctuation)

for line in sonnets:
	# split apart hyphenated words.
	line_words = line.replace("-", " ").strip().split()

	# if it's empty or a sonnet number, skip it.
	if len(line_words) <= 1:
		continue

	for word in line_words:
		stripped =  strip_punctuation(word)
		if stripped and len(stripped) > 1:
			sonnets_set.add(stripped.upper())

sonnet_words = list(sonnets_set)
sonnet_words.sort()

f = open("sonnet_words_test.txt")
for word in sonnects_word:
