from pymongo.mongo_client import MongoClient
import os

from convert import convert
from credits import credit
from add_country import add
from update import update

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

uri = "mongodb+srv://niraimathi:niraimathi@cluster0.y2ixacg.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

db_name = "currency_converter_app"
database = client[db_name]


os.system("color 0E")

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

while True:
    option = menu()
    if option == 1:
        os.system("cls")
        convert(database)
        option = menu()
    elif option == 2:
        os.system("cls")
        add(database)
        option=menu()
    elif option ==3:
        os.system("cls")
        update(database)
        option=menu()
    elif option==4:
        os.system("cls")
        credit(database)

        option=menu()
    elif option==5:
        print("Thank you for using this app")
        input()
        os.system("cls")
        break
    else:
        print("\nPlease enter a valid option from 1 to 5")
        input("\nRedirected to Menu")

    
            
