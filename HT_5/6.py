"""
6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
  
"""


def range_new(start, finish=None, step=1):
    if finish == None:
        finish = start
        start = 0
    if step ==0:
        raise ValueError()
    if step>0:
        while start < finish:
            yield start
            start += step
    else:
        while start > finish:
            yield start
            start += step



for i in range_new(2):
    print(i)


for i in range_new(1, 10):
    print(i)


for i in range_new(10, 0, -2):
    print(i)
