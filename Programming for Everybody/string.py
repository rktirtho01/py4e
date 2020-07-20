
emails = ['rktirtho@gmail.com', 'rejaul@yahoo.com', 'my@hootmail.com']

for emain in emails:
    aps = emain.find('@')
    dtype = emain.find('.com')
    domain = emain[aps+1:dtype]
    print(domain)

sentense = "Welcome to bangladesh"

print ('a' in sentense)

print(sentense.upper())
print(sentense)

words = sentense.split()
print(words)