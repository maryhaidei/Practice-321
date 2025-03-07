import cowsay
import shlex

class Gamer:
    def __init__(self): 
        self.cord=(0,0)
    def move(self, x, y): 
        a, b =self.cord
        if y in ['left', 'right']: self.cord=(a+x if a+x>=0 and a+x<=9 else 0 if a+x>9 else 9, b)
        else: self.cord=(a, b+x if b+x>=0 and b+x<=9 else 0 if b+x>9 else 9)
        print("Moved to", self.cord)
    
class Monster: 
    def __init__(self, a, b, hello, name, hitpoints): 
        self.cord=(a,b)
        self.hello=hello 
        self.name=name 
        if hitpoints>0: self.hitpoints=hitpoints
        else: raise ValueError
        print("Added monster", self.name, "to", self.cord, "saying", self.hello)
    def say(self): 
        print(cowsay.cowsay(self.hello, cow=self.name))
        
class MUD: 
    def __init__(self): 
        self.monsters=[[0 for _ in range(10)] for _ in range(10)]
    
    def encounter(self, x, y): 
        self.monsters[x][y].say()
    def play(self): 
        pl=Gamer(); direct=['right', 'left', 'up', 'down']; replaced=False
        while s:=input():
            s=shlex.split(s); 
            if [True for i in direct if i==s[0]]: 
                if len(s)>1: 
                    print("Invalid arguments");continue 
                pl.move(1 if s[0] in ['right', 'down'] else -1, s[0])
                x, y = pl.cord
                if self.monsters[x][y]!=0: 
                    self.monsters[x][y].say()
            elif 'addmon'==s[0]: 
                if len(s)!=9: 
                    print("Invalid arguments");continue 
                    if s[1] not in cowsay.list_cows():
                        print("Cannot add unknown monster");continue 
                    p=['hello','hp','coords']
                    if not any([True]+[False for i in p if i not in s]): 
                        print("Invalid arguments");continue     
                try: 
                    coord=s.index('coords')
                    phrase=s[s.index('hello')+1]
                    hitpoints=s[s.index('hp')+1]
                    a, b = int(s[coord+1]), int(s[coord]+2)
                    replaced= True if self.monsters[int(s[2])][int(s[3])] !=0 else False
                    self.monsters[int(s[2])][int(s[3])]=Monster(a, b, phrase, s[1], int(hitpoints))
                except : 
                    print("Invalid arguments");continue
                if replaced: 
                    print("Replaced the old monster")
                    replaced=False 
            else: 
                print("Invalid command")
MUD().play()
                
                
        
