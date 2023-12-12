# A
from random import randint
matrix = [[randint(-102, 464) for i in range(4)] for j in range(10)]
print(matrix)

#B 

max, min, i_max, i_min = 0, 0, 0, 0

for i in range(10):
    for j in range(4):
        if(max < matrix[i][j]):
            max = matrix[i][j]
            i_max = "[{}][{}]".format(i, j)
        if(min > matrix[i][j]):
            min = matrix[i][j]
            i_min = "[{}][{}]".format(i, j)
print("max:", max, "rang de max:", i_max, "\nmin:", min, "rang de min:", i_min)

#C 
index = 0
max = 0
sum = []

for i in range(10):
    for j in range(4):
        max = max + matrix[i][j]
    sum.append(max)
    max = 0

max = sum[0]

for i in range(10):
    if(max < sum[i]):
        max = sum[i]
        index = i 

print("L'indice de la ligne de la matrice dont la somme des éléments est la plus grade est:", index)

#D et E

ligne = int(input("Saisie la ligne pour trouver leur element min(10 lignes): "))
min = matrix[ligne][0]
index = 0

for i in range(4):
    if(min > matrix[ligne - 1][i]):
        min = matrix[ligne - 1][i]
        index = i
print("Le min de la ligne", ligne, "est:", min)

sum = 0

for i in range(10):
    sum = sum + matrix[i][index]

print("La somme des élements de colonne ou se trouve le min est:", sum)
