def carré_parfait(x):
    i = 0
    while(x >= i**2):
        if i ** 2 == x:
            print(f"{x} est un carré parfait.")
            return
        i += 1
    print(f"{x} n'est pas un carré parfait")

