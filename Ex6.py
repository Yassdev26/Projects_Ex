class Game():
    def __init__(self):
        print('Welsome In Full Game..... ^_^')
        print('Choose Your Game From Our Collection')
        print('Press [1] : Play Multiplication Table Game')
        print('Press [2] : Play Even Odd Game')
        print('Press [3] : Sum Average Game')
        self.Choices()

########################################################
    #CHOICES
    def Choices(self):
        while True:
            try:
                user_choices = input('Enter Your Choice : ')
                user_choices = int(user_choices)
                if user_choices == 1:
                    self.Multiplication_App()
                elif user_choices == 2:
                    self.Even_Odd_Game()
                elif user_choices == 3:
                    self.Sum_Average_Game()
                else:
                    print('Enter Only Number 1,2 Or 3')
            except ValueError:
                print('Please Enter Your Number')

########################################################
    #MULTIPLICATION APP  
    def Multiplication_App(self):
        print('WELCOME TO MULTIPLICATION APP')
        start = int(input('Enter Your First Number : '))
        end = int(input('Enter Your Last Number : '))
        for x in range(start, end +  1):
            for y in range(1, 13):
                print(x, '*', y, '=' , x *y)
            print('-------------------------')

########################################################     
    #EVEN ODD GAME
    def Even_Odd_Game(self):
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

########################################################     
    #SUM AVERAGE GAME
    def Sum_Average_Game(self):
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

game1 = Game()