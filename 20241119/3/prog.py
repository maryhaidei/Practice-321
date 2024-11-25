class Vowel:
    __slots__=tuple(list("aouiey")+["answer_"])
    def __init__(self, **args): 
        for i in "aouiey": 
            if i in args: setattr(self, i, args[i])
        setattr(self, 'answer_', 42)
    def __str__(self): 
        return ', '.join([ str(i)+':'+str(getattr(self, i)) for i in 'aeiouy' if hasattr(self, i)] )
    @property
    def answer(self): return self.answer_
    @answer.setter
    def answer(self, val): raise AttributeError
    @property
    def full(self):
        return all([getattr(self, i) if hasattr(self, i) else None for i in "aouiey" ])    
    @full.setter
    def full(self, val): pass
import sys
exec(sys.stdin.read())