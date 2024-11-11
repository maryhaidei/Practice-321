class Maze:
    def __init__(self,n):
        self.a=[["█" if i%2==0 or j%2==0 else "·" for i in range(2*n+1)] for j in range(2*n+1)]
    def __str__(self): return '\n'.join(map(''.join,self.a))
    def f(self,p,q,pr):
        if p==q: return True
        x,y=p
        t=[c for c in [(x+1,y),(x,y+1),(x,y-1),(x-1,y)] if self.a[c[0]][c[1]]=="·" and c not in pr]
        pr.add(p)
        return t and any(self.f(c,q,pr) for c in t)   
    def __getitem__(self,x):
        p=(x[1].start,x[0]);q=(x[2],x[1].stop)
        return self.f(tuple(map(lambda x: x*2+1,p)),tuple(map(lambda x: x*2+1,q)),{tuple(map(lambda x: x*2+1,p))})    
    def __setitem__(self,x,v):
        p=max([(x[1].start,x[0]),(x[2],x[1].stop)]);q=max([(x[1].start,x[0]),(x[2],x[1].stop)])
        if p[0]==q[0] or p[1]==q[1]:
            for i in range(p[p[1]==q[1]]*2+1,q[p[1]==q[1]]*2+2): self.a[p[p[0]==q[0]]*2+1][i]="·"
import sys
print(sys.stdin.read())