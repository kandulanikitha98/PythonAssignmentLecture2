#Design a program that asks the user for their biological gender and hemoglobin level (g/L).
# Based on the provided values, the program should inform the user if their hemoglobin is low, normal, or high.
# The normal ranges are:
#- For adult females: **117-155 g/L**.
#- For adult males: **134-167 g/L**.

user_Gender = input("Please enter your gender (Male/Female): ")
user_Hemoglobin = int(input("Please enter your hemoglobin level(g/L): "))

if user_Gender == "Male" and user_Hemoglobin < 134:
    print("Your Hemoglobin level is Low")
elif user_Gender == "Male" and user_Hemoglobin <= 167:
    print("Your Hemoglobin level is Normal")
elif user_Gender == "Male" and user_Hemoglobin > 167:
    print("Your Hemoglobin level is High")
elif user_Gender == "Female" and user_Hemoglobin < 117:
    print("Your Hemoglobin level is Low")
elif user_Gender == "Female" and user_Hemoglobin <= 155:
    print("Your Hemoglobin level is Normal")
elif user_Gender == "Female" and user_Hemoglobin > 155:
    print("Your Hemoglobin level is High")
else:
    print("Invalid gender")