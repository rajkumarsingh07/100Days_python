#max()
#min()


student_scores= input("Input a list of students scores:").split()
print(student_scores)
# print(max(student_scores)) #this is easy to use above function and do it

highest_score = 0
for score in student_scores:
    if int(score) > highest_score:
       highest_score = int(score)
print(f"Highest score is: {highest_score}")




