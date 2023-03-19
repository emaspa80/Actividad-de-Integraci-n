# 2.Escribir una función que calcule el mínimo común múltiplo entre dos números

def mcm (x,y):
    z = max(x,y)
    
    while True:
        if (z % x == 0) and (z % y == 0):
            return z
        
        z += 1
        
print(mcm(9, 3))
print(mcm(40, 12))       
print(mcm(30, 3))
