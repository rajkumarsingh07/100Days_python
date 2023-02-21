#Passwd Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', ';', ':', ',', '.', '/', '<', '>', '?', '\\', '|', '~']

print("Welcome to python password Generator")

nr_letters = int(input("How many letters would you like in your passwd?\n"))
nr_symbols = int(input("How many symbols would you like in your passwd?\n"))
nr_numbers = int(input("How many numbers would you like in your passwd?\n"))

#Easy_level:- 
passwd = " "
# range to 1 to 4
for char in range(1, nr_letters + 1): 
#  randon_char = random.choice(letters)
#  passwd = passwd + randon_char
   passwd += random.choice(letters)

for char in range(1, nr_symbols + 1): 
    passwd += random.choice(symbols)

for char in range(1, nr_numbers + 1): 
#    passwd += int(random.choice(numbers))
    randon_char = random.choice(numbers)
    passwd = passwd + str(randon_char)
print(f" Our final random passwd is: {passwd}")

#Hard_level:- 

# passwd_list = []
# for char in range(1, nr_letters + 1): 
#    passwd_list += random.choice(letters)
# for char in range(1, nr_symbols + 1): 
#     passwd_list += random.choice(symbols)
# for char in range(1, nr_numbers + 1): 
#     randon_char = random.choice(numbers)
#     passwd_list = str(passwd_list) + str(randon_char)
# print(passwd_list)

# #ramdom.shuffle()

# random.shuffle(passwd_list)
# print(passwd_list)


