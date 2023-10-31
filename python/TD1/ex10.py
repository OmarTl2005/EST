prix = float(input("Saisie le prix: "))
nombre_article = float(input("Saisie le nombre des articles: "))
tva = float(input("Saisie la valuer de TVA (en %): "))

print("Le prix total TTC: "+ str((prix * nombre_article * tva) / 100))