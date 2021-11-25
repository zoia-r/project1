"""
3. Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12),
яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)
"""
def season(x):
    if 1<=x<=2 or x == 12:
        return "Winter"
    elif 3<=x<=5:
        return "Spring"
    elif 6<=x<=8:
        return "Summer"
    elif 9<=x<=11:
        return "Autumn"
    else:
        return "Error"
number = int(input("Enter number month 1...12: "))
print(season (number))

