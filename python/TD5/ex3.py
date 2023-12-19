# q1
def sum_of_2(a, b):
    return a + b

# q1-2

def factorial(n):
    if(n == 0 or n == 1):
        return 1
    
    fact = 1
    for i in range(n, 1, -1):
        fact *= i
    return fact

# q2
def divisible(a, b):
    if(b % a == 0):
        return 1
    else:
        return 0

# q3

def division(a, b):
    quotion = int(a / b)
    reste = a % b
    print(f"{a} / {b} = {quotion} et le reste est: {reste}")

# q4

def voyelle(char):
    voyelles = "aeiouy"
    if char in voyelles:
        return 1
    else:
        return 0

# q5

def echange(a, b):
    return b, a

# q6

def absolue(a):
    if a < 0:
        return -a
    return a

print(absolue(-5))