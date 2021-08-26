import gmpy2
from gmpy2 import mpfr

# realpi = 4/sqrt((1+sqrt(5))/2)

prec = input ('Enter bits of precision : ')
# catch error if floating point entered
# convert to integer if floating point entered
try:
    prec = int(float(prec))

except ValueError:
    prec = 0

# check that number input is a positive integer
# otherwise set default precision to 256 bits

if prec <=1:

    print('\nEnter an integer value greater than 1. Setting to 256-bit precision')
    gmpy2.get_context().precision = 256

else:
    print('\nSetting to {}-bit precision'.format(prec))
    gmpy2.get_context().precision = prec

# Perform calculation
# calc variable stores intermediate values in calculation
calc = mpfr('5')
calc = gmpy2.sqrt(calc)
calc = gmpy2.add(1, calc)

phi = gmpy2.div(calc, 2)

rootphi = gmpy2.sqrt(phi)

realpi = gmpy2.div(4, rootphi)

print('Real value of pi = ')
print(realpi)
