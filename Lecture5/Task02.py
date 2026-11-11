names = set() #set will automatically deletes the duplicates
while True:
    name = input("Please enter a name: ")
    if name == "":
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

for name in names:
    print(name)



