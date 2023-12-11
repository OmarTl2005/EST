T = [int(input("Saisie la valeur {}: ".format(i + 1))) for i in range(10)]

for i in range(10):
    print(T[i], end=" ")
    T[i] = 1
