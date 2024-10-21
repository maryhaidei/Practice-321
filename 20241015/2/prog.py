from math import *
l={}; c=0; res=[]; 
while (s:=input())[:4]!="quit":
    s=s.split();c+=1
    if s[0][0]==":": 
        l[s[0][1:]]= [s[-1]]+[ s[i] for i in range(1, len(s)-1)]
        
    else: 
        if len(l[s[0]])==1:
            res.append(eval(l[s[0]][0]))
        else: 
            res.append(eval(l[s[0]][0],None, {l[s[0]][i]:eval(s[i]) for i in range(1, len(s))}))
print(*res, sep='\n')
print((eval(s[5:])).format(len(l)+1, c+1))