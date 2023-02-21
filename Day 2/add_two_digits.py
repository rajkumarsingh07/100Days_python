#Enter any two digit number and need output of after added them each number like 35 the 3+5=8
two_digit_number = input("type two digit number: ")
print(type(two_digit_number))
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

print(first_digit)
print(second_digit)
result = int(first_digit) + int(second_digit ) #convert from str to intger to get each number addition
print(result)