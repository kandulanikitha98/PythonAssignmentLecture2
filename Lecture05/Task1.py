import random
def roll_dice():
    return random.randint(1, 6)
def main():
    result=0
    while True:
        if result==6:
            break
        result = roll_dice()
        print(result)
main()