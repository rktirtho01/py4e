movies = {"Tom cruse":"Missin Impossible", "Delian Criz": "Jems Bond" }
barChart = dict();

print(movies)

fhand = open("mbox-short.txt")

for line in fhand:
    for w in line:
        if w not in barChart:
            barChart[w] = 1
        else:
            barChart[w] = barChart[w]+1

for i in barChart:
    print(i, barChart[i])