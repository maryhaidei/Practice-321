import cowsay

class Gamer:
    def __init__(self): 
        self.cord=(0,0)
    def down(self): 
        a, b =self.cord
        self.cord= (a, b+1 if b<9 else 0)
        print("Moved to", self.cord)
    def up(self): 
        a, b=self.cord
        self.cord = (a, b-1 if b>0 else 9)
        print("Moved to", self.cord)
    def left(self): 
        a, b =self.cord
        self.cord= (a-1 if a>0 else 9, b)
        print("Moved to", self.cord)
    def right(self): 
        a, b=self.cord
        self.cord = (a+1 if a<9 else 0, b)
        print("Moved to", self.cord)
    
class Monster: 
    def __init__(self, a, b, hello): 
        self.cord=(a,b)
        self.hello=hello 
        print("Added monster to", self.cord, "saying", self.hello)
    def say(self): 
        print(cowsay.cowsay(self.hello))
