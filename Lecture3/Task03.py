#Write a program that prompts the user to enter numbers until they leave the input blank.
# Once the input stops, the program outputs the smallest and largest numbers entered.
numbers = []
while True:
    user_input = input("Please Enter a number: ")
    if user_input == "":
        break
    numbers.append(float(user_input))
if numbers:
    print(f"Smallest: {min(numbers)}")
    print(f"Largest: {max(numbers)}")
else:
    print("No numbers were entered.")
