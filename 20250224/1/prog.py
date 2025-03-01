import cowsay

class Gamer:
    def __init__(self): 
        self.cord=(0,0)
    def move(self, x, y): 
        a, b =self.cord
        if y in ['left', 'right']: self.cord=(a+x if a>0 and a<9 else 0 if a+x>9 else 9, b)
        else: self.cord=(a, b+x if b>0 and b<9 else 0 if b+x>9 else 9)
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
            if [True for i in direct if i==s[0]]: 
                if len(s)>1: 
                    print("Invalid arguments");continue 
                pl.move(1 if s[0] in ['right', 'down'] else -1, s[0])
                x, y = pl.cord
                if self.monsters[x][y]!=0: 
                    self.monsters[x][y].say()
            if 'addmon'==s[0]: 
                if len(s)!=4: 
                    print("Invalid arguments");continue 
                try: 
                    self.monsters[s[1]][s[2]]=Monster(s[1], s[2], s[3])
                    replaced= True if self.monsters[s[1]][s[2]] !=0 else False
                except: 
                    print("Invalid arguments");continue
                if replaced: 
                    print("Replaced the old monster")
                    replaced=False 
            else: 
                print("Invalid command")
                
                
                
        
