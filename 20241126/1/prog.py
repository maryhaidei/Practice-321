import sys
s=sys.stdin.read(); n=ord(s[0]); l=len(s)-1; ss=s[1:]
le=[ss[i*int(l/n): (i+1)*int(l/n)] if i!= n-1 else ss[i*int(l/n):] for i in range(n)] if n < l else sorted(ss);
st=s[0]+''.join(sorted(le))
for i in st:sys.stdout.buffer.write(bytes(ord(i)))