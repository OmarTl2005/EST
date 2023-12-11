temps = [float(input("Saisie la température du jour {}: ".format(i + 1))) for i in range(28)]
chaud, froid = 0, 0

for temp in temps:
    if (temp >= 10):
        chaud = chaud + 1
    if (temp < 10):
        froid = froid + 1

print("Le nombre des jours chaux est:", chaud, "et le nombre des jours froids est:", froid)