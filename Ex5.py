#SUM AVERAGE GAME
print('WELCOME TO SUM AVERAGE GAME')

count = int(input('Enter How Many Number You Will Avilad : '))

current_count = 0
summ = 0

while current_count < count:
    print(current_count)
    number = float(input('Enter Your Number : '))
    summ += number
    current_count += 1

print(summ)