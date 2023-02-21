#Actual condition
# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else:
#     do this

print("Welcome to the rollercoaster!")
height = int(input("Whats your height in cm? "))
#print(type(height))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter the age:"))
    if age < 18:                      #called nested if-else
        print("you have to pay $7.")
    else:
        print("you have to pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride")