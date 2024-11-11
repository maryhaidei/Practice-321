from itertools import *
class Triangle:
    def __init__(self,*a): self.a,self.b,self.c=sorted(map(list,a))
    def __abs__(self): 
        a=((self.a[0]-self.b[0])**2+(self.a[1]-self.b[1])**2)**0.5
        b=((self.b[0]-self.c[0])**2+(self.b[1]-self.c[1])**2)**0.5
        c=((self.a[0]-self.c[0])**2+(self.a[1]-self.c[1])**2)**0.5
        p=(a+b+c)/2
        return int(r) if int(r:=(p*(p-a)*(p-b)*(p-c))**0.5)==r else r
    def __bool__(self): return bool(abs(self))
    def __lt__(self,other): return abs(self)<abs(other)
    def __contains__(other,self): return abs(self)==0 or all(other.consists(c) for c in [self.a,self.b,self.c])
    def consists(self,other): 
        y=(self.a,self.b,self.c)
        x=[(y[t][0]-other[0])*(y[(t+1)%3][1]-y[t][1])-(y[(t+1)%3][0]-y[t][0])*(y[t][1]-other[1]) for t in range(3)]
        return all(t>=0 for t in x) or all(t<=0 for  t in x)
    def __and__(self,other): 
        if abs(self)==0 or abs(other)==0: return False
        xs=self.a[0];xf=self.c[0];ys=min([self.a[1],self.b[1],self.c[1]]);yf=max([self.a[1],self.b[1],self.c[1]])
        while ys<=yf:
            while xs<=xf:
                if self.consists([xs,ys]) and other.consists([xs,ys]): return True
                xs+=0.1
            xs=self.a[0];ys+=0.1
        return False
import sys
exec(sys.stdin.read())