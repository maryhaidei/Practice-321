from math import *
def Calc(s, t, u) : 
    def f (n): 
        x=n; r1=eval(s)
        y=eval(t); x=r1
        return eval(u)
    return f

F = Calc(*eval(input()))
print(F(eval(input())))