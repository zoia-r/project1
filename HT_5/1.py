"""
1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
   Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
   Логіка наступна:
       якщо введено коректну пару ім'я/пароль - вертається <True>;
       якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>, інакше (<silent> == <False>) - породжується виключення LoginException
"""

class LoginException(Exception):
    pass

def userfunk(username, password, silent = False):
    dict_1 = {username: password}
    dict_user = {'valya': 'abc123', 'zoia': '5555', 'agahan': '9876', 'vova': '1111', 'julia': '2468'}
    if password == dict_user.get(username) :
        return True
    else:
        if silent == False:
            raise LoginException("Ooooupsss! Try again ")
        else:
            return False
        


print(userfunk('valya', 'abc1233', False))
print(userfunk('zoia', '5555'))
print(userfunk('vova', 'abc1233', True))


