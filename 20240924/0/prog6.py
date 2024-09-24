import sys
a=[]

while l:=input():
    a.append(eval(l))


for i in range( len(a)-1):
    for j in range(i+1, len(a)):
        a[i][j], a[j][i]=a[j][i], a[i][j]
for linr in a:
    print(line)
