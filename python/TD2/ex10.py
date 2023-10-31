print("Entrer des valeurs pour résoudre l'equation ax² + bx + c = 0!")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b**2 - (4 * a * c)
x1 = ((-b - (delta ** (1/2))) / 2*a)
x2 = ((-b + (delta ** (1/2))) / 2*a)

print("Les solution de l'equation ax² + bx + c sont: ",x1, "ou", x2)