"""
1. Створити цикл від 0 до ... (вводиться користувачем). В циклі створити умову, яка буде виводити поточне значення, якщо остача від ділення на 17 дорівнює 0.
"""
number = int(input("Enter the number to which you want to create a loop: "))
for i in range(number+1):
    if i % 17 == 0:
        print(i)
