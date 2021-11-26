"""
4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і
кінець діапазона, і вертатиме список простих чисел всередині цього діапазона.
"""
def prime_list(start, finish):
    list_1 = []
    for i in range (start, finish):
        is_prime = True 
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            list_1.append(i)
    return list_1


print(prime_list(1, 100))
