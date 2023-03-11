ticket = input('Enter number of your ticket: ')

if len(ticket) != 6:
    print("check the correctness of the entered data")
elif int(ticket[0])+int(ticket[1])+int(ticket[2]) == int(ticket[-3])+int(ticket[-2])+int(ticket[-1]):
    print('YES')
else:
    print('NO')
