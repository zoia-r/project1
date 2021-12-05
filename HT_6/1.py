import time


def lamp(color, n):
    for i in range(n):
        print(color)
        time.sleep(1)

        
while True:
    lamp('Red        Green', 4)
    lamp('Yellow     Green', 2)
    lamp('Green      Red', 4)
    lamp('Yellow     Red', 2)
            

    
