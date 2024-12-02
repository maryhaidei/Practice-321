import sys

s=sys.stdin.read() 
sys.stdout.write(s.encode('latin1',  errors="replace").decode('cp1251',  errors="replace"))
