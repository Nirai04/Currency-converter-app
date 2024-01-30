def add(database):
    print("\t\t\tAdd country")
    print("What are the countries you want to add ?")
          #\nCountry Name:\nSymbol:\nConversion Value:")

    cname = input("Country name:")          
    symbol = input("Symbol:")
    cvalue = input("Conversion value:")
    col = database["countries"]
    total = len(list(col.find()))
    c = col.insert_one({"_id":total+1,"country_name": cname,"symbol":symbol,"conversion_rate":float(cvalue)})
    print("Country added successfully")
    input()
