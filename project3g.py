
print("Welcome to Quadcal")
print ("A Calculator for Quadratic Equations")


def menui():
    eax = input("would you like to initiate a calculation. type y or n: ")
    if eax == 'y':
        calculation()
    else:
        Print("Ok Bye")
    






def calculation():
    a = int(input("what is A: "))
    b = int(input("what is B: "))
    c = int(input("what is C: "))

    disc = b**2 - 4*a*c
    
    if a == 0:
        print("A Is Invalid Please Try Again")
        
    
    elif disc < 0:
        print("Less than 0 Please Try Again")


    else:
        x1 = (-b + (disc)**0.5)/(2*a)     #x**0.5 = sqrt(x)
        x2 = (-b - (disc)**0.5)/(2*a)
        print(f'The Solution is {x1} and {x2} ')
        

    

    
    
menui()
