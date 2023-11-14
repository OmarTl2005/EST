sucre = int(input("Entrer 1 pour vrai et 0 pour faut pour indiquant si un plat est.\n1- Sucré ou pas: "))
sales  = int(input("2- Salé ou pas: "))
chaud = int(input("3- Chaud ou pas: "))
cher = int(input("4- Cher ou pas: "))

if (sucre == 1 and sales == 0 and chaud == 0 and cher == 0):
    print("Love")
elif (sales == 1 and sucre == 0 and chaud == 1):
    print("Haha")
elif (sales == 0 and sucre == 0 and chaud == 0):
    print("Wow")
elif (sucre == 1 and sales == 1 and chaud == 0):
    print("Sad")
else:
    print("Angry")