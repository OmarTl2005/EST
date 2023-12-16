def has30(mounth):
    if(mounth == 4 or mounth == 6 or mounth == 9 or mounth == 11):
        return 1
    else:
        return 0

def has31(mounth):
    if(mounth == 1 or mounth == 3 or mounth == 5 or mounth == 7 or mounth == 8 or mounth == 10 or mounth == 12):
        return 1
    else:
        return 0

def bissextile(year):
    if((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        return 1
    else:
        return 0

