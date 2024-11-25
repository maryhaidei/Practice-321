class Num:
    def __init__(self):
        self.value_= {}
    
    def __get__(self, instance, owner):
        if instance is None:return self
        return self.value_.get(instance, 0)  
    
    def __set__(self, instance, value):
        if hasattr(value, 'real'): self.value_[instance] = value.real
        else: self.value_[instance] = len(value)
        
    def __delete__(self, instance):
        if instance in self._values:del self.value_[instance] 
              
import sys
exec(sys.stdin.read())