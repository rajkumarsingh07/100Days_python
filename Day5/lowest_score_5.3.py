#min()
student_scores= input("Input a list of students scores:").split()
print(student_scores)
# print(min(student_scores)) #this is easy to use above function and do it

lowest_score = 0
for score in student_scores:
    if int(score) < lowest_score:
       lowest_score = int(score)
print(f"lowest score is: {lowest_score}")
