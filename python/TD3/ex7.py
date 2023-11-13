N = int(input("Saisie des valuers pour l'intervale [N, M].\nN: "))
M = int(input("M: "))
sum = 0

for i in range(N, M + 1):
    if(i % 2 == 1):
        sum += i

print("La somme des nombre impair compris entre", N,"et", M,"est:", sum)