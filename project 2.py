year = 2022
notDone =True
ntDne =True


about = ("alby is a album library to put your favorite albums it stores them in a list and allows you to look at them when you wish as well as add an infinite number of albums")
        
        
        
  
def enterAlbum():
    Name = input("Please enter the name of this album: ")
    DateOfRelease = input("Please enter the year of release: ")
    Band = input("Please enter the name of the band: ")
    f = open("albumListA.txt","a")
    f.write("---------------------")
    f.write('\n')
    f.write(Name)
    f.write('\n')
    f.write(DateOfRelease)
    f.write('\n')
    f.write(Band)
    f.write('\n')
    f.close()
    file = open("titlelistA.txt","a")
    file.write(Name)
    file.write('\n')
    f.close()
    print(f'{Name} was released {year - int(DateOfRelease)} years ago by {Band}.')
    minimenu()


def readTitles():
    print("Reading titles.")
    file = open("titlelistA.txt","r")
    for each in file:
          print (each)




def readAlbums():
    print("Reading albums.")
    file = open("albumListA.txt","r")
    for each in file:
        print (each)
     

def menu():
    option = input("Press 1 to enter album library, press 2 to see all entries, press 3 to print album names and press 0 to exit to title screen.: ")
    if option == "2":
          readAlbums()
    if option == "3":
          readTitles()
    if option == "1":
         print('Entering library')
         enterAlbum()
    if option == "0":
        print("Returning to title screen")
        
   

while ntDne:
    print("--Alby--")
    print("Title Screen")
    choice = input("Would you like to continue to the program (1.) see the about info (2.) or quit from here (0.)")
    if choice == "1":
        print("Proceeding to program")
        menu()
    if choice == "0":
        print("You have quit")
        ntDne=False
    if choice == "2":
        print (about)
    
    
   

print("Ended")
    


