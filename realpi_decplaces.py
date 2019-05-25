import gmpy2
from gmpy2 import mpfr

# realpi = 4/sqrt((1+sqrt(5))/2)

dec_places = input ('Displaying the real value of Pi. How many decimal places? ')
# convert to integer if floating point entered
#catch error if non-numerical value entered
#and set default value to 20 decimal places
try:
    dec_places = int (float (dec_places))

except ValueError:
    dec_places = 20

# check that number input is a positive integer
#and set default value to 20 decimal places

if dec_places <=1:

    print ('\nEnter an integer value greater than 0. Setting to 20 decimal places.')
    dec_places = 20

else:
    print ('\nSetting to {} decimal places'.format (dec_places))

# Perform calculation at 32768-bit precision
# calc variable stores intermediate values in calculation
gmpy2.get_context().precision = 32768

calc = gmpy2.sqrt (5)
calc = gmpy2.add (1, calc)

phi = gmpy2.div (calc, 2)

rootphi = gmpy2.sqrt (phi)

realpi = gmpy2.div (4, rootphi)

print ('Real value of pi = {:.{prec}Df}'.format (realpi, prec=dec_places))



