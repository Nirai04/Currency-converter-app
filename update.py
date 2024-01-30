def update(database):
        print("\t\t\tUpdate")
        print("\t\t\t------")
        #print("\nThese are the available countries:\n1.France\n2.Cananda\n3.UK\n4.USA\n5.Europe\n\n\nCountry:\nUpdated value:")
        col = database["countries"]
        for i,j in enumerate(col.find({}, {"country_name","conversion_rate"})):
                print(i+1,".",j["country_name"],"-",j["conversion_rate"],sep="")
        
        country = input("\nFrom Country:")
        amount = float(input("\nUpdated Amount:"))
        c = col.update_one({"_id": int(country)}, {"$set":{"conversion_rate":float(amount)}})
        print("Updated amount successfully")

