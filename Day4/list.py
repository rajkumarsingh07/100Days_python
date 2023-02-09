# fruits = [item1, item2]
# state1 = UP
# state2 = MH 

#offset start from 0 to 1,2,3, Thats why index 0 is 1st value of list
states_of_India = ["UP", "MH","MP", "RJ", "TN","KA" ]
#It will print itirate in the list from start to end value
print(states_of_India[0])
print(states_of_India[1])
print(states_of_India[2])
print(states_of_India[3])
print(states_of_India[4])
print(states_of_India[5])

print("\n")

#It will print itirate in the list from end to start value
print(states_of_India[-1])
print(states_of_India[-2])
print(states_of_India[-3])
print(states_of_India[-4])
print(states_of_India[-5])

#If i want to replace the value of list like MP to GOA
states_of_India[2] = "GOA"

print(f"updated states are {states_of_India}")

states_of_India.append("BIHAR") # append actually add the item in end of the list
print(f"updated states are {states_of_India}")

states_of_India.extend(["DELHI","Haryana"]) #it will add the at the end of the list
print(f"Updated states are {states_of_India}")

