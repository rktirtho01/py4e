import re

fHand = open("mbox-short.txt")

for line in fHand:
    line = line.rstrip()
    if re.search("^X-\S+:", line):
        print(line)
    if re.search('^F.*?:',line):
        print(line)

massage = "My favourite number is 2 and 5, 7,17"
n = re.findall("[0-9]+", massage)
print(n)

vowel = re.findall('[aeiou]', massage)
print(vowel)

print('===============================================')
fHand1 = open("mbox-short.txt")

for line in fHand1:
    line = line.rstrip()
    #print(re.findall("^From (\S+@\S+)", line))
    print(re.findall("^From.*@([^ ]\S*)", line))
