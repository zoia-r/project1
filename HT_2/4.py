"""
4. Написати скрипт, який об'єднає три словника в новий. Початкові словники не повинні змінитись. Дані можна "захардкодити".
		Sample Dictionary :
		dict_1 = {1:10, 2:20}
		dict_2 = {3:30, 4:40}
		dict_3 = {5:50, 6:60}
		Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
dict_1 = {1:10, 2:20}
dict_2 = {3:30, 4:40}
dict_3 = {5:50, 6:60}
new_dict ={}
new_dict.update(dict_1)
new_dict.update(dict_2)
new_dict.update(dict_3)
print(new_dict)
