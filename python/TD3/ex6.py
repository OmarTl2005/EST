while(True):
    num = float(input("Saisie un nombre compris entre 10 et 20: "))
    if (num >= 10 and num <= 20):
        print(num,"est compris entre 10 et 20.")
        break
    elif(num > 20):
        print("Plus grand!")
    else:
        print("Plus petit!")