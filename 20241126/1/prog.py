import sys
s=sys.stdin.buffer.read(); n=s[0]; l=len(s)-1; ss=s[1:-1]
le=sorted([ss[i*int(l/n): (i+1)*int(l/n)] if i!= n-1 else ss[i*int(l/n):] for i in range(n)]) if n < l else sorted(ss);
sys.stdout.buffer.write(bytes([s[0]]))
try:
    for t in le: sys.stdout.buffer.write(t)
except Exception:
    sys.stdout.buffer.write(bytes(list(le)))