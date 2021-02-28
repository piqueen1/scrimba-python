print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

def calculate(num1,operator,num2):
  if operator == '+':
    result = num1 + num2
  elif operator == '-':
    result = num1 - num2
  elif operator == '*':
    result = num1 * num2
  elif operator == '/':
    result = num1 / num2
  else: 
    result = "Please enter one of the following operators: + - * /"
  return result

num1 = input('Enter the first number')
operator = input('Please enter one of the following operators: + - * /')
num2 = input('Enter the second number')
print(calculate(int(num1),operator,int(num2)))