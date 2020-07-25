
fHand = open("romeo.txt")

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

