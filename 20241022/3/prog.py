from itertools import *
print(*[''.join(el) for el in sorted(filter(lambda x: ''.join(x).count("TOR") == 2, product("TOR", repeat=eval(input()))))])