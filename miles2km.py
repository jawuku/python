'''
Allow user to enter miles and convert to km

convert from string

km = miles * 1.69034

print  equivalent miles in km on screen
'''

miles = input('Enter miles : ')

miles = float(miles)

km = miles * 1.69034

print (f'{miles} miles equals {km} kilometres.')

'''
// C equivalent

# include <stdio.h>

int main (void) {

	float miles, km;

	printf ("Enter miles : ");

	scanf ("%f", &miles);

	km = miles * 1.69034;

	printf ("%f miles equals %f kilometers.\n", miles, km);

	return 0;
}

'''

