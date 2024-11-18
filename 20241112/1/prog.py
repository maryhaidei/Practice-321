from collections import*

class DivStr(UserString): 
    def __init__(self, s=''): 
        self.data=s
    def __floordiv__(self, n): 
        i=0; k=len(self.data)//n
        while i<len(self.data): 
            yield DivStr(self.data[i:i+k])
            i+=k
    def __mod__(self, n): 
        if (i:=len(self.data)%n)>0: 
            return DivStr(self.data[-i:])
        else: return DivStr()
import sys
exec(sys.stdin.read())
