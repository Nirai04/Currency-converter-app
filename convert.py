def convert(database):
    print("\t\t\tConvert")
    print("\t\t\t-------")
    print("These are the available countries:")
    col = database["countries"]

     
    for i,j in enumerate(col.find({}, {"country_name"})):
        print(i+1,".",j["country_name"],sep="")


    #print("\n1.France\n2.Cananda\n3.Great Britain\n4.New York\n5.China\n")

    country = input("\nFrom Country:")
    amount = float(input("\nAmount:"))

    c = col.find_one({"_id": int(country)})
    

    print(amount,c["symbol"],"equals to ", amount*c["conversion_rate"]," Indian rupees")
    input()