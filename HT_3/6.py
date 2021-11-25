"""
6. Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
-  якщо довжина бульше 50 - > ваша фантазiя
"""

def str_random(x):
    str_new = ''
    countLetter = 0
    countNumber = 0
    if 30<=len(x) <=50:
        for i in x:
            if i.isdigit():
                countNumber +=1
            elif i.isalpha():
                countLetter +=1
        print (f'Довжина: {len(x)} \nКількість букв: {countLetter} \nКількість цифр: {countNumber}')
    elif len(x)<30:
        for i in x:
            if i.isdigit():
                countNumber +=int(i)
            elif i.isalpha():
                str_new +=i
        print (f'Сума чисел: {countNumber} \nРядок без цифр: {str_new}')
    elif len(x)>50:
        print("Моя фантазія на цьому закінчилась...")
        
str1 = input ("Enter your line: ")
str_random(str1)

