def f(a, b): 
    if isinstance(a, int| float| complex) and isinstance(b, int| float| complex): return a-b
    elif type(a)==type(b) and (isinstance(a[0], type(b[0])) or isinstance(a[0], int| float| complex) and isinstance(b[0], int| float| complex) ):
        a=list(a)
        for el in b: 
            while a.count(el): a.remove(el)
        if type(a)!=type(b): return tuple(a)
        else: return a 
     
print(f(*eval(input())))