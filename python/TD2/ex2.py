# Avec L'aide d'un variable
a = int(input("Entrer une valeur pour a: "))
b = int(input("Entrer une valeur pour b: "))
c = int(input("Entrer une valeur pour c: "))

max_num = a
if b > max_num:
    max_num = b
if c > max_num:
    max_num = c
print(max_num)
# sans l'aide d'un variable
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)