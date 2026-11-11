airports = {} #dictionary

while True:
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    user_choice = input("Choose an option: ") #input

    if user_choice == "1":
        icao = input("Enter ICAO code: ")
        airport = input("Enter airport name: ")

        airports[icao] = airport
        print("Airport saved!")

    elif user_choice == "2":
        icao = input("Enter ICAO code: ")

        if icao in airports:
            print(airports[icao])
        else:
            print("Airport not found!")

    elif user_choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")

