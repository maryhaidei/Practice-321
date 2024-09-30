n, m=eval(input())
print([ x for x in range(n ,m) if all([x%y for y in range(1, int(x**0.5)+1) if y!=x and y!=1]) and x!=1] )