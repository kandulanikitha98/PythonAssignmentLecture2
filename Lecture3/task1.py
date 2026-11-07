#Create a program using a while loop that prints all numbers divisible by three within the range of 1 to 1000.
number = 1

while number in range(1, 1001):
    if number % 3 == 0:
        print(f"{number} is divisible by 3")
    number += 1
