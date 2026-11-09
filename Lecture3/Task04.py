import random
secret_number = (random.randint(1, 10))
attempts = 0
print("Iam thinking of a number between 1 and 10.")

while True:
    guess_number = int(input("Enter Your guess number: "))
    attempts += 1
    if guess_number > secret_number:
        print("Too high")
    elif guess_number < secret_number:
        print("Too low")
    else:
        print("Correct")
        print(f"You got it in {attempts} attempts.")
        break