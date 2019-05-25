'''
Simple calculator
-----------------

Enter number, followed by arithmetic operator ( + - * / %)
then second number

e.g. 4 * 5

print result on screen i.e.

4 * 5 = 20

'''

num1, operator, num2 = input('Enter operation (e.g. 3 + 2) : ').split()

num1 = int(num1)
num2 = int(num2)

if operator == "+":
    print('{} + {} = {}'.format(num1, num2, num1+num2))

elif operator == "-":
    print('{} - {} = {}'.format(num1, num2, num1-num2))

elif (operator == "*") or (operator == "x"):
    print('{} * {} = {}'.format(num1, num2, num1*num2))

elif operator == "/":
    print('{} / {} = {}'.format(num1, num2, num1/num2))


elif operator == "%":
    print('{} % {} = remainder {}'.format(num1, num2, num1 % num2))

elif (operator == "^") or (operator == "**"):

    print('{} ^ {} = {}'.format(num1, num2, num1**num2))

else:
    print('Invalid operation - Format: num1 [ + - * / % ^ ] num2')
