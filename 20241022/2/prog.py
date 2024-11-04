from itertools import* 
def slide(s, n):
    a = iter(s)
    while 1:
        a, b = tee(a)
        b = list(islice(b, n))
        if not b: return
        yield from b
        next(a, None) 
import sys
exec(sys.stdin.read())
