"""
7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.
"""

def count_elements(list_elements):
    result = {}
    for i in list_elements:
        result[i] = list_elements.count(i)
    return result


list_starting = [2, 'a', 'b', ("q", 1, 2), 'c', 2, 3, 4, 5, 5, ("q", 1, 2), 'c', 'c', 3]
print(count_elements(list_starting))

