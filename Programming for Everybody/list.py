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