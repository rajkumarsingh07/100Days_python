# BMI = (weight/height2(m2))
input_height = float(input("Enter your height in meter:"))
input_weight = float(input("Enter your weight in kg:"))

bmi = (input_weight)/(input_height ** 2)
print(bmi)
bmi_as_a_int = int(bmi)
print(bmi_as_a_int)
