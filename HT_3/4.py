"""
4. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат.
Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi,
обробляє повернутий ними результат та також повертає результат.
Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3

моя функція буде виводити середню заробітню плату за 3 місяці, при чому, за кожен місяць зарплата нараховується відповідно до окладу та премій.
"""
def month_1(x):
    x += x*15/100
    return x

def month_2(y):
    y += y*25/100
    return y

def month_3(z):
    z += z*99/100
    return z

def average_zp(zp):
    print(f'Cередня заробітня плата за 3 місяці: {round((month_1(zp)+month_2(zp)+month_3(zp))/3, 2)}')

zp_oklad = float(input("Введіть посадовий оклад: "))

average_zp(zp_oklad)

