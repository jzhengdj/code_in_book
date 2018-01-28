import re

phoneNumberRegex = re.compile(r'(\d\d\d-)?\d\d\d\-\d\d\d\d')

mo = phoneNumberRegex.search('My number is 555-4242.')



batRegex = re.compile(r'bat(wo)?man')
mo1 = batRegex.search('The advanture of batwoman')

haRegex = re.compile(r'(Ha){3}')
mo2 = haRegex.search('HaHaHa ya')

xmasRegex = re.compile(r'\d+\s+\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3hens, 2 doves, 1 partridge')

vowelRegex = re.compile(r'[^aeiouAEIOU]')
list = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')

wholeStringIsNum = re.compile(r'^\d+$')
mo3 = wholeStringIsNum.search('423 424')

atRegex = re.compile(r'.at')
mo4 = atRegex.findall('The cat in the hat sat on the flat mat.')

nongreedyRegex = re.compile(r'<.*?>')
mo5 = nongreedyRegex.search('<To serve man> for dinner.>')

newlineRegex = re.compile(r'.*', re.DOTALL)
mo6 = newlineRegex.search('Serve the public trust\nProtect the innocent\nUphold the law.')
print(mo6.group())
