name  = input("What is your name? ")
length = len(name)
print(length)

a = 4
b = 5
#need to print replacment of the value
a, b = b,a
print(a)
print(b)

print("   OR   ")
c = a
a  = b
b = c
print(a)
print(b)