operation = int(input("1- addition\n2- soustraction\n3- produit\nChoisir une operation: "))
x = float(input("Entrer le 1er nombre: "))
y = float(input("Enter le 2éme nombre: "))

if(operation == 1):
    print(x + y)
elif (operation == 2):
    print(x - y)
elif (operation == 3):
    print(x * y)
else:
    print("Quelque chose s'est mal passé s'il vous plait essayez à nouveau")