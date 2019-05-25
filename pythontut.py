# Ask the user to input 2 values and store them in variables num1 and num2

num1, num2 = input ('Enter 2 numbers: ').split ();

# Convert input strings into integers

num1 = int (num1);
num2 = int (num2);

#add the values and store value in sum

sum = num1 + num2;

#subtract the values and store value in difference

difference = num1 - num2;

# multiply the values and store value in product

product = num1 * num2;

# divide the values and store value in quotient

quotient = num1 / num2;

# Use modulus to find remainder

remainder = num1 % num2;

# print these results on the screen

print ("{} + {} = {}".format (num1, num2, sum));
print ("{} - {} = {}".format (num1, num2, difference));
print ("{} * {} = {}".format (num1, num2, product));
print ("{} / {} = {}".format (num1, num2, quotient));
print ("{} % {} = remainder {}".format (num1, num2, remainder));

