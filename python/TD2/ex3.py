a = int(input("Entrer une valeur pour a: "))
b = int(input("Entrer une valeur pour b: "))

# produit
if (a > 0 and b > 0 or a < 0 and b < 0):
    print("Le produit de", a, "et",b, "est positif")
else:
    print("Le produit de", a, "et",b, "est negatif")

# somme
if (a > 0 and b > 0 or a > b or b > a):
    print("La somme de", a, "et",b, "est positif")
else:
    print("Le produit de", a, "et", b, "est negatif")