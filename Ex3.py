#MULTIPLICATION APP

print('WELCOME TO MULTIPLICATION APP')
start = int(input('Enter Your First Number : '))
end = int(input('Enter Your Last Number : '))

for x in range(start, end +  1):
    for y in range(1, 13):
        print(x, '*', y, '=' , x *y)
    print('-------------------------')