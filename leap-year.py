year = int (input ('Enter The 4-Digit Year To Learn If It Is Leap Year Or Not: '))
if year % 4 == 0 and year % 100 == 0:
    if year % 400 == 0:
        print(f"{year} is LEAP YEAR.")
    else:
        print(f"{year} is NOT LEAP YEAR. ")
elif year % 4 == 0:
    print(f"{year} is LEAP YEAR.")
else:
    print(f"{year} is NOT LEAP YEAR. ")
