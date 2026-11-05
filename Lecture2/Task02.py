#Create a program that asks the user to input the cabin class on a cruise ship and prints the corresponding description based on the following list:
#- **LUX**: Upper-deck cabin with a balcony.
#- **A**: Cabin above the car deck with a window.
#- **B**: Windowless cabin above the car deck.
#- **C**: Windowless cabin below the car deck.
#You must use an **if**/**elif**/**else** structure in your solution. If the user inputs an invalid class, the program should output: `Invalid cabin class`.

cruise_cabin_class =input("User please enter cabin class on a cruise ship: ")
if cruise_cabin_class== "LUX":
    print(f"upper-deck cabin with a balcony")
elif cruise_cabin_class=="A":
    print(f"Cabin above the car deck with a window")
elif cruise_cabin_class=="B":
    print(f"Windowless cabin above the car deck")
elif cruise_cabin_class=="C":
    print(f"Windowless cabin below the car deck")
else:
    print(f"Invalid cabin class")
