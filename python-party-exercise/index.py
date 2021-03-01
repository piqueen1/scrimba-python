names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
names.extend(names1)

new_name_1 = input('Please add another friend to invite')
names.append(new_name_1)
new_name_2 = input('Please add another friend to invite')
names.append(new_name_2)

for name in names:
  print(f'Hello {name.title()}! You are invited to the party Saturday!')