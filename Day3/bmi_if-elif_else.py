# BMI = (weight/height2(m2))
input_height = float(input("Enter your height in meter:"))
input_weight = float(input("Enter your weight in kg:"))
bmi = round(input_weight)/(input_height ** 2)
bmi_as_a_int = int(bmi)
print(bmi_as_a_int)

if bmi < 18.5:
    print(f"your bmi is {bmi},you are underweight")
elif bmi < 25:
    print(f"your bmi is {bmi},you are normal weight")
elif bmi < 30:
    print(f"your bmi is {bmi},you are overweight")
elif bmi < 35:
    print(f"your bmi is {bmi},you are obese")
else:
    print(f"your bmi is {bmi},you are clinically obese")
