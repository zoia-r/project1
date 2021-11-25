"""
7. Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!

"""
def calculator(x, y, z):
    if z == '+':
        print(f'{x} + {y} = {x+y}')
    elif z =='-':
        print(f'{x} - {y} = {x-y}')
    elif z =='*':
        print(f'{x} * {y} = {x*y}')
    elif z =='/':
        if y == 0:
            print('Error. На нуль ділити не можна')
        else:
            print(f'{x} / {y} = {x/y}')
            
number_1 = float(input("Введіть перше число: "))
number_2 = float(input("Введіть друге число: "))
operation = input("Введіть арифметичну операцію (+, -, *, /): ")
calculator(number_1, number_2, operation)
