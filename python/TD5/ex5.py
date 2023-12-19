# q1

def is_oO(char):
    if(char in "oO"):
        return "Vrai"
    else:
        return "Faux"

# q2

def table_de(n):
    print(f"Table de {n}")
    for i in range(1, 10):
        print(i * n)

