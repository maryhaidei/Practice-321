s=input().lower(); c=set()
for i in range(len(s)-1): 
    if s[i].isalpha() and s[i+1].isalpha(): c.add(s[i]+s[i+1])
print(len(c))