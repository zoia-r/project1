"""
8. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів
в списку. Тобто, функція приймає два аргументи: список і величину зсуву
(якщо ця величина додатня - пересуваємо з кінця на початок, якщо від'ємна -
навпаки - пересуваємо елементи з початку списку в його кінець).
   Наприклад:
       fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
       fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]
"""

def shift_elements (lst, shift):
    s =len(lst)
    if shift > 0:
        for i in range(shift):
            lst.insert(0, lst.pop())
        return lst
    else :
        for i in range(-shift):
            lst.append(lst.pop(0))
        return lst


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shift_1 = int(input("Enter the shift: "))
print(shift_elements(nums, shift_1))
