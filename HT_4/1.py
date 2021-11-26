"""
1. Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата,
і вертатиме 3 значення (кортеж): периметр квадрата, площа квадрата та його діагональ.
"""

def square(x):
    return [4*x, x**2, (2**0.5)*x]

side = float(input("Enter the side of the square: "))
print(square(side))
