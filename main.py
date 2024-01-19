import os

os.system("cls")
print(
    '''
   ____   _   _   ____    ____    _____   _   _    ____  __   __  
  / ___| | | | | |  _ \  |  _ \  | ____| | \ | |  / ___| \ \ / /  
 | |     | | | | | |_) | | |_) | |  _|   |  \| | | |      \ V /   
 | |___  | |_| | |  _ <  |  _ <  | |___  | |\  | | |___    | |    
  \____|  \___/  |_| \_\ |_| \_\ |_____| |_| \_|  \____|   |_|    

   ____    ___    _   _  __     __  _____   ____    _____   _____   ____    
  / ___|  / _ \  | \ | | \ \   / / | ____| |  _ \  |_   _| | ____| |  _ \   
 | |     | | | | |  \| |  \ \ / /  |  _|   | |_) |   | |   |  _|   | |_) |  
 | |___  | |_| | | |\  |   \ V /   | |___  |  _ <    | |   | |___  |  _ <   
  \____|  \___/  |_| \_|    \_/    |_____| |_| \_\   |_|   |_____| |_| \_\  

     _      ____    ____  
    / \    |  _ \  |  _ \ 
   / _ \   | |_) | | |_) |
  / ___ \  |  __/  |  __/ 
 /_/   \_\ |_|     |_|    
                          
                                                                            
'''
)


os.system("color 8B");

def menu():
    os.system("cls")
    print()
    print()
    print("\t\t\tMENU")
    print("\t\t\t----")
    print("1. Convert")
    print("2. Add country")
    print("3. Update")
    print("4. Credits")
    print("5. Exit")
    return int(input("Enter your option: "))

print("\n\n")
print("Press anykey to continue...", end="")
input()

option = menu()
while option != 5:
    if option == 1:
        os.system("cls")
        print("\t\t\tConvert")
        print("\t\t\t-------")
        print("These are the available countries:\n1.France\n2.Cananda\n3.UK\n4.USA\n5.Europe\n\n\nFrom Country:\nAmount:")
        input()
        option = menu()
    if option == 2:
        os.system("cls")
        print("\t\t\tAdd country")
        print("What are the countries you want to add ?\nVALUE:")
        input()
        option=menu()
    if option ==3:
        os.system("cls")
        print("\t\t\tUpdate")
        print("\t\t\t------")
        print("\nAmount:\nConverted Amount:")
        input()
        option=menu()
    if option==4:
        os.system("cls")
        print("\t\t\tCredits")
        print("\t\t\t-------")
        input()
        option=menu()
    if option==5:
        print("Thank you for using this app")
        input()
        os.system("cls")
    
            
