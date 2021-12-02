"""
2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
   - щось своє :)
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
"""

class LoginException(Exception):
    pass


def registration(username, password):   
    if 3  > len(username) > 50 or len(password) < 8 :
        raise LoginException("Oupss! You entered a short username or password")
    if any(map(str.isdigit, password)) == False:
        raise LoginException("Oupss! Password should contain a number")
    if 'a' in password:
        raise LoginException("Oupss! Enter password without letter 'a' ")
    return True


print(registration('zoia', 'bbbbbbb1'))
