devoir = [[int(input("Saisie la {} note du devoir {} : ".format(j + 1, i + 1))) for i in range(2)] for j in range(30)]
moyenne = 0
moyenne_perso = 0
count = 0

for i in range(30):
    for j in range(2):
        moyenne = (moyenne + ((devoir[i][j]) / 2 ))

moyenne = moyenne / 30
print("La moyenne est: ", moyenne)

for i in range(30):
    for j in range(2):
        moyenne_perso = moyenne_perso + (devoir[i][j] / 2)
        if (moyenne_perso > moyenne):
            count = count + 1
    moyenne_perso = 0
print("Le nombre des moyennes supérieures à la moyenne de la classe: ", count)