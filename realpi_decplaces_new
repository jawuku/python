# using mpmath library
from mpmath import mp, mpf, sqrt

# realpi = 4/sqrt((1+sqrt(5))/2)

# convert to integer if floating point entered
# catch error if non-numerical value entered
# and set default value to 50 decimal places

try:
    dec_places = int(float(input ("How many decimal places for pi? ")))
    assert dec_places > 0
except ValueError:
    print("\nNot a numerical value. Setting to 50 decimal places.")
    dec_places = 50
except AssertionError:
    print("\nPlease enter a positive value. Setting to 50 decimal places.")
    dec_places = 50
finally:
    # set decimal places for mpmath library
    mp.dps = dec_places

# doing calculation
phi = (sqrt(5) + mpf(1)) / mpf(2)

realpi = mpf(4) / sqrt(phi)

print(f"Real value of pi to {dec_places} decimal places =\n{realpi}")
