#Write a program that asks the user to enter a year and tells them whether the year is a leap year.
# A year is a leap year if:
#It is divisible by 4, **and**
#If divisible by 100, it must also be divisible by 400.
Input_year = int(input("Please Enter a year: "))
if (Input_year % 4 == 0 and Input_year % 100 != 0) or (Input_year % 400 == 0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")