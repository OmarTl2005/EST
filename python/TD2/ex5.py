a = int(input("Entrer une valeur pour a: "))
b = int(input("Entrer une valeur pour b: "))
c = int(input("Entrer une valeur pour c: "))

if (a > b):
    a, b = b, a
if (b > c):
    b, c = c, b
if (a > b):
    a, b = b, a

print(a, b, c)