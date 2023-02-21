#need to add all even numvers between 1 to 100 including both value
even_no = 0
for number in range(2,101,2):
    even_no += number
print(f"addition of even number between 1 to 100 is: {even_no}\n")

print("Second Method\n")

total_no_2 = 0
for number in range(1,101):
    if number % 2 == 0:
        total_no_2 += number
print(f"addition of even number between 1 to 100 is: {total_no_2}")