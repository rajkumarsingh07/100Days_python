##Actual condition(if we need to check atleast 3 condition then we have to use if-elif-else)
#condition is like 1). age <12, 2). age is between 12-18, 3). age > 18
# if condition:
#     if another condition:
#         do this
#     elif:
#        do this
#     else:
#         do this
# else:
#     do this

print("Welcome to the rollercoaster!")
height = int(input("Whats your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter the age:"))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:                    
        print("you have to pay $7.")
    else:
        print("you have to pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride")