
fHand = open("romeo.txt")
"""Read data from text romeo.txt file. split all word from line and make a bar chart using dictionary"""
wordChart = dict()
for line in fHand:
    words = line.split()
    for word in words:
        wordChart[word] = wordChart.get(word,0)+1

wordsList = list(wordChart)
wordsList.sort()

for i in wordsList:
    print(i, wordChart[i])

print(wordsList)

