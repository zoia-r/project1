"""
5. Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити). Словник для
   роботи захардкодити свій.
                Приклад словника (не використовувати):
                {'a': 1, 'b': 3, 'c': 1, 'd': 5}
                Очікуваний результат:
                {'a': 1, 'b': 3, 'd': 5}
"""
dict_1 = {'Blue': 2, 'Black': 3, 'Red': 2, 'Yellow': 5, 'Green':3}
dict_out ={}
for  key, value in dict_1.items():
    if value not in dict_out.values():
        dict_out[key] = value  
print(dict_out)
