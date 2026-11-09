#Design a program that continuously converts inches to centimeters,
# stopping only when the user enters a negative value.
CM_PER_INCH = 2.54  #1inch=2.54cm

while True:
    inches = float(input("Please enter inches (negative value to stop): "))

    if inches < 0:
        break

    cm = inches * CM_PER_INCH
    print(f"{inches} inches = {cm:.2f} cm")

print("Goodbye!")