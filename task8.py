n = int(input('Enter numbers of slice on vertical: '))
m = int(input('Enter numbers of slice on horizontal: '))
k = int(input('Enter quantity of slices that you want to break off: '))

if k % n == 0 or k % m == 0:
    print('YES')
else:
    print('NO')