import decimal 
def esum(n,one):
    s=0
    for m in range(1, n+1): s+= type(one)(str(1/m))
    return s

print(esum(10, 3))