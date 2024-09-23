def s(st): 
    ss=0
    for c in st: ss+=int(c)
    return ss
k=int(input())
n=k
while n<=k+2:
    m=k
    while m<=k+2: 
        print(n, '*', m, '=', ':=)' if s(str(m*n))==6 else m*n, end=' ')
        m+=1
    n+=1
    print('\n')
    