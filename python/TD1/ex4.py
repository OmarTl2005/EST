note1 = float(input("Entrer la 1er note: "))
note2 = float(input("Entrer la 2éme note: "))
note3 = float(input("Entrer la 3éme note: "))
co1 = float(input("Entrer le 1er coefficient: "))
co2 = float(input("Entrer le 2éeme coefficient: "))
co3 = float(input("Entrer le 3éme coefficient: "))
total = (note1 * co1 + note2 * co2 + note3 * co3) / (co1 + co2 + co3)
print(total)