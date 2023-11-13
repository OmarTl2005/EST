password = "1234"

while(True):
    attempt = input("Entrer le mot de passe: ")
    if (attempt == password):
        print("Mot de passe correct")
        break
    else:
        print("Mot de passe incorrect")