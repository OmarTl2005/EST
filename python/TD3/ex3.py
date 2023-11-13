total_price = 0
price = 1

while price != 0:
    price = int(input("Entrez le prix de l'article en DH (saisir 0 pour terminer) : "))
    total_price += price

print("La somme totale des prix est de", total_price ,"DH.")
