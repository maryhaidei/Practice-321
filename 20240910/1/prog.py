a=eval(input())
a.sort()
n=len(a)
for i in range(n): print(a[i],end=(', ' if i<n-1 else '\n'))
