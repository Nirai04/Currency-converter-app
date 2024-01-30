def credit(database):
    print("\t\t\tCredits")
    print("\t\t\t-------")
    col=database["credits"]

    for i,k in enumerate(col.find({})):
        print(i+1,".",k["name"],"-",k["designation"],"-",k["year"], sep="")
    input()
    c = col.find({"_id": credits})
    

    print()
    input() 

def credit(database):
    print("\t\t\tCredits")
    print("\t\t\t-------")
    col=database["credits"]

    for i,k in enumerate(col.find({})):
        print(i+1,".",k["name"],"-",k["designation"],"-",k["year"], sep="")
    input()
    c = col.find({"_id": credits})
    

    print()
    input() 
