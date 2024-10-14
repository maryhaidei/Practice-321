from fractions import *
def func(s, w, a, *args): 
    r=0; r1=0
    for i in range(a+1): 
        r+=args[i]*(s**(a-i))
    for j in range(args[a+1]+1): 
        r1+=args[a+2+j]*(s**(args[a+1]))
    return Fraction(r/r1) == Fraction(w)

print(func(*eval(input())))