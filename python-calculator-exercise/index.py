print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f
num1 = input('Enter the first number')
operator = input('Please enter one of the following operators: + - * / or enter f for Celsius to Fahrenheit conversion')
if operator.lower() == 'f':
  print(f'{num1} Celsius is equivalent to {(num1*9/5) + 32} Fahrenheit')
else:
  num2 = input('Enter the second number')

  if operator == '+':
    print(f'Anser is {num1 + num2}')
  elif operator == '-':
    print(f'Anser is {num1 - num2}')
  elif operator == '*':
    print(f'Anser is {num1 * num2}')
  elif operator == '/':
    print(f'Anser is {num1 / num2}')
  else:
    print('Input error!')
