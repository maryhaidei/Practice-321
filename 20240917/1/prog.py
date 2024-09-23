n=int(input())
print('A', '+' if n%25==0 and n%2==0 else '-', 'B', '-' if n%25 or (n%2==0) else '+', 'C', '-' if n%8 else '+')  
