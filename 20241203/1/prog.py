
import sys
class dump(type):
    def __new__(cls, name, bases, dct):
        new_dct = {}
        for attr, value in dct.items():
            if callable(value): 
                new_dct[attr] = cls.create_wrapped_method(value)
            else:
                new_dct[attr] = value
        return super().__new__(cls, name, bases, new_dct)

    @staticmethod
    def create_wrapped_method(method):
        def wrapped(self, *args, **kwargs):
            invalid_args = [arg for arg in args if not isinstance(arg, (str, int, float, bool))]
            invalid_kwargs = [value for value in kwargs.values() if not isinstance(value, (str, int, float, bool))]
            print(f"{method.__name__}: {args}, {kwargs}")
            return method(self, *args, **kwargs)
        return wrapped

    
exec(sys.stdin.read())