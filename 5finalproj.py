
alphabet ={
        "a":0,
        "b":0,
        "c":0,
        "d":0,
        "e":0,
        "f":0,
        "g":0,
        "h":0,
        "i":0,
        "j":0,
        "k":0,
        "l":0,
        "m":0,
        "n":0,
        "o":0,
        "p":0,
        "q":0,
        "r":0,
        "s":0,
        "t":0,
        "u":0,
        "v":0,
        "w":0,
        "x":0,
        "y":0,
        "z":0,
        " ":0,
        ",":0,
        ":":0,
        "1":0,
        "2":0,
        "3":0,
        "4":0,
        "5":0,
        "6":0,
        "7":0,
        "8":0,
        "9":0,
        "0":0,
        ".":0,
        ";":0,
        '"':0,
        "'":0,
}

def greeting():
    print("welcome to Alpcount a useful tool when you wanna know how many of each letter is is in a piece of text")
    caltFull()


def caltFull():
    tex = input("Enter your Message: ").lower()
    for letter in tex:
        if letter not in tex:
            alphabet[letter] = 1
        else:
            alphabet[letter] = alphabet[letter]+1
    print(alphabet)





greeting()
