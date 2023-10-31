heure = int(input("Saisie l'heure(en 24h): "))
min = int(input("Saisie les minutes: "))

if (min >= 0 and min <= 58):
    print(heure,"h",min + 1,"min")
else:
    print(heure + 1,"h", min - min, "min")