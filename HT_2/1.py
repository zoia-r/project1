"""
1. Написати скрипт, який конкатенує всі елементи в списку і виведе їх на екран. Список можна "захардкодити".
   Елементами списку повинні бути як рядки, так і числа.
"""
list_1 = [12, 'black', 'red', 41, 6, 'hello', 'friends']
suma_elemets = str(list_1[0])
for i in range(1, len(list_1)):
    suma_elemets+=str(list_1[i])
print(suma_elemets)

    
