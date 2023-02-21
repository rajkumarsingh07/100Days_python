#For leap year, year should be divisiable by 4, 
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"given year {year} is a leap year")
        else:
            print(f"given year {year} is not a leap year")
    else:
        print(f"given year {year} is a leap year")
else:
    print(f"given year {year} is not a leap year")