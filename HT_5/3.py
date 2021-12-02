"""
3. На основі попередньої функції створити наступний кусок кода:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)
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


st = (('iv', 'ivanov111'),
      ('vasya', 'pupkinpupkin11'),
      ('petro', 'petrovvvvv'),
      ('ivan', 'iv'))

for name_user, password_user in st:
    try:
        if registration(name_user, password_user):
            print (f' Name: {name_user} \n Password: {password_user} \n Status: Ok \n')
    except LoginException as error404:
        print (f' Name: {name_user} \n Password: {password_user} \n Status: {error404} \n')
