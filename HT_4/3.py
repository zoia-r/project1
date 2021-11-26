"""
3. Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000,
и яка вертатиме True, якщо це число просте, и False - якщо ні.
"""
def is_prime(n):
    for i in range (2, n):
        if n%i ==0:
            return False
    return True

        
number = int(input("Please, enter the number: "))
print(is_prime(number))
    
