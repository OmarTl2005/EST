chiffre = int(input("Saisir le chiffre d'affaires: "))

if (chiffre <= 150000):
    print("Le chiffre d'affaires", chiffre, "à 0% de prime")
elif (chiffre > 150000 and chiffre <= 500000):
    print("Le chiffre d'affaires", chiffre, "à 1% de prime alors", chiffre * 0.01 ,"est le prime du commercial")
else:
    print("Le chiffre d'affaires", chiffre, "à 2% de prime alors", chiffre * 0.02 ,"est le prime du commercial")