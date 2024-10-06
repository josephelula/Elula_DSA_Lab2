
def power(base, exponent):
    # Base: any number that raised to to the power of 0 is 1
    if exponent == 0:
        return 1
    # base * (base raised to the power of exponent - 1)
    else:
        return base * power(base, exponent - 1)
    
# Example of usage
base = 2
exponent = 7
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is {result}")