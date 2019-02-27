print "Hallo, this is the unit converter that converts miles into kilometers. "

while True:
    km = raw_input("Please enter number of kilometers. ")

    try:
        km = float(km.replace(",", "."))              # try if number or string/replace comma with dot

        miles = km * 0.621371

        print miles

        choice = raw_input("Would you like to do another conversion (y/n): ")

        if choice.lower() == "n":
            print "Thank you for using our converter."
            break

        elif choice.lower() != "n" and choice.lower() != "y":
            print "I understand Y and N only!"

        else:
            continue

    except ValueError:         # if string
        print "Numbers only! "
