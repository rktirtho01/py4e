mark = input('Enter Mark : ')

try:
    fahr = float(mark) 
    cel = (fahr - 32.0) * 5.0 / 9.0 
    print(cel) 
except:
     print('Please enter a number')


mark = fahr
if mark >100:
    print('Wrong Input')
elif mark >79:
    print("Later grade A+")
elif mark > 70:
    print("Later grade A")
elif mark > 60:
    print("Later grade B")
else:
    print('Marks is not enough to pass')


numbers = [67,6,26,746,74]
largest = None
print('Before:', largest) 
for i in [586,68,9]:
    if largest is None or i > largest:
        largest = i

print(largest)
