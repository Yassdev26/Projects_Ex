#EVEN ODD GAME
while True:
    try:
        number = input('Enter Your Number : ')

        if number == 'x':
            print('Game is Closed')
            break

        number = int(number)

        if number % 2 == 0:
            print('This Number Is Even')
        else:
            print('This Number Is Odd')
        print('-------------------------')
    except ValueError as op:
        print(op)