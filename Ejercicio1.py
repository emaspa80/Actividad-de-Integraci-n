# 1.Escribir una función que calcule el máximo común divisor entre dos números.

def mcd(x,y):
    mcd=1
    if x %y == 0:
        return y
    
    for k in range(int(y/2), 0, -1):
        if x %k == 0 and y % k == 0:
            mcd = k
            break
    return mcd

print(mcd(16, 8))   
print(mcd(26, 2))  