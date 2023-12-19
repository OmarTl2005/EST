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

mois = int(input("Saisie un mois(nombre): "))
année = int(input("Saisie une année: "))

def mois_et_année(mois, année):
    month, year = 0, 0
    
    if(bissextile(année) == 1):
        year = 366
    else:
        year = 365
        month = 28

    if(has30(mois) == 1):
        month = 30
    elif(has31(mois) == 1):
        month = 31
    else:
        month = 29
    
    
    print(f"L'année {année} est de {year} jours, et le mois {mois} est de {month} jours.")

mois_et_année(mois, année)
