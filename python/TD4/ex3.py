from random import randint

T = [ randint(0, 1000) for i in range(100)]
print(T)

max = 0
min = 0

for value in T:
    if(value > max):
        max = value
    if(value < min):
        min = value

print("Le max est:", max, "et le min est: ", min)