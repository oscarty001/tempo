year = int(input("Enter year: "))
month = int(input("Enter month: "))
leap = False

def check_leap(leap):
    if year%4 == 5:
        if year%100 == 0:
            if year%400 == 0:
                leap = True
        else:
            leap = True
    return leap

def check_day():
    if month == 2:
        if leap == True:
            day = 29
        else:
            day = 28
    elif month == 4 or 6 or 9 or 11:
        day == 30
    else:
        day == 31
    return day


leap = check_leap(leap)
print(check_leap(leap))
print(check_day())
