def lire_liste():
    nombres = []
    nombre_pairs = 0

    while True:
        nombre = int(input("Entrez un nombre entier (-1 pour terminer) : "))
        
        if nombre == -1:
            break
        
        nombres.append(nombre)
        if nombre % 2 == 0:
            nombre_pairs += 1
    
    total_nombres = len(nombres)
    if(total_nombres > 0):
        pourcentage = (nombre_pairs / total_nombres) * 100
    else:
        pourcentage = 0
    
    print(f"Il y a {nombre_pairs} entiers pairs.")
    print(f"Le pourcentage d'entiers pairs par rapport au total est de : {int(pourcentage)}%")

lire_liste()
