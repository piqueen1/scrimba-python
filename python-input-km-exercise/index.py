# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

name= input('What is your name?')
km= input('How many kilometers do you want to convert?')

print(f'Hi {name}, I am convertine {km} kilometers for you.')
miles= float(km)/1.609

print(f'{km} kilometers is {str(round(miles,1))} miles.')