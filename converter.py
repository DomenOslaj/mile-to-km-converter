print "Hallo, this is a unit converter that converts kilometers into miles. "

while True:
    km = raw_input("Please enter number of kilometers. ")

    try:
        km = float(km)              #try if number or string
        miles = km * 0.621371
        print miles

        choice = raw_input("Would you like to do another conversion (y/n): ")

        if choice == "n":
            print "Thank you for using our converter."
            break


    except:          #if string
        print "Please enter numbers only. "

