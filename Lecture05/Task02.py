def gallons_to_liters(gallons):
    return gallons * 3.785  #1 US gallon = 3.785 litres

def main():
    while True:
        gallons = float(input("Enter gallons: "))
        if gallons < 0:
            break
        liters = gallons_to_liters(gallons)
        print(f"{liters:.2f} liters")

main()