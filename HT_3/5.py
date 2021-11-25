"""
5. Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
-  Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї),
пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y"
і при нерiвностi змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.
-  Повиннi опрацювати такi умови:
-  x > y;       вiдповiдь - х бiльше нiж у на z
-  x < y;       вiдповiдь - у бiльше нiж х на z
-  x == y.      вiдповiдь - х дорiвнює z
"""
def comparison (x, y):
    if x > y:
        print (f'{x} більше ніж {y} на {x-y}')
    elif x < y:
        print (f'{y} більше ніж {x} на {y-x}')
    else:
        print (f'{x} дорівнює {y}')


number1 = int(input("Enter X for comparison: "))
number2 = int(input("Enter Y for comparison: "))

comparison (number1, number2)
