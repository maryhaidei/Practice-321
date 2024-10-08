from math import *
def scale(a, b, A, B, x): 
    return ((x-a)*(B-A))/(b-a) + A

def gra(a,b, w, h): 
    for i in range(h):
        x=scale(0, h-1, a,b,i)
        y=sin(x)
        s=scale(-1,1,0,w-1,y)
        print(" "*round(s), "*")