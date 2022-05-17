global Shift
Shift = 4









def menu():
    global Shift
    elem= input("Welcome to Cecipr. What do you wish to do first(1.)Change letter shift amount(2.)Encrypt Message(3.)Decrypt Message(4.)Quit: ")
    if elem == "1":
       Shift = int(input("How many letters over do you wish to shift: "))
       print(f"the shift is now {Shift}")
       menu()
       return Shift
    if elem == "2":
        encryptFull()
    if elem == "3":
        print("This feature has yet to be added. Please look forward to it in a future update.")
        menu()
    if elem == "4":
        print("You have quit")
       


    
def encryptM(t):
    global Shift
    cip = int(ord(t)) + (Shift)
    return chr(cip)
   

def encryptFull():
    out=''
    fern = input("Enter your Message: ")
    for letter in fern:
        out+=(encryptM(letter))
    print(out)
    menu()
        



menu()



