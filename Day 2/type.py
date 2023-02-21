num_char  = len(input("Whats is your name?"))
print(type(num_char)) #getting int type
#print("Your name has " + num_char + "Charactor") #TypeError: can only concatenate str (not "int") to str
#We can only cancatenate strings

#So need to convert it first
new_num_char = str(num_char)
print("Your name has " + new_num_char + " Characters.")

a = 123
print(type(a)) #integer
b = str(234)
print(type(b)) #type string

c = float(123)
print(type(c))

print(70 + float("100.70")) 
print(str(70) + str(100)) #just concatinate
