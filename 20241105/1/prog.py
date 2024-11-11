class Omnibus:
    dic = {}
    def __setattr__(self, name, value):
        if name in Omnibus.dic: Omnibus.dic[name].add(self)
        else: Omnibus.dic[name]={self}
    def __getattr__(self, name):
        if name in Omnibus.dic: return len(Omnibus.dic[name])
        return 0
    def __delattr__(self, name):
        if name in Omnibus.dic: Omnibus.dic[name].discard(self)
import sys
exec(sys.stdin.read())