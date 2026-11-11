## Assignment 01:
#Write a program that asks the user for the number of a month and prints the corresponding season: `spring`, `summer`, `autumn`, or `winter`. The seasons are stored in a tuple, and we can define each season to last for three months, with December being the first month of winter.
#**Example:**
#- Input: `12` (December)
#- Output: `Winter`

seasons = ("winter", "spring", "summer", "autumn")
month = int(input("Please Enter the number of a month : "))
season = seasons[(month % 12) // 3]
print(f"The corresponding season is {season}")
