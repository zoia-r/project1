def fibonacci(n):
    n_1 = 0
    n_2 = 1
    print(n_1)
    print(n_2)
  
    while n > n_2:
        s = n_1 + n_2
        n_1 = n_2
        n_2 = s  
        print(s)


number = int(input("Enter the number: "))
fibonacci(number)
    
        
        
        
