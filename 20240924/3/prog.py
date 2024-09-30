l=list()
while s:=input(): 
    l.append(list(map(int, s.split(','))))
k=len(l)//2
for i in range(k): 
    for j in range(k): 
        a=str(l[i][0]*l[k][j]+l[i][1]*l[k+1][j]+l[i][2]*l[k+2][j])
        print(a+',' if j!=k-1 else a, end='')
    print()