def objcount(cls): 
    class wrap(cls): 
        counter=0
        def __init__(self, *a, **k): 
            super().__init__(*a, **k)
            type(self).counter+=1
        def __del__(self): 
            if hasattr(cls, '__del__'):super().__del__()
            type(self).counter-=1
    return wrap
import sys
exec(sys.stdin.read())