names = list()

names = ['Rejaul', 'Siam']
names.append('Hasib')
names.append('Kamal')
# List is muteable
print(names[1])

# Sorting list
names.sort()


for i in names:
    print(i)

print('List sclicing')

scliced= names[0:2]

print(scliced)

names.extend(["Mahin", "kamal"])

print(names)

names.pop(len(names)-1)
print(names)


sentence = "I love my country"
words = sentence.split()
print(words)

joinSentense = "I love my country, but everbody does not love."
commaSeperator = joinSentense.split(',')
print(commaSeperator)

latters = list(sentence)

print(latters)
