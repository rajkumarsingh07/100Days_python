import random 
random_integer = random.randint(1, 9) # it will include the 1st and last number , visit https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
print(random_integer)

random_float = random.random() #bydefault start value is 0 and end is 1.0 so random float value will be vary in between this range
print(random_float)

randomFloat = random_float * 5 # if i need the range from 1 to 5
print(randomFloat)

love_score = random.randint(1,100)
print(f"Your love scrore value is: {love_score} ")