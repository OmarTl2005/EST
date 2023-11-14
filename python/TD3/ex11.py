x = float(input("Saisie une valeur pour x: "))
n = float(input("Saisie une valeur pour n: "))
result = 0
i = 0
fact = 1

# 1er
while(i <= n):
    fact *= i
    if(i == 0):
        fact = 1
    print(fact)
    result += (x ** i) / fact
    print(result)
    i += 1
print("Le resultat de la 1er expression est:", result)

# 2éme
i = 1
while(i <= n):
    result += x ** i
    i += 1
print("Le resultat de la 2éme expression est:", result)