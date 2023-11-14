n = float(input("Saisie une valeur: "))
i = 1
total = 0

while(i <= n):
    total = ((-1) ** i)*(i ** 2 + i)
    i += 1
print("Le resultat du calcul est:", total)