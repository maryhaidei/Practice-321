import sys 
a=[] 

while l:=input(): 
    a.append(eval(l))

if not all([len(e)==len(a) for e in a)]:
    print("Wat")
    sys.exit(100500)

for i in range( len(a)-1): 
    for j in range(i+1, len(a)):
        a[i][j], a[j][i]=a[j][i], a[i][j]
for linr in a: 
    print(line)