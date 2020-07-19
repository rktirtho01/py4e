mark = input('Enter Mark : ')

try:
    fahr = float(mark) 
    cel = (fahr - 32.0) * 5.0 / 9.0 
    print(cel) 
except:
     print('Please enter a number')



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

