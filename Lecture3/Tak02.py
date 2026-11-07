#Design a program that continuously converts inches to centimeters,
# stopping only when the user enters a negative value.

CM_PER_INCH = 2.54    # inches = centimeters / 2.54, 1 cm = 1 / 2.54 ≈ 0.3937 inches.
inches = float(input(" Please Enter inches(stop when negative value) : "))
while inches >= 0:
    print(f"{inches} inches = {inches * CM_PER_INCH:.2f} cm")
    inches = float(input("Please Enter inches(stop when negative value) : "))

print("Goodbye!")