from math import *
def show(screen): 
    print("\n".join(["".join(s) for s in screen][::-1]))
def scale(a, b, A, B, x): 
    return ((x-a)*(B-A))/(b-a) + A

def count(x, v): return eval(v) 
 
def gra(w, h, a,b, v):
    w,h,a,b=eval(w), eval(h), eval(a), eval(b)
    screen=[[" "]* w for i in range(h)]
    ma=count(a,v); mi=count(a, v);j=a+0.01
    while j<=b:
        mi=min(mi, count(j, v)); ma=max(ma, count(j, v)); j+=0.01
    for i in range(w): 
        x=scale(0, w-1, a, b, i)
        y=eval(v)
        s=scale(mi, ma, 0, h-1, y)
        screen[round(s)][i]="*"
        if i and (abs(round(s)-prev)>1) : 
            if prev<=round(s):
                for j in range(prev+1,round(s)): screen[j][i-1]='*'
            else:
                for j in range(round(s)+1,prev): screen[j][i-1]='*'
        prev=round(s)

    return screen 

        
show(gra(*input().split(' ')))