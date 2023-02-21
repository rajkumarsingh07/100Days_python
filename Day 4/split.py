import random
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")
print(names)
#len()
num_items = len(names)
print(num_items)

# random_choice = random.randint(0, num_items - 1)
# print(random_choice)
# persion_who_will_pay = names[random_choice]
# print(persion_who_will_pay + "is going to buy the meal today")

#print( "OR" )

persion_who_will_pay = random.choice(names) #https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
print(persion_who_will_pay + "is going to buy the meal today")
