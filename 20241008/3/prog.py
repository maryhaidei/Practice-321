l=[];w=0;o=0
while s:=input(): 
    l+=[s]
    w+=s.count('~')
    o+=s.count('.')
r=[ '#'*len(l) for i in range(len(l[0])) ]
w1=w; k=len(r)-1
for i in range(1,k):
    if w>0:
        r[k-i]="#"+"~"*(len(r[0])-2)+"#"
        w-=len(l)-2
    else:
        
        r[k-i]="#"+"."*(len(r[0])-2)+"#"
print(*r, sep='\n')

s1="."*o+" "*(abs(w1-o)+len(str(w1)) if w1>o else 1)+str(o)+"/"+str(o+w1)
s2="~"*w1+" "*(abs(w1-o)+len(str(o)) if w1<o else 1)+str(w1)+"/"+str(o+w1)

print(s1)
print(s2)
    
