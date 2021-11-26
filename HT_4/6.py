"""
6. Вводиться число. Якщо це число додатне, знайти його квадрат,
якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.
"""

def number_change(x):
    if x > 0:
        return x**2
    elif x < 0:
        return x+100
    else:
        return x

number = int(input("Please, enter the number: "))
print(number_change(number))
