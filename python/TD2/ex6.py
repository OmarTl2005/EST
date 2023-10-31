year = int(input("Entrer l'année pour savoir si est-il bissextile où pas: "))

if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
    print(year,"est une année bissextile.")
else:
    print(year,"n'est pas une année bissextile.")