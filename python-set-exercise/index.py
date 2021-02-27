#Sets - Exercise


friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

#1. Check if ‘Eric’ and ‘John’ exist in friends
print('Eric' in friends and 'John' in friends)
#2. combine or add the two sets 
combined = friends.union(my_friends)
print(combined)
combinedPipe = friends | my_friends
print(combinedPipe)
#3. Find names that are in both sets
print (friends.intersection(my_friends))
intersection2 = friends & my_friends
#4. find names that are only in friends
print(friends.difference(my_friends))
difference2 = friends - my_friends
print(difference2)
#5. Show only the names who only appear in one of the lists
print(my_friends.symmetric_difference(friends))
symmetric2 = my_friends ^ friends
#6. Create a new cars-list without duplicates
print(set(cars))
#7. Make a list of unique cars
unique_cars_list = list(set(cars))