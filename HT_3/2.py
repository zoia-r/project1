"""
2. Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно).

"""
year1 = int(input("Enter the starting year: "))
year2 = int(input("Enter the final year: "))
for i in range(year1, year2+1):
    if i %400 == 0 or i % 4  == 0 and i % 100 != 0:
        print (i)
