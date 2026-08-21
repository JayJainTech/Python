# Lists
bicycles = ['trek', 'cannon-dale', 'redline', 'specialized']
print(bicycles)

# Accessing Elements in a List
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[2])
print(bicycles[-1]) # Last element(goes backwards)

# Names
names = ['pallavi failure', 'elvis Presley', 'steven he', 'yippee bunny']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())

# Greetings
print(f"Hello {names[0].title()}, how are you doing today?")
print(f"Hello {names[1].title()}, how are you doing today?")
print(f"Hello {names[2].title()}, how are you doing today?")
print(f"Hello {names[3].title()}, how are you doing today?")

# Your Own List
car_brands = ['Tesla', 'BMW', 'Audi', 'Chevy', 'Corvette', 'Lamborghini']
print(f'I would like to own a {car_brands[0]} car.')
print(f'I would like to eat a {car_brands[4]} car.')
print(f'I would like to burn a {car_brands[3]} car.')
print(f'I would like to gift a {car_brands[2]} car.')
print(f'I would like to have a {car_brands[1]} car.')

# Modifying, Adding, and Removing Elements
car_brands[0] = 'Mercedes' # Changed first element to 'Mercedes'
print(f'\nActually, I would like to own a {car_brands[0]} car.')
car_brands.append('Rivian') # Added 'Rivian' element to end of list
print(f'A {car_brands[-1]} would also be nice.')
car_brands.insert(2, 'Semi truck') # Added 'Semi truck' element to 2nd position and moved the rest right to make space
print(f'A {car_brands[2].lower()} is useful for carrying multiple cars at once.')
print(car_brands)
del car_brands[4] # Deleted 'Chevy' element from list
print(car_brands)
popped_car_brand = car_brands.pop(3) # Deleted 'Audi' element from list and assumed value of 'Audi' element
print(popped_car_brand)
print(car_brands)
car_brands.remove('BMW') # Removed first occurrence of element 'BMW' from list
print(car_brands)

# Guest List
dinner_invitees = ['steven HE', "ChaRLie BrOwN", "TIMMY FALIUrE"]
print(f'Dear {dinner_invitees[0].title()},\n\t You are invited to dinner at my place at 3 PM today.\n\t See you there!\nBest,\n\tJay\n')
print(f'Dear {dinner_invitees[2].title()},\n\t You are invited to dinner at my place at 3 PM today.\n\t See you there!\nBest,\n\tJay\n')
print(f'Dear {dinner_invitees[1].title()},\n\t You are invited to dinner at my place at 3 PM today.\n\t See you there!\nBest,\n\tJay')

# Changing Guest List
print(f'\nWHY THE HELL YOU CANNOT ATTEND LEH? OKAY {dinner_invitees[2].upper()} SEE YOU LATER LEH\n')
dinner_invitees.remove('TIMMY FALIUrE')
print(f'Dear {dinner_invitees[0].title()},\n\t You are invited to dinner at my place at 3 PM today.\n\t See you there!\nBest,\n\tJay\n')
print(f'Dear {dinner_invitees[1].title()},\n\t You are invited to dinner at my place at 3 PM today.\n\t See you there!\nBest,\n\tJay\n')
dinner_invitees.append('Papa BAby')
print(f'Dear {dinner_invitees[0].title()},\n\t You are invited to dinner at my place at 3 PM today.\n\t See you there!\nBest,\n\tJay\n')
print(f'Dear {dinner_invitees[2].title()},\n\t You are invited to dinner at my place at 3 PM today.\n\t See you there!\nBest,\n\tJay\n')
print(f'Dear {dinner_invitees[1].title()},\n\t You are invited to dinner at my place at 3 PM today.\n\t See you there!\nBest,\n\tJay')
