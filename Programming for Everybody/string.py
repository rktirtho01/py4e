
emails = ['rktirtho@gmail.com', 'rejaul@yahoo.com', 'my@hootmail.com']

for emain in emails:
    aps = emain.find('@')
    dtype = emain.find('.com')
    domain = emain[aps+1:dtype]
    print(domain)