import sys

s=sys.stdin.read() 
print(s.encode('latin1',  errors="replace").decode('cp1251',  errors="replace"))
