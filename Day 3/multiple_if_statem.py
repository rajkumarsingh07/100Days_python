print("Welcome to the rollercoaster!")
height = int(input("Whats your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter the age:"))
    if age < 12:
        bill = 5 
        print("Please pay $5")
    elif age <= 18:  
        bill = 7                  
        print("you have to pay $7.")
    else:
        bill = 12  
        print("you have to pay $12.")
    wants_photo  = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill +=3
        print(f"your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride")