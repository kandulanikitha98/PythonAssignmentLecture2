import random
num_of_dice = int(input("Please enter how many dice you want to roll: "))
total = 0

for i in range(num_of_dice):
    roll = random.randint(1, 6)
    print(f"Dice {i + 1}: {roll}")
    total += roll
print(f"The sum is {total}.")

