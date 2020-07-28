import re

fHand = open('regex_sum_754341.txt')
total = 0
for line in fHand:
    numbers = re.findall('[0-9]+',line.rstrip())
    if len(numbers) != 0:
        for n in numbers:
            total += int(n)

print(total)