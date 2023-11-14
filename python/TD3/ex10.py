max_number = 0
i = 0
index = 0

while(True):
    number = float(input("Saisie un nombre: "))
    if (number > max_number):
        max_number = number
        index = i + 1

    i += 1
    if(number == 0):
        break
print("Le nombre maximal est:", max_number)
print("Sont index est:", index)