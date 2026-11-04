#Write a program that prompts a fisher for the length of a zander in centimeters.
#If the zander is below the legal size limit, the program should instruct the fisher to release it back into the lake and tell them how many centimeters short the fish is of the limit.
#A zander must be at least 42 centimeters long to be kept.

Length_of_Zander = float(input("Please enter the length of zander in centimeters: "))

if Length_of_Zander < 42:
    short_of_zander = 42 - Length_of_Zander
    print(f"Please release the zander back to the lake")
    print(f"The Zander is {short_of_zander} centimeters below the legal size ")
else:
    print(f"The Zander can be kept ")