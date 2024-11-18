class InvalidInput(Exception): 
    def __init__(self): 
        print("Invalid input")
class BadTriangle(Exception): 
    def __init__(self): 
        print("Not a triangle")
        
def triangleSquare(s): 
    try : 
        (x1, y1), (x2, y2), (x3, y3) = eval(s)
    except: 
        raise InvalidInput
    a=((x1-x2)**2 + (y1-y2)**2)**0.5
    b=((x3-x2)**2 + (y3-y2)**2)**0.5
    c=((x1-x3)**2 + (y1-y3)**2)**0.5
    if a+b<=c or a+c<=b or c+b<=a: raise BadTriangle
    else: 
        p=(a+b+c)/2
        return ((p-a)*(p-b)*(p-c)*p)**0.5
    
while s:=input(): 
    try: 
        print(f"{triangleSquare(s):.2f}")
    except InvalidInput: pass
    except BadTriangle: pass