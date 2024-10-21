n=int(input()); l=''
while s:=input():
    l+=s.lower()+' '
for i in l: 
    if not i.isalpha(): l=l.replace(i, " ")
s={i: l.count(i) for  i in set(l.split()) if len(i)==n}

m=max(s.values()) if s else 0
print(*sorted([i for i in s if s[i]==m]))