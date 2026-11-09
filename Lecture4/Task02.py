numbers = []
while True:
    user_input = input("Please Enter a number: ")
    if user_input == "":
        break
    numbers.append(int(user_input))
numbers.sort(reverse=True)
print("Five greatest numbers in descending order: ")

for number in numbers[:5]:
    print(number)