i = 0
N = int(input("Entrer le nombre total des réels à entrer: "))
sum = 0
mul = 1
average = 0
num = 0

while (True):
    num = float(input("Saisie un nombre: "))
    sum = sum + num
    mul = mul * num
    average = sum / N
    i = i + 1

    if(i >= N):
        break

print("La somme des nombres est:", sum)
print("Le produit des nombres est:", mul)
print("La moyenne est:", average)