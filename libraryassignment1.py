notDone= True


year=2022

album2 = {
    "Name": "_",
    "DateOfRelease": "_",
    "Band": "_",
}

album1 = {
    "Name": "_",
    "DateOfRelease": "_",
    "Band": "_",
}
album3 = {
    "Name": "_",
    "DateOfRelease": "_",
    "Band": "_",
}

album4 = {
    "Name": "_",
    "DateOfRelease": "_",
    "Band": "_",
}

album5 = {
    "Name": "_",
    "DateOfRelease": "_",
    "Band": "_",
}

album6 = {
    "Name": "_",
    "DateOfRelease": "_",
    "Band": "_",
}

album7 = {
    "Name": "_",
    "DateOfRelease": "_",
    "Band": "_",
}

album8 = {
    "Name": "_",
    "DateOfRelease": "_",
    "Band": "_",
}

album9 = {
    "Name": "_",
    "DateOfRelease": "_",
    "Band": "_",
}

album10 = {
    "Name": "_",
    "DateOfRelease": "_",
    "Band": "_",
}

album11 = {
    "Name": "_",
    "DateOfRelease": "_",
    "Band": "_",
}
album12 = {
    "Name": "_",
    "DateOfRelease": "_",
    "Band": "_",
}
album13 = {
    "Name": "_",
    "DateOfRelease": "_",
    "Band": "_",
}
album14 = {
    "Name": "_",
    "DateOfRelease": "_",
    "Band": "_",
}
album15 = {
    "Name": "_",
    "DateOfRelease": "_",
    "Band": "_",
}
album16 = {
    "Name": "_",
    "DateOfRelease": "_",
    "Band": "_",
}
album17 = {
    "Name": "_",
    "DateOfRelease": "_",
    "Band": "_",
}
album18 = {
    "Name": "_",
    "DateOfRelease": "_",
    "Band": "_",
}
album19 = {
    "Name": "_",
    "DateOfRelease": "_",
    "Band": "_",
}
album20 = {
    "Name": "_",
    "DateOfRelease": "_",
    "Band": "_",
}
while notDone:
    Answer = input("press 1 to enter album library, press 2 to view it and press 3 if you wish to quit: ")
    if Answer == "2":
        print('your library is currently empty please go back and add an album')
    if Answer == "3":
        notDone = False
    else:
        print('Entering library')
        album1["Name"] = input("Enter album name: ")
        album1["DateOfRelease"] =int(input("Enter date of release:"))
        album1["Band"] = input("Enter the Band name: ")
        print(f'this was released {year - album1["DateOfRelease"] } years ago by {album1["Band"]}')
        Answer = input("Press 1 to enter another album, press 2 to view your last entry and press 3 if you wish to quit: ")
    if Answer == "2":
        print(album1)
    if Answer == "3":
        notDone = False
    else:
        print('Entering library')
        album2["Name"] = input("Enter album name: ")
        album2["DateOfRelease"] =int(input("Enter date of release: "))
        album2["Band"] = input("Enter the Band name: ")
        print(f'this was released {year - album2["DateOfRelease"] } years ago by {album2["Band"]}')
        Answer = input("Press 1 to enter another album, press 2 to view your last entry and press 3 if you wish to quit: ")
    if Answer == "2":
        print(album2)
    if Answer == "3":
        notDone = False
    else:
        print('Entering library')
        album3["Name"] = input("Enter album name: ")
        album3["DateOfRelease"] = int(input("Enter date of relase: "))
        album3["Band"] = input("Enter the Band name: ")
        print(f'this was released {year - album3["DateOfRelease"] } years ago by {album3["Band"]}')
        Answer = input("Press 1 to enter another album, press 2 to view your last entry and press 3 if you wish to quit: ")
    if Answer == "2":
        print(album3)
    if Answer == "3":
        notDone = False
    else:
        print('Entering library')
        album4["Name"] = input("Enter album name: ")
        album4["DateOfRelease"] = int(input("Enter date of relase: "))
        album4["Band"] = input("Enter the Band name: ")
        print(f'this was released {year - album4["DateOfRelease"] } years ago by {album4["Band"]}')
        Answer = input("Press 1 to enter another album, press 2 to view your last entry and press 3 if you wish to quit: ")
    if Answer == "2":
        print(album4)
    if Answer == "3":
        notDone = False
    else:
        print('Entering library')
        album5["Name"] = input("Enter album name: ")
        album5["DateOfRelease"] = int(input("Enter date of relase: "))
        album5["Band"] = input("Enter the Band name: ")
        print(f'this was released {year - album5["DateOfRelease"] } years ago by {album5["Band"]}')
        Answer = input("Press 1 to enter another album, press 2 to view your last entry and press 3 if you wish to quit: ")
    if Answer == "2":
        print(album5)
    if Answer == "3":
        notDone = False
    else:
        print('Entering library')
        album6["Name"] = input("Enter album name: ")
        album6["DateOfRelease"] = int(input("Enter date of relase: "))
        album6["Band"] = input("Enter the Band name: ")
        print(f'this was released {year - album6["DateOfRelease"] } years ago by {album6["Band"]}')
        Answer = input("Press 1 to enter another album, press 2 to view your last entry and press 3 if you wish to quit: ")
    if Answer == "2":
        print(album6)
    if Answer == "3":
        notDone = False
    else:
        print('Entering library')
        album7["Name"] = input("Enter album name: ")
        album7["DateOfRelease"] = int(input("Enter date of relase: "))
        album7["Band"] = input("Enter the Band name: ")
        print(f'this was released {year - album7["DateOfRelease"] } years ago by {album7["Band"]}')
        Answer = input("Press 1 to enter another album, press 2 to view your last entry and press 3 if you wish to quit: ")
    if Answer == "2":
        print(album7)
    if Answer == "3":
        notDone = False
    else:
        print('Entering library')
        album8["Name"] = input("Enter album name: ")
        album8["DateOfRelease"] = int(input("Enter date of relase: "))
        album8["Band"] = input("Enter the Band name: ")
        print(f'this was released {year - album8["DateOfRelease"] } years ago by {album8["Band"]}')
        Answer = input("Press 1 to enter another album, press 2 to view your last entry and press 3 if you wish to quit: ")
    if Answer == "2":
        print(album8)
    if Answer == "3":
        notDone = False
    else:
        print('Entering library')
        album9["Name"] = input("Enter album name: ")
        album9["DateOfRelease"] = int(input("Enter date of relase: "))
        album9["Band"] = input("Enter the Band name: ")
        print(f'this was released {year - album9["DateOfRelease"] } years ago by {album9["Band"]}')
        Answer = input("Press 1 to enter another album, press 2 to view your last entry and press 3 if you wish to quit: ")
    if Answer == "2":
        print(album9)
    if Answer == "3":
        notDone = False
    else:
        print('Entering library')
        album10["Name"] = input("Enter album name: ")
        album10["DateOfRelease"] = int(input("Enter date of relase: "))
        album10["Band"] = input("Enter the Band name: ")
        print(f'this was released {year - album10["DateOfRelease"] } years ago by {album10["Band"]}')
        Answer = input("Press 1 to enter another album, press 2 to view your last entry and press 3 if you wish to quit: ")
    if Answer == "2":
        print(album10)
    if Answer == "3":
        notDone = False
    else:
        print('Entering library')
        album11["Name"] = input("Enter album name: ")
        album11["DateOfRelease"] = int(input("Enter date of relase: "))
        album11["Band"] = input("Enter the Band name: ")
        print(f'this was released {year - album11["DateOfRelease"] } years ago by {album11["Band"]}')
        Answer = input("Press 1 to enter another album, press 2 to view your last entry and press 3 if you wish to quit: ")
    if Answer == "2":
        print(album11)
    if Answer == "3":
        notDone = False
    else:
        print('Entering library')
        album12["Name"] = input("Enter album name: ")
        album12["DateOfRelease"] = int(input("Enter date of relase: "))
        album12["Band"] = input("Enter the Band name: ")
        print(f'this was released {year - album12["DateOfRelease"] } years ago by {album12["Band"]}')
        Answer = input("Press 1 to enter another album, press 2 to view your last entry and press 3 if you wish to quit: ")
    if Answer == "2":
        print(album12)
    if Answer == "3":
        notDone = False
    else:
        print('Entering library')
        album13["Name"] = input("Enter album name: ")
        album13["DateOfRelease"] = int(input("Enter date of relase: "))
        album13["Band"] = input("Enter the Band name: ")
        print(f'this was released {year - album13["DateOfRelease"] } years ago by {album13["Band"]}')
        Answer = input("Press 1 to enter another album, press 2 to view your last entry and press 3 if you wish to quit: ")
    if Answer == "2":
        print(album13)
    if Answer == "3":
        notDone = False
    else:
        print('Entering library')
        album14["Name"] = input("Enter album name: ")
        album14["DateOfRelease"] = int(input("Enter date of relase: "))
        album14["Band"] = input("Enter the Band name: ")
        print(f'this was released {year - album14["DateOfRelease"] } years ago by {album14["Band"]}')
        Answer = input("Press 1 to enter another album, press 2 to view your last entry and press 3 if you wish to quit: ")
    if Answer == "2":
        print(album14)
    if Answer == "3":
        notDone = False
    else:
        print('Entering library')
        album15["Name"] = input("Enter album name: ")
        album15["DateOfRelease"] = int(input("Enter date of relase: "))
        album15["Band"] = input("Enter the Band name: ")
        print(f'this was released {year - album15["DateOfRelease"] } years ago by {album15["Band"]}')
        Answer = input("Press 1 to enter another album, press 2 to view your last entry and press 3 if you wish to quit: ")
    if Answer == "2":
        print(album15)
    if Answer == "3":
        notDone = False
    else:
        print('Entering library')
        album16["Name"] = input("Enter album name: ")
        album16["DateOfRelease"] = int(input("Enter date of relase: "))
        album16["Band"] = input("Enter the Band name: ")
        print(f'this was released {year - album16["DateOfRelease"] } years ago by {album16["Band"]}')
        Answer = input("Press 1 to enter another album, press 2 to view your last entry and press 3 if you wish to quit: ")
    if Answer == "2":
        print(album16)
    if Answer == "3":
        notDone = False
    else:
        print('Entering library')
        album17["Name"] = input("Enter album name: ")
        album17["DateOfRelease"] = int(input("Enter date of relase: "))
        album17["Band"] = input("Enter the Band name: ")
        print(f'this was released {year - album17["DateOfRelease"] } years ago by {album17["Band"]}')
        Answer = input("Press 1 to enter another album, press 2 to view your last entry and press 3 if you wish to quit: ")
    if Answer == "2":
        print(album17)
    if Answer == "3":
        notDone = False
    else:
        print('Entering library')
        album18["Name"] = input("Enter album name: ")
        album18["DateOfRelease"] = int(input("Enter date of relase: "))
        album18["Band"] = input("Enter the Band name: ")
        print(f'this was released {year - album18["DateOfRelease"] } years ago by {album18["Band"]}')
        Answer = input("Press 1 to enter another album, press 2 to view your last entry and press 3 if you wish to quit: ")
    if Answer == "2":
        print(album18)
    if Answer == "3":
        notDone = False
    else:
        print('Entering library')
        album19["Name"] = input("Enter album name: ")
        album19["DateOfRelease"] = int(input("Enter date of relase: "))
        album19["Band"] = input("Enter the Band name: ")
        print(f'this was released {year - album19["DateOfRelease"] } years ago by {album19["Band"]}')
        Answer = input("Press 1 to enter another album, press 2 to view your last entry and press 3 if you wish to quit: ")
    if Answer == "2":
        print(album19)
    if Answer == "3":
        notDone = False
    else:
        print('Entering library')
        album20["Name"] = input("Enter album name: ")
        album20["DateOfRelease"] = int(input("Enter date of relase: "))
        album20["Band"] = input("Enter the Band name: ")
        print(f'this was released {year - album20["DateOfRelease"] } years ago by {album20["Band"]}')
        Answer = input("Your outa space  please press 2 to view your last entry and press 3 if you wish to quit: ")
    if Answer == "2":
        print(album20)
    if Answer == "3":
        notDone = False
        break
print("You have ran outa space in this library go buy more storage.")
    
       

       
       
       

       
       
       

       


    
       

        
       


       

       
       
       

       
       
       

       


    
       

        
       

       
       
       

       


    
       

       



        













        













        
















       
        







