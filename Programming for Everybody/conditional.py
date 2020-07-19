mark = float(input('Enter Mark : '))
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
