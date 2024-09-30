l=list(map(int, input().split(',')))
for i in range(len(l)): 
    for j in range(i+1, len(l)): 
        if l[i]**2 %100 > l[j]**2%100: 
            m=l[j]
            l[j]=l[i]
            l[i]=m
print(l)