import math

def termeDeLaSuite():
    n = 1
    u = 0.5 * math.exp(1) - 0.5
    while n < 21:
        u = 0.5 * math.exp(1) - (n+1) * 0.5 * u
        n = n+2
    return n
    
print(termeDeLaSuite())
