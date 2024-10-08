import decimal
import fractions
def multiplier( x, y, Type): 
    return Type(x)*Type(y)

print(multiplier("1/6", "2/3", fractions.Fraction))
print(multiplier("1/6", "2/3", decimal.Decimal))
print(multiplier("1/6", "2/3",  float))

