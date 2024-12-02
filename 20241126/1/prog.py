s=input(); n=ord(s[0]); l=len(s)-1; ss=s[1:]
le=[ss[i*int(l/n): (i+1)*int(l/n)] if i!= n-1 else ss[i*int(l/n):] for i in range(n)] if n < l else sorted(ss)
print(s[0],*(sorted(le)), sep='')