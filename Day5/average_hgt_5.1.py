student_heights_input = input("Input a list of Students Heights: " )
student_heights = student_heights_input.split() # it will print the given input into a list

total_height = 0
for height in student_heights:
    total_height +=  int(height)
print(f"total sum is: {total_height}")

no_of_students = 0
for student in student_heights:
    no_of_students += 1
print(f"total no of student is: {no_of_students}")

average_height = round(total_height / no_of_students)
print(f"Average height per student is: {average_height}")

#We can use len() and sum() function to do the same
