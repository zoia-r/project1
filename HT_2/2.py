"""
2. Написати скрипт, який пройдеться по списку, який складається із кортежів, і замінить для кожного кортежа останнє значення.
   Список із кортежів можна захардкодити. Значення, на яке замінюється останній елемент кортежа вводиться користувачем.
   Значення, введене користувачем, можна ніяк не конвертувати (залишити рядком). Кількість елементів в кортежу повинна бути різна.
             Приклад списка котежів: [(10, 20, 40), (40, 50, 60, 70), (80, 90), (1000,)]
             Очікуваний результат, якщо введено "100":
	     Expected Output: [(10, 20, "100"), (40, 50, 60, "100"), (80, "100"), ("100",)]
"""
n = input("Enter the value to which you want to replace the last elements of the tuple: ")
list_tuple = [(10, 20, 30, 40, 50), (30, 20, 10), (100, 90, 80, 70), (1000,), (50, 60)]
list_tuple_new = []
list_temp =[]
for i in list_tuple:
    for j in range(len(i)):
        if j == len(i)-1:
            list_temp = list(i)
            list_temp[j] = n
            i = tuple(list_temp)
            list_tuple_new.append(i)

print(list_tuple_new)
    

