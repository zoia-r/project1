"""
1. Програма-банкомат.
   Створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>);
      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>) та історію транзакцій (файл <{username}_transactions.data>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено число; знімається не більше, ніж є на рахунку).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
      - файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
      - спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
      - потім - елементарне меню типа:
        Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив :)
"""
import csv
import pathlib
import json

MAIN_PATH = pathlib.Path(__file__).parent.resolve().joinpath('db')
USERS_DB = MAIN_PATH.joinpath('users.data')
BALANCE_PATH = MAIN_PATH.joinpath('balance')
TRANSACTIONS_PATH = MAIN_PATH.joinpath('transactions')

def login():
    print('Вас вітає банківська система GOOLD LAMP')
    name = input("Введіть ім'я користувача\n")

    data = None
    with open(USERS_DB, newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if  name == row['name']:
                data = (row['name'], row['password'])
                break
    if data == None:
        print(f"Користувача з ім'ям {name} не знайдено :(\n")
    else:
        for _ in range(3):
            if input('Введіть пароль\n') == data[1]:
                print('Вітаємо в системі GOLD LAMP')
                return data
        print('Ви використали три спроби :(')
    
    return None


def get_balance(name):
    try:
        with open(BALANCE_PATH.joinpath(f'{name}__balance.data')) as file:
            return int(file.read())
    except Exception as error:
        print(error)
    return None
    

def replenish_balance(name, money):
    try:
        now_money = get_balance(name)
        if now_money != None:
            with open(BALANCE_PATH.joinpath(f'{name}__balance.data'), 'w') as file:
                file.write(str(now_money + money))
            return True
    except Exception as error:
        print(error)
    return False


def add_transactions(name, op, money):
    try:
        with open(TRANSACTIONS_PATH.joinpath(f'{name}__transactions.data'), 'a') as file:
            to_json = {'operation': op, 'money': money}
            file.write(json.dumps(to_json))
            file.write('\n')
    except Exception as error:
        print(error)


def start():
    while True:
        data = login()
        if data:
            while True:
                name, pw = data
                print('*' * 30)
                print('Оберіть операцію')
                print('1. Продивитись баланс')
                print('2. Поповнити баланс')
                print('3. Зняти готівку')
                print('4. Вихід')
                get_op = input()
                # 1
                if get_op == '1':
                    res = get_balance(name)
                    if res != None:
                        print(f'--- ваш баланс {res}')
                # 2
                elif get_op == '2':
                    have_problem = True
                    for _ in range(3):
                        money = input('--- на скільки поповнити баланс?\n')
                        if money.isdigit():
                            money = int(money)
                            starus = replenish_balance(name, money)
                            add_transactions(name, 'add_money', money)
                            if starus:
                                print(f'--- рахунок поповнено на {money}')
                                have_problem = False
                            break
                        else:
                            print('--- система повинна приймати число :(')
                    if have_problem:
                        print('--- ви використали три спроби :(')
                # 3
                elif get_op == '3':
                    have_problem = True
                    for _ in range(3):
                        money = input('--- стільки ви хочете зняти?\n')
                        if money.isdigit():
                            money = int(money)
                            now_money = get_balance(name)
                            if now_money < money:
                                print(f'--- вам не доступна така сума, ваш баланс {now_money}')
                            else:
                                starus = replenish_balance(name, -money)
                                add_transactions(name, 'withdrawal_of_money', money)
                                if starus:
                                    print(f'--- ви зняли {money}')
                                    have_problem = False
                                break
                        else:
                            print('--- система повинна приймати число :(')
                    if have_problem:
                        print('--- ви використали три спроби :(')

                # 4
                elif get_op == '4':
                    break
                else:
                    print('--- Команда введена не вірно :(')


print(start())
