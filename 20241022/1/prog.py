def fib(m, n):
    a, b= 1, 1 
    if n==1: yield 1
    for i in range(m+n-1):
        if i>=m-1: yield b
        a, b= b, a+b
        
import sys
exec(sys.stdin.read())