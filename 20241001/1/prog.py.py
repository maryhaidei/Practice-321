def Pareto (*a) : 
    l=list(a)
    for b in a: 
        for c in a: 
            if b!=c and b[0]<=c[0] and b[1]<=c[1]: 
                l.remove(b); break
    return tuple(l) 

print(Pareto(*eval(input())))