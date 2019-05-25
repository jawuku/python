weight = float(input('Enter your weight in kg : '))

height = float(input('\nand enter your height in metres : '))

height = float(height)

bmi = weight / (height**2)

print(f'\nYour BMI is {bmi}\n')

if bmi < 19.5:
    print('You are underweight')
elif (bmi >= 19.5 and bmi <=25):
    print('You are the ideal weight')
elif (bmi >25 and bmi < 30):
    print('You are overweight')
elif (bmi >=30 and bmi < 40):
    print('You are obese')
else:
    print('Morbid obesity')