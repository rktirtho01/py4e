t = ('c','a', 'b')
# t[0] = "A"  Tuple is not mudifyable

t = ('a',)+t[1:] 
print(t)

i =6
i+=20
print(i)

txt = 'but soft what light in yonder window breaks' 
words = txt.split() 

myList = list()

myList.append(('r',4))

print(myList)


t = list() 
for word in words: 
    t.append((len(word), word))  # put tuple object in list

print(t)
t.sort()
res = list() 
for length, word in t: 
    res.append(word)
print(res)


t = ("Rejaul", 'Karim', "Tirtho")

fName, mName, lName = t  # Value assigning to other variable

print(fName)
print(mName)
print(lName)

url = 'marayaglobal.com'

domain, dom_type = url.split('.')

print(domain)
print(dom_type)
