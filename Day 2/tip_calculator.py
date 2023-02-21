#Example:- If the bill was 200, split between 5 people with 12% tip 
print("Welcome to the top calculator!:)") 
bill = float(input("What was the total bill amount? INR "))
tip = int(input("How much tip would you like to give? 10,12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
#final_amount = round(bill_per_person, 2) #sometimes it will give output like 33.6 not 33.60 so need to google for 2digit outputs
final_amount = "{:.2f}".format(bill_per_person) # This will given you output till 2digit from dot link =>https://stackoverflow.com/questions/1995615/how-can-i-format-a-decimal-to-always-show-2-decimal-places
print(f"Each person should pay INR {final_amount}") #checking with 150,12,and 5people

