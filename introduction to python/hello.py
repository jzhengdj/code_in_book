import string


for letter in string.ascii_lowercase:
	exists = False
	for word in scrabble.wordlist:
		if letter*2 in word:
			exists = True
			break
	if not exists:
		print("There is no English words with double" + letter)

vowels = "aeiou"
def has_all_vowels(word):
	for vowel in vowels:
		if vowel not in word:
			return False
	return True

for word in scrabble.wordlist:
	if has_all_vowels(word):
		print(word)