"""
2. Написати функцію, яка приймає два параметри: ім'я файлу та кількість символів.
   На екран повинен вивестись список із трьома блоками - символи з початку, із середини та з кінця файлу.
   Кількість символів в блоках - та, яка введена в другому параметрі.
   Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, ніж є в файлі (наприклад, файл із двох символів і треба вивести по одному символу, то що виводити на місці середнього блоку символів?)
   В репозиторій додайте і ті файли, по яким робили тести.
   Як визначати середину файлу (з якої брать необхідні символи) - кількість символів поділити навпіл, а отримане "вікно" символів відцентрувати щодо середини файла і взяти необхідну кількість. В разі необхідності заокруглення одного чи обох параметрів - дивіться на свій розсуд.
   Наприклад:
   █ █ █ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ ░ █ █ █    - правильно
                     ⏫ центр

   █ █ █ ░ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ █ █ █    - неправильно
                     ⏫ центр

"""

def print_list(name, count_number):
    with open(name, "r") as file:
        str1 = file.read()
        len_str1 = len(str1)
        if len_str1 < count_number*3:
            res = []
            n = ''
            centre_position = len_str1 // 2 - count_number // 2
            res.append(str1[:count_number])
            res.append(str1[centre_position: centre_position + count_number])
            res.append(str1[-count_number:])
            n = '*' * count_number
            res = n.join(res)
        else:
            count_space = len_str1 - count_number*3
            count_space_r = (count_space)//2
            count_space_l = count_space - count_space_r

            temp = count_number + count_space_l

            res = str1[:count_number]
            res += '*' * count_space_l
        
            res +=str1[temp: temp + count_number]
           
            res += '*' * count_space_r
            res += str1[-count_number:]
        print(res)


print_list('text1.txt', 4)


