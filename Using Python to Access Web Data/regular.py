import re

fHand = open("note.txt")

for line in fHand:
    line = line.rstrip()
    if re.search("^F", line):
        print(line)