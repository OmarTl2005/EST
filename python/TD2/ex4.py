nombre = int(input("Entrez un nombre entier: "))
# Vérifier si le bit de poids faible est défini (1 pour impair, 0 pour pair)
if nombre & 1:
    print("Le chiffre" , nombre , "est impair.")
else:
    print("Le chiffre" , nombre , "est pair.")