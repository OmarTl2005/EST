X = float(input("Entrer des valeurs pour calculer par multiplications successives X à la puisance N.\nX: "))
N = float(input("N: "))
i = 0
result = 1

while(i < N):
    result *= X
    i += 1
print("X à la puisnce N est égal à:", result)