def show(screen): 
    print("\n".join(["".join(s) for s in screen]))
def scale(a, b, A, B, x): 
    return ((x-a)*(B-A))/(b-a) + A
 
def gra(a,b, w, h): 
    screen=[[" "]* w for i in range(h)]
    for i in range(w): 
        x=scale(0, w-1, a, b, i)
        y=sin(x)
        s=scale(-1, 1, 0, h-1, y)
        screen=[roun(s)][i]="*"
    return screen 
