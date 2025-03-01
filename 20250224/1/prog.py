import cowsay

class Gamer:
    def __init__(self): 
        self.cord=(0,0)
    def move(self, x, y): 
        a, b =self.cord
        if y in ['left', 'right']: self.cord=(a+x if a>0 and a<9 else 0 if a+x>9 else 9, b)
        if y in ['up', 'down']: self.cord=(a, b+x if b>0 and b<9 else 0 if b+x>9 else 9)
        print("Moved to", self.cord)
    
class Monster: 
    def __init__(self, a, b, hello): 
        self.cord=(a,b)
        self.hello=hello 
        print("Added monster to", self.cord, "saying", self.hello)
    def say(self): 
        print(cowsay.cowsay(self.hello))
        
class MUD: 
    def __init__(self): 
        self.monsters=[[0 for _ in range(10)] for _ in range(10)]
    
    def encounter(self, x, y): 
        self.monsters[x][y].say()
    def play(self): 
        pl=Gamer(); direct=['right', 'left', 'up', 'down']
        while s:=input():
            s=s.strip().split()
            if any([True for i in direct if i in s]): 
                if len(s)>1: 
                    print("Invalid arguments");continue 
                pl
                
                
                
        
