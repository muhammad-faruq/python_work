# ~ def message():
	# ~ print("Hello World!")
# ~ message()
# ~ message = 'Hello Python Course!!'
# ~ print(message)
# ~ name = 'muhammad faruq'
# ~ print(name.title())
# ~ print(name.upper())
# ~ print(name.lower())

# ~ first_name = 'bobby'
# ~ last_name = 'hedgehog'
# ~ full_name = first_name + " " + last_name
# ~ print('Hello ' + full_name.title() + '!')

# ~ print('\tHello \nis it me\nhow does this work?')
# ~ blob = '      t h e r e \ti s \ta \tl o t \to f \tw h i t e \ts p a c e'
# ~ print(blob)
# ~ print(blob.strip())
### .strip only removes white space at the beginning and end

# ~ print("That jewel is my mother's dog")
# ~ print('That jewel is my mother"s dog')
### Use different quotations with '' and "" to avoid syntax errors.

# ~ age = 23
# ~ print('I will be ' + str(age) + ' years old this year!')
### Remember to add str() for numbers when adding them intro strings!

# ~ age = 3/2
# ~ print(age)
# ~ print(3/2)
# ~ print('3/2')
### well you can do simple arithmatics in the print function

### Here we start to learn about lists!

# ~ bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# ~ print(bicycles)
# ~ trek = 'a'
# ~ cannondale = 'b'
# ~ redline = 'c'
# ~ specialized = 'd'
# ~ bicyclee = [trek, cannondale, redline, specialized]
# ~ print(bicyclee)
### make sure to have '' inside your lists if they are strings!!

# ~ food = ['apple', 'potato', 'banana', 'turnip']
# ~ print(food[0].title())
# ~ print(food[1])
# ~ print(food[0:4])
# ~ print(food[-1])
# ~ print(food[2:])
# ~ print(food[:3])

# ~ food = ['apple', 'potato', 'banana', 'turnip']
# ~ print(food)
# ~ food[0] = 'not apple'
# ~ print(food)
# ~ food.append("pear")
# ~ print(food)
# ~ food.insert(2,'not pear')
# ~ print(food)
### append will add things to the back of the list whereas inserting can
### put them anywhere in the list that you want.


# ~ print("---------------------------")
# ~ popped_food = food.pop()
# ~ print(food)
# ~ print(popped_food)
# ~ print('The first food on this list is ' + food.pop(0))
# ~ print('The first food on this list is ' + food.pop(0))
# ~ print('The first food on this list is ' + food.pop(0))
# ~ print('The first food on this list is ' + food.pop(0))
# ~ print(food)

# ~ this_list = ['food', 'nonsense', 'garbage', 'stuffs', 'filler text']
# ~ print(this_list)
# ~ del this_list[0]
# ~ print(this_list)
# ~ this_list.remove('garbage')
# ~ print(this_list)
### del helps to delete based on position whereas remove will remove 
### based on value

# ~ this_list = ['food', 'nonsense', 'garbage', 'stuffs', 'filler text']
# ~ this_list.sort(reverse=True)
# ~ print(this_list)
# ~ print(sorted(this_list))
### for some funny reason sort and sorted work completely differently
### sort is used at the end -> list.sort()
### sorted is at the start -> sorted(list)
### Why does it happen this way? I dont know :(

# ~ this_list = ['food', 'nonsense', 'garbage', 'stuffs', 'filler text']
# ~ print(this_list)
# ~ this_list.reverse()
# ~ print(this_list)

### finding length of a list
# ~ stuff = [1, 2, 3, 4, 5, 6, 7, 8]
# ~ print(stuff)
# ~ print(len(stuff))

### Lets start learning Loops!!

# ~ people = ['sarah', 'alice', 'jacob', 'gordon', 'rigdon']
# ~ for person in people:
	# ~ print(person.title() + ' did not come to work today!')
# ~ print('\nOh right its a Sunday')

# ~ for value in range(1,9):
	# ~ print(value)
# ~ numbers = list(range(1,10000))
# ~ print(numbers)
# ~ even_numbers = list(range(2,11,2))
# ~ print(even_numbers)
# ~ odd_numbers = list(range(1,111,2))
# ~ print(odd_numbers)
# ~ squares = []
# ~ for elements in range(1,11):
	# ~ square = elements**2
	# ~ squares.append(square)
# ~ print(squares)

# ~ squares = [value**2 for value in range(1,11)]
# ~ print(squares)

# ~ cubes = [value**3 for value in range(1,11)]
# ~ print(cubes)

# ~ for numbers in range(1,21):
	# ~ print(numbers)
	
# ~ big = list(range(1,1000001))
# ~ for elements in big:
	# ~ print(elements)
# ~ print(max(big))
# ~ print(min(big))
# ~ print(sum(big))

# ~ listed = list(range(1,21,2))
# ~ for numbers in listed:
	# ~ print(numbers)

# ~ lsited = list(range(3,31,3))
# ~ for asd in lsited:
	# ~ print(asd)

# ~ cubes = [value**3 for value in range(1,11)]
# ~ for asd in cubes:
	# ~ print(asd)
# ~ print(cubes)

# ~ people = ['martins', 'george', 'bob', 'caleb', 'sam']
# ~ print(people[1:3])
# ~ print('Here are the first 3 in the list.')
# ~ for asd in people[0:3]:
	# ~ print(asd.title())
### Here we learnt how to slice a list and do a loop through the slice

# ~ people = ['martins', 'george', 'bob', 'caleb', 'sam']
# ~ my_people = people[:]
# ~ my_people.append('jonathan')
# ~ print(my_people)
# ~ print(people)
### copying is useful as it gives you a different list to work on
### a = b and a = b[:] is very different

# ~ lister = ['apple', 'bottom', 'jeans', 'coconut', 'nut', 'not']
# ~ print('The middle three elements on this list are:')
# ~ for asd in lister[3:]:
	# ~ print(asd)
	
### Here we learn about tuples!!
### Seems to me tuples are just lists that cannot be edited??
# ~ numbers = (1, 2, 3, 4, 5)
# ~ for number in numbers:
	# ~ print(number)
# ~ numbers = (2, 4, 6, 8, 10)
# ~ for number in numbers:
	# ~ print(number)

# ~ cars = ['audi', 'bmw', 'toyota', 'hyundai']
# ~ for car in cars:
	# ~ if car == 'bmw':
		# ~ print(car.upper() + ' is amazing.')
	# ~ else:
		# ~ print(car.upper() + ' is garbage.')

# ~ requested_topping = 'NOT mushroom'
# ~ if requested_topping != 'mushroom':
	# ~ print('STOP IN THE NAME OF THE MUSH-LORD')
# ~ else:
	# ~ print('MUSHMUSHMUSHROOOOOM')

# ~ answer = 12
# ~ if answer != 42:
	# ~ print('thats where youre wrong kiddo')

# ~ names = ['adam', 'eve', 'paul', 'rob', 'john', 'sam']
# ~ allowed_names = ['adam', 'eve', 'paula', 'rob', 'john', 'james']
# ~ for name in names:
	# ~ if name in allowed_names:
		# ~ print('Hello there ' + name.title())
	# ~ else:
		# ~ print('Get outta here ' + name.title() + ' you dont belong!')

# ~ age = -13
# ~ if 0 < age < 3:
	# ~ print('baby')
# ~ elif age < 6:
	# ~ print('toddler')
# ~ elif age < 20:
	# ~ print('teenager')
# ~ else:
	# ~ print('adult')		
# ~ names = []
# ~ if names:
	# ~ print('hi guys')
# ~ else:
	# ~ print('why is nobody here?!?!')
### if LIST: is a conditional test to test if the list is non-empty.

# ~ available_toppings = ('mushrooms', 'olives', 'pineapple', 'cheese')
# ~ requested_toppings = ['apple', 'mushrooms', 'tomato']
# ~ for requested_topping in requested_toppings:
	# ~ if requested_topping in available_toppings:
		# ~ print('Adding ' + requested_topping)
	# ~ else:
		# ~ print('Sorry we do not have ' + requested_topping + ' in this pizzeria.')
# ~ print('done with the damned pizza!')	

# ~ usernames = ['martins', 'george', 'bob', 'caleb', 'sam', 'admin']
# ~ if usernames:
	# ~ for username in usernames:
		# ~ if username == 'admin':
			# ~ print('Welcome back to SkyNet Lord Horkarthan')
		# ~ else:
			# ~ print('Welcome back ' + username)
# ~ else:
	# ~ print('I am so lonely.')
# ~ current_users = ['martins', 'george', 'bob', 'caleb', 'sam']
# ~ new_users = ['martin', 'George', 'bobby', 'caleb', 'samantha']
# ~ for users in new_users:
	# ~ if users.lower() in current_users:
		# ~ print('Username ' + users + ' is unavailable')
	# ~ else:
		# ~ print(users + ' is allowed')
# ~ asd = list(range(1,10))
# ~ for aa in asd:
	# ~ if aa in asd[0:1]:
		# ~ print('1st')
	# ~ elif aa in asd[0:2]:
		# ~ print('2nd')
	# ~ elif aa in asd[0:3]:
		# ~ print('3rd')
	# ~ else:
		# ~ print(str(aa) + 'th')
		
### Lets start learning about dictionaries. YAY :')

# ~ alien_0 = {'color' : 'green', 'points' : '5'}
# ~ alien_1 = {'color' : 'red', 'points' : '10'}

# ~ print(alien_0['color'])
# ~ print(alien_1['points'])
# ~ print(alien_0)
# ~ alien_0['x_position'] = 0
# ~ alien_0['y_position'] = 25
# ~ print(alien_0)

# ~ alien_0 = {}
# ~ alien_0['color'] = 'green'
# ~ alien_0['points'] = '5'
# ~ print(alien_0)

# ~ alien_0['color'] = 'not green'
# ~ print(alien_0)

# ~ alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
# ~ print("Original x-position: " + str(alien_0['x_position']))

# ~ # Move the alien to the right.
# ~ # Determine how far to move the alien based on its current speed.

# ~ if alien_0['speed'] == 'slow':
	# ~ x_increment = 1
# ~ elif alien_0['speed'] == 'medium':
	# ~ x_increment = 2
# ~ else:
	# ~ #If the only other speed is fast
	# ~ x_increment = 3

# ~ alien_0['x_position'] = alien_0['x_position'] + x_increment

# ~ print("New x-position: " + str(alien_0['x_position']))
# ~ del alien_0['speed']

# ~ favourite_food = {
	# ~ 'jen': 'apple',
	# ~ 'sarah': 'pear',
	# ~ 'jacob': 'jacob biscuit'
	# ~ }
# ~ print(favourite_food['sarah']
	# ~ + ' does this indent work?')

# ~ marge = {'first_name' : 'marge', 'last_name' : 'hammonds', 'city' : 
		# ~ 'new haven'}
		
# ~ print(marge['first_name'])
# ~ print(marge['last_name'])
# ~ print(marge['city'])

# ~ favourite_number = {
	# ~ 'jen' : '4',
	# ~ 'ali' : '911',
	# ~ 'rasputin' : '5050',
	# ~ 'obama' : '89'}

# ~ for name, number in favourite_number.items():
	# ~ print('\n' + name.title() + "'s favourite number is " + str(number))
# ~ for name in favourite_number.keys():
	# ~ print(name.title())

# ~ user_0 = {
	# ~ 'username' : 'bobby99',
	# ~ 'first_name' : 'bobby',
	# ~ 'last_name' : 'niner',
	# ~ }
	
# ~ for x, y in user_0.items():
	# ~ print("\nKey: " + x)
	# ~ print("Value: " + y)

# ~ same_key = {
	# ~ 'apple' : 'fruit',
	# ~ 'apple' : 'not fruit'}
	
# ~ print(same_key['apple'])
# ~ for asd in same_key.keys():
	# ~ print(asd)

# ~ favourite_fruits = {
	# ~ 'john' : 'apple',
	# ~ 'ben' : 'pear',
	# ~ 'sarah' : 'apple',
	# ~ 'jacob' : 'grape',
	# ~ 'lenin' : 'coconut',
	# ~ 'john' : 'pear'}

# ~ for fruit in favourite_fruits.values():
	# ~ print(fruit)
# ~ print('\n')
# ~ print(favourite_fruits['john'])
# ~ print('\n')
# ~ for fruit in set(favourite_fruits.values()):
	# ~ print(fruit)
	
# ~ rivers = {
	# ~ 'egypt' : 'nile',
	# ~ 'usa' : 'mississipi',
	# ~ 'vietnam' : 'mekong',
	# ~ 'singapore' : 'singapore'}

# ~ for country, river in rivers.items():
	# ~ print('The ' + str(river).title() + ' River, runs through ' + str(country).title())
# ~ print('\n')
# ~ for river in rivers.values():
	# ~ print(river)
# ~ print('\n')
# ~ for country in rivers.keys():
	# ~ print(country)

# ~ people_to_poll = ['bob', 'jason', 'albert', 'sarah', 'jon']

# ~ polled = {
	# ~ 'bob' : 'apple',
	# ~ 'bacon' : ' bacons',
	# ~ 'sarah' : 'grape',
	# ~ 'jason' : 'pineapple'}
	
# ~ for people in people_to_poll:
	# ~ if people not in polled.keys():
		# ~ print('Hey ' + people.title() + ' please complete this poll!')
	# ~ else:
		# ~ print('Thanks for doing the poll ' + people.title())

# ~ alien_0 = {'color' : 'green', 'points' : '5'}
# ~ alien_1 = {'color' : 'yellow', 'points' : '10'}
# ~ alien_2 = {'color' : 'red', 'points' : '15'}
# ~ aliens = [alien_0, alien_1, alien_2]

# ~ for alien in aliens:
	# ~ print(alien)
##Make 30 green aliens?

# ~ aliens = []

# ~ for alien_number in range(30):
	# ~ new_alien = {'color' : 'green', 'points' : '5', 'speed' : 'slow'}
	# ~ aliens.append(new_alien)

# ~ for alien in aliens[:5]:
	# ~ print(alien)
# ~ print('...')

# ~ print('Total number of aliens: ' + str(len(aliens)))

# ~ for alien in aliens[:3]:
	# ~ if alien['color'] == 'green':
		# ~ alien['color'] = 'yellow'
		# ~ alien['points'] = '10'
		# ~ alien['speed'] = 'medium'

# ~ for alien in aliens[0:5]:
	# ~ print(alien)
	
# ~ for alien in aliens[:6]:
	# ~ if alien['color'] == 'green':
		# ~ alien['color'] = 'yellow'
		# ~ alien['points'] = '10'
		# ~ alien['speed'] = 'medium'
	# ~ elif alien['color'] == 'yellow':
		# ~ alien['color'] = 'red'
		# ~ alien['points'] = '15'
		# ~ alien['speed'] = 'fast'

# ~ print('\n')
# ~ for alien in aliens[0:10]:
	# ~ print(alien)

# ~ pizza = {
	# ~ 'crust' : 'stuffed',
	# ~ 'toppings' : ['mushroom', 'pineapple', 'cheese'],
	# ~ }
# ~ print('You ordered a ' + pizza['crust'] + 
	# ~ 'crusted pizza with the following toppings:')

# ~ for topping in pizza['toppings']:
	# ~ print('\t' + topping)

# ~ fav_lang = {
	# ~ 'jen' : ['python', 'ruby'],
	# ~ 'bob' : ['c', 'kilton'],
	# ~ 'phil' : ['go'],
	# ~ 'eddy' : ['python', 'go'],
	# ~ }

# ~ for name, languages in fav_lang.items():
	# ~ if len(languages) > 1:
		# ~ print('\n' + name.title() + "'s favourite languages are:")
		# ~ for language in languages:
			# ~ print('\t' + language.title())
	# ~ elif len(languages) == 1:
		# ~ print('\n' + name.title() + "'s favourite language is:")
		# ~ for language in languages:
			# ~ print('\t' + language.title())

# ~ pet_1 = {
	# ~ 'name' : 'kibble',
	# ~ 'animal' : 'cat',
	# ~ 'owner' : 'skipper'}
# ~ pet_2 = {
	# ~ 'name' : 'floofy',
	# ~ 'animal' : 'hamster',
	# ~ 'owner' : 'freddy'}
# ~ pet_3 = {
	# ~ 'name' : 'yuri',
	# ~ 'animal' : 'dog',
	# ~ 'owner' : 'rasputin'}
	
# ~ pets = [pet_1, pet_2, pet_3]

# ~ for pet in pets:
	# ~ print("\nName: " + pet['name'].title())
	# ~ print("Type of animal: " + pet['animal'])
	# ~ print("Owner: " + pet['owner'].title())

# ~ favourite_number = {
	# ~ 'jen' : [4, 5, 6],
	# ~ 'ali' : [911, 420],
	# ~ 'rasputin' : [5050, 1010],
	# ~ 'obama' : [42],
	# ~ }
# ~ for person, numbers in favourite_number.items():
	# ~ if len(numbers) > 1:
		# ~ print('\n' + person.title() + "'s favourite numbers are:")
		# ~ for number in numbers:
			# ~ print(number)
	# ~ elif len(numbers) == 1:
		# ~ print('\n' + person.title() + "'s favourite number is:")
		# ~ for number in numbers:
			# ~ print(number)

### time to learn while loops page 150
# ~ message = input('Tell me something, and I will repeat it back to you: ')
# ~ print(message)

# ~ name = input("Please enter your name: ")
# ~ print('Hello ' + name.title())

# ~ prompt = 'If you tell us who you are, we can personalize the message you see!'
# ~ prompt += '\nWhat is your first name? '
# ~ name = input(prompt)
# ~ print('\nHello ' + name.title())

# ~ age = input('How old are you? ')
# ~ print(age)
# ~ age = int(age)
# ~ print(age + 1)

# ~ height = input('How tall are you? ')
# ~ height = int(height)

# ~ if height >= 140:
	# ~ print('\nYou are tall enough to ride this ride!')
# ~ else:
	# ~ print('Get outta here shorty!')
	
# ~ number = input('Enter a number, and I will tell you if it is even or odd: ')
# ~ number = int(number)

# ~ if number % 2 == 0:
	# ~ print('\nThe number ' + str(number) + ' is even!')
# ~ else:
	# ~ print('\nThe number ' + str(number) + 'is odd!')

# ~ car = input('What car would you like to buy? ')
# ~ print('\nLet me see if I can find you a nice new ' + car.title() + '.')

# ~ number_people = input('How many seats will you be needing Sir? ')
# ~ number_people = int(number_people)
# ~ if number_people > 8:
	# ~ print('I am sorry but you will have to wait a while.')
# ~ else:
	# ~ print('Your table is ready!')

# ~ number = input('Enter a number, and I will tell you if it is a multiple of 10: ')
# ~ number = int(number)

# ~ if number % 10 == 0:
	# ~ print(str(number) + ' is a multiple of 10.')
# ~ else:
	# ~ print(str(number) + ' is not a multiple of 10.')

# ~ current_number = input('give me a number more than 5')
# ~ current_number = int(current_number)
# ~ while current_number <= 9999999999999999:
	# ~ print(current_number)
	# ~ current_number += 1

# ~ prompt = "Tell me something, and I will repeat it back to you: "
# ~ prompt += "\nEnter 'quit' to end the program. "

# ~ message = ""
# ~ while message != 'quit' :
	# ~ message = input(prompt)
	# ~ if message != 'quit':
		# ~ print(message)

# ~ prompt = "Tell me something, and I will repeat it back to you: "
# ~ prompt += "\nEnter 'quit' to end the program. "

# ~ active = True
# ~ while active:
	# ~ message = input(prompt)
	
	# ~ if message == 'quit':
		# ~ active = False
	# ~ else:
		# ~ print(message)

# ~ prompt = "Please enter the name of the city you've visited: "
# ~ prompt += "\n(Enter 'quit' when youre finished.) "

# ~ while True:
	# ~ city = input(prompt)
	
	# ~ if city == 'quit':
		# ~ break
	# ~ else:
		# ~ print("I'd love to go to " + city.title() + '.')

# ~ prompt = "\nIs Faruq a smart guy? "

# ~ while True:
	# ~ facts = input(prompt)
	
	# ~ if facts == 'yes':
		# ~ print('That is absolutely right! You are almost as smart as Faruq')
		# ~ break
	# ~ else:
		# ~ print('Sorry that is the wrong answer. Try again!')

# ~ current_number = 1
# ~ while current_number < 10:
	# ~ current_number += 1
	# ~ if current_number % 2 == 0:
		# ~ continue
	# ~ else:
		# ~ print(current_number)

# ~ pizza_toppings = []
# ~ actual_toppings = ['mushrooms', 'cheese', 'pineapples', 'olives']
# ~ prompt = "What pizza toppings would you like to have? "

# ~ while True:
	# ~ toppings = input(prompt)
	# ~ if toppings == 'quit':
		# ~ print('Your delicious pizza is all ready!')
		# ~ print('It contains the following topppings: ')
		# ~ print(pizza_toppings)
		# ~ break
	# ~ elif toppings in actual_toppings:
		# ~ print("Adding " + toppings + ' to your pizza!')
		# ~ print('\n')
		# ~ pizza_toppings.append(toppings)
	# ~ else:
		# ~ print("Sorry but we do not have that topping.")
		# ~ print("Would you like to choose from these toppings? \n")
		# ~ for topping in actual_toppings:
			# ~ print(topping)
		# ~ print('\n')

# ~ prompt = "Hi, could you please tell me your age so I can charge you accordingly. "
# ~ while True:
	# ~ age = input(prompt)
	# ~ age = int(age)
	# ~ if age < 3:
		# ~ print("Your movie ticket is FREE! Enjoy! \n NEXT PLEASE! \n")
	# ~ elif age < 12:
		# ~ print("Your movie ticket will be $10. Have a nice day! \nNEXT PLEASE! \n")
	# ~ elif age == 100:
		# ~ break
	# ~ else:
		# ~ print("Your movie ticket will be $12. Have a nice day! \nNEXT PLEASE! \n")
# ~ age = 2
# ~ while True:
	# ~ print(age)
	# ~ age = age**2

# ~ unconfirmed_users = ['alice', 'ben', 'candace']
# ~ confirmed_users = []

# ~ while unconfirmed_users:
	# ~ current_user = unconfirmed_users.pop()
	
	# ~ print("Verifying user: " + current_user.title())
	# ~ confirmed_users.append(current_user)
	
# ~ print('\nThe following users have been confirmed: ')
# ~ for confirmed_user in confirmed_users:
	# ~ print(confirmed_user.title())

# ~ pets = ['dog', 'hamster', 'cat', 'cat', 'gerbil', 'cat', 'rabbit', 'cat']
# ~ print(pets)

# ~ while 'cat' in pets:
	# ~ pets.remove('cat')

# ~ print(pets)

# ~ responses = {}

# Set a flag to dictate that polling is active.

# ~ polling_active = True

# ~ while polling_active:
	# ~ name = input("\nWhat is your name? ")
	# ~ response = input("Which fruit is your favourite? ")
	# ~ responses[name] = response
	
	# ~ repeater = input("would you like another person to respond? (yes/no). ")
	# ~ if repeater == 'yes':
		# ~ continue
	# ~ elif repeater == 'no':
		# ~ polling_active = False
		
# ~ print("\n===== Poll Results =====")
# ~ for name, response in responses.items():
	# ~ print(name.title() + "'s favourite fruit is " + response + '.')

# ~ asd = {'color' : 'green', 'points' : '15'}
# ~ for color, points in asd.items():
	# ~ print(color + points)

# ~ ### Ala Sandwiches Deli

# ~ finished_sandwiches = {
	# ~ 'tuna sandwich' : 0,
	# ~ 'marinara sandwich' : 0,
	# ~ 'egg mayo sandwich' : 0,
	# ~ 'tuna mayo sandwich' : 0,
	# ~ }
# ~ types_of_sandwich = ['tuna sandwich', 
	# ~ 'marinara sandwich', 
	# ~ 'egg mayo sandwich',
	# ~ 'tuna mayo sandwich',
	# ~ ]
# ~ welcome = 'Hi, welcome to Ala Sandwiches Deli!'
# ~ welcome += '\nMay I take your order? '

# ~ store_open = True

# ~ while store_open:
	# ~ order = input(welcome)
	# ~ if order in types_of_sandwich:
		# ~ print("One " + order + ' coming right up!')
		# ~ finished_sandwiches[order] += 1
		# ~ next_up = input("Is there anyone that wants to order next? (yes/no) ")
		# ~ if next_up == 'yes':
			# ~ continue
		# ~ elif next_up == 'no':
			# ~ break
	# ~ else:
		# ~ print("Sorry we dont have that here. These are our selections \n")
		# ~ for type_of_sandwich in types_of_sandwich:
			# ~ print(type_of_sandwich)
		# ~ print('\n')



# ~ print("\nTotal orders for today: ")
# ~ for sandwich, quantity in finished_sandwiches.items():
	# ~ print(sandwich.title() + ' : ' + str(quantity))

# ~ def greet_user(username):
	# ~ print("Hello " + username.title() + '!')
	
# ~ greet_user('faruq')

# ~ def flex():
	# ~ print("currently I am learning how to use functions in python!")
# ~ flex()

# ~ def book(title):
	# ~ print("One of my favourite books is " + title.title() + "!")
# ~ book('a wrinkle in time')

# ~ def describe_pet(type_animal, pet_name):
	# ~ print('\nI have a pet ' + type_animal + '.')
	# ~ print('His name is ' + pet_name.title())

# ~ describe_pet('cat', 'adam west')
# ~ describe_pet('dog', 'buster')
# ~ describe_pet(type_animal = 'creeper', pet_name = 'psssssssssss')
# ~ describe_pet(pet_name = 'Oof', type_animal = 'Steve')

# ~ def describe_pet(pet_name, type_animal = 'dog'):
	# ~ print('\nI have a pet ' + type_animal + '.')
	# ~ print('His name is ' + pet_name.title())
# ~ describe_pet('adam west', 'cat')
# ~ describe_pet('buster')

# ~ def make_shirt(shirt_size, shirt_text):
	# ~ print('Your shirt size is ' + str(shirt_size) + '.')
	# ~ print('Your shirt will say: ' + shirt_text)
# ~ make_shirt(5, 'sky is blue')
# ~ make_shirt(shirt_text = 'pink is rain', shirt_size = 14)

# ~ def make_shirt(shirt_size = 'large', shirt_text = 'I love Python'):
	# ~ print('Your shirt size is ' + shirt_size + '.')
	# ~ print('Your shirt will say ' + shirt_text + '.')
# ~ make_shirt()
# ~ make_shirt('medium')
# ~ make_shirt('small', 'I hate Python')
	
# ~ def describe_city(city, country = 'malaysia'):
	# ~ print(city.title() + ' is in ' + country.title())
# ~ describe_city('johor')
# ~ describe_city('melaka')
# ~ describe_city('hanoi', 'vietnam')
	
# ~ def get_formatted_name(first_name, last_name, middle_name = ''):
	# ~ full_name = first_name + ' ' + middle_name + ' '+ last_name
	# ~ return full_name.title()
	
# ~ musician = get_formatted_name('bob', 'marley')
# ~ print(musician)
	
# ~ musician = get_formatted_name('john', 'jovi', 'bon')
# ~ print(musician)
# ~ people = []
# ~ def build_person(name, age_, gender_, job_):
	# ~ name = {'age' : age_, 'gender' : gender_, 'job' : job_}
	# ~ people.append(name)
	# ~ return name
# ~ person_0 = build_person('faruq', 20, 'male', 'student')
# ~ print(faruq)
# ~ print(people)
	
# ~ def get_formatted_name(first_name, last_name, middle_name = ''):
	# ~ full_name = first_name + ' ' + middle_name + ' '+ last_name
	# ~ return full_name.title()
	
# ~ while True:
	# ~ print('\nPlease tell me your name:')
	# ~ f_name = input('First name: ')
	# ~ if f_name == 'q':
		# ~ break
	# ~ l_name = input('Last name: ')
	# ~ if l_name == 'q':
		# ~ break
	
	# ~ formatted_name = get_formatted_name(f_name, l_name)
	# ~ print("\nHello " + formatted_name + '!')

# ~ def city_country(city, country):
	# ~ print(city.title() + ', ' + country.title())
# ~ city_country("singapore", 'singapore')
# ~ city_country('johor', 'malaysia')
# ~ city_country('melaka', 'malaysia')
	
# ~ def make_album(artist_name, album_title):
	# ~ album = {
		# ~ 'By' : artist_name,
		# ~ 'Title' : album_title
		# ~ }
	# ~ return album
# ~ list_of_albums = []
# ~ print('Lets input an album! \n')
# ~ continue_making = True
# ~ while continue_making:
	# ~ a_name = input("Who is the album by? \n")
	# ~ a_title = input("What is the album called? \n")

	# ~ ## making of album
	
	# ~ album_dic = make_album(a_name, a_title)
	
	# ~ print(album_dic)
	# ~ list_of_albums.append(album_dic)
	# ~ print('\nHere are your list of albums: ')
	# ~ for contents in list_of_albums:
		# ~ print(contents)
		
	# ~ while True:
		# ~ quitter = input('\nDo you want to input another album? (yes/no)')
		# ~ if quitter == 'yes':
			# ~ print('\n')
			# ~ break
		# ~ elif quitter == 'no':
			# ~ continue_making = False
			# ~ break
		# ~ else:
			# ~ continue
# ~ print('\nThank you for inputting albums!')
		
# ~ def greet_users(names):
	# ~ for name in names:
		# ~ msg = "Hello there " + name.title() + '!'
		# ~ print(msg)
# ~ usernames = ['bob', 'sam', 'josh']

# ~ greet_users(usernames)
	
# ~ unprinted_designs = ['iphone case', 'rhombic dodecahedron', 'icosahedron']
# ~ completed_models = []
	
# ~ def print_models(unprinted_designs, completed_models):
	# ~ while unprinted_designs:
		# ~ current_design = unprinted_designs.pop()
		# ~ print("\nPrinting model: " + current_design)	
		# ~ completed_models.append(current_design)

# ~ def show_completed_models(completed_models):
	# ~ print("\nThe following models have been printed:")
	# ~ for completed_model in completed_models:
		# ~ print(completed_model)
		
# ~ print_models(unprinted_designs[:], completed_models)

# ~ unprinted_designs.append('koala bear')
# ~ unprinted_designs.append('magnificent lion')

# ~ show_completed_models(completed_models)

# ~ print_models(unprinted_designs, completed_models)

# ~ show_completed_models(completed_models)

# ~ magicians = ['bob', 'sarah', 'jacob', 'samantha']
# ~ def show_magicians(list_magicians):
	# ~ for magician in list_magicians:
		# ~ print(magician)
# ~ show_magicians(magicians)
# ~ great_magicians = []
# ~ def show_great(list_magicians):
	# ~ for magician in list_magicians:
		# ~ great_magicians.append('great ' + magician)
# ~ show_great(magicians)
# ~ print(magicians)
# ~ print(great_magicians)

# ~ def make_pizza(size, *toppings):
	# ~ """Print the list of toppings that have been requested"""
	# ~ print('\nMaking a ' + str(size) + ' inch pizza with the following toppings: ')
	# ~ for topping in toppings:
		# ~ print('- ' + topping)
# ~ make_pizza(16, 'pepperoni')
# ~ make_pizza(24, 'mushrooms', 'green peppers', 'extra cheese')

# ~ def build_profile(first, last, **user_info):
	# ~ """Build a dictionary containing everything we know about the user"""
	# ~ profile = {}
	# ~ profile['first_name'] = first
	# ~ profile['last_name'] = last
	# ~ for key, value in user_info.items():
		# ~ profile[key] = value
	# ~ return profile

# ~ user_profile = build_profile('muhammad', 'faruq', age = 20, gender = 'male',
	# ~ country = 'singapore')

# ~ print(user_profile)


# ~ def my_sandwich(*ingredients):
	# ~ print('Your sandwich will contain the following ingredients: ')
	# ~ for ingredient in ingredients:
		# ~ print('- ' + ingredient)
		
# ~ my_sandwich('tomato', 'lettuce', 'bacon', 'beef')

# ~ def car_info(manuf, mod_name, **cars_info):
	# ~ car_profile = {}
	# ~ car_profile['manufacturer'] = manuf
	# ~ car_profile['model name'] = mod_name
	# ~ for key, value in cars_info.items():
		# ~ car_profile[key] = value
	# ~ return car_profile
# ~ car = car_info('subaru', 'outback', color = 'blue', insurance = True)
# ~ print(car)

# ~ import pizza

# ~ pizza.make_pizza(16, 'pepperoni')
# ~ pizza.make_pizza(24, 'mushrooms', 'green peppers', 'pineapples')

""" For importing modules, we need to include the line
	import file_name
	file_name.function_name()
	Do take note that the file needs to be in the same folder as the 
	original program file that requires the module."""

# ~ from pizza import make_pizza
# ~ make_pizza(24, 'mushrooms', 'green peppers', 'pineapples')

""" Or you can specify the function you want to import 
	by using 'from file_name import function_name'
	From here you can freely use the function without the 
	prefix file_name."""

# ~ from pizza import make_pizza as mp

# ~ mp(24, 'pepperoni', 'mushrooms', 'pinapples')

"""from file_name import function_name as new_function_name"""

# ~ import pizza as p
# ~ p.make_pizza(24, 'pepperoni', 'bell peppers')

"""import file_name as shorter_file_name"""

# ~ from pizza import *

# ~ make_pizza(24, 'pepperoni', 'chives')

# ~ class Dog():
	# ~ """A simple attempt to model a dog."""
	
	# ~ def __init__(self, name, age):
		# ~ """Initialize name and age attributes."""
		# ~ self.name = name
		# ~ self.age = age
	# ~ def sit(self):
		# ~ """Simulate a dog sitting in response to a command"""
		# ~ print(self.name.title() + ' is now sitting.')
		
	# ~ def roll_over(self):
		# ~ """Simulate rolling over in response to a command"""
		# ~ print(self.name.title() + ' rolled over!')
		
# ~ my_dog = Dog('willie', 6)
# ~ your_dog = Dog('kibble', 4)
# ~ print("My dog's name is " + my_dog.name.title() + '.')
# ~ print("My dog is " + str(my_dog.age) + " years old.")

# ~ my_dog.sit()

# ~ print("\nYour dog's name is " + your_dog.name.title() + '.')
# ~ print("Your dog is " + str(your_dog.age) + " years old.")
# ~ your_dog.roll_over()

# ~ class Restaurant():
	# ~ """A simple restaurant."""
	# ~ def __init__(self, restaurant_name, cuisine_type):
		# ~ self.restaurant_name = restaurant_name
		# ~ self.cuisine_type = cuisine_type
		
	# ~ def describe_restaurant(self):
		# ~ print("Welcome to " + self.restaurant_name.title() + " we serve "
			# ~ + self.cuisine_type + ".")
		
	# ~ def open_restaurant(self):
		# ~ print(self.restaurant_name.title() + " is now open for business!")

# ~ restaurant_0 = Restaurant('ping yu', 'chinese')
# ~ restaurant_1 = Restaurant('krafti', 'western')
# ~ restaurant_2 = Restaurant('muthu curry', 'indian')

# ~ restaurant_0.describe_restaurant()
# ~ restaurant_0.open_restaurant()
# ~ print('\n')
# ~ restaurant_1.describe_restaurant()
# ~ restaurant_1.open_restaurant()
# ~ print('\n')
# ~ restaurant_2.describe_restaurant()
# ~ restaurant_2.open_restaurant()

# ~ class User():
	# ~ def __init__(self, first_name, last_name, login_attempts=0):
		# ~ self.first_name = first_name
		# ~ self.last_name = last_name
		# ~ self.full_name = first_name + " " + last_name
		# ~ self.login_attempts = login_attempts
		
	# ~ def describe_user(self):
		# ~ print("First name: " + self.first_name.title())
		# ~ print("Last name: " + self.last_name.title())
		# ~ print("Full name: " + self.full_name.title())
	
	# ~ def greet_user(self):
		# ~ print("Hello " + self.full_name.title() + "!")
		
	# ~ def increment_login_attempts(self):
		# ~ self.login_attempts += 1
		
	# ~ def reset_login_attempts(self):
		# ~ self.login_attempts = 0
		
	# ~ def call_login_attempts(self):
		# ~ print("\n" + self.full_name.title() + " have attempted to log in " 
			# ~ + str(self.login_attempts) + " times.")
		
# ~ user_0 = User('albert', 'einstein')
# ~ user_1 = User('issac', 'newton')
# ~ user_2 = User('marie', 'curie')

# ~ """Increasin Login attempts"""
# ~ user_0.increment_login_attempts()
# ~ user_0.increment_login_attempts()
# ~ user_0.increment_login_attempts()
# ~ user_0.increment_login_attempts()
# ~ user_0.reset_login_attempts()
# ~ user_0.call_login_attempts()

# ~ user_0.describe_user()
# ~ user_0.greet_user()
# ~ print('\n')
# ~ user_1.describe_user()
# ~ user_1.greet_user()
# ~ print('\n')
# ~ user_2.describe_user()
# ~ user_2.greet_user()
# ~ print('\n')
		
# ~ class Car():
	# ~ """A simple attempt to represent car."""
	
	# ~ def __init__(self, make, model, year):
		# ~ """Initialize attributes to describe car."""
		# ~ self.make = make
		# ~ self.model = model
		# ~ self.year = year
		# ~ self.odometer_reading = 0
		
	# ~ def get_descriptive_name(self):
		# ~ """Return a neatly formatted descriptive name."""
		# ~ long_name = str(self.year) + " " + self.make + " " + self.model
		# ~ return long_name.title()
		
	# ~ def read_odometer(self):
		# ~ """Print a statement showing the car's mileage."""
		# ~ print("This car has " + str(self.odometer_reading) + " miles on it.")
		
	# ~ def update_odometer(self, mileage):
		# ~ if mileage >= self.odometer_reading:
			# ~ self.odometer_reading = mileage
		# ~ elif mileage < self.odometer_reading:
			# ~ print("You cannot roll back an odometer!")
			
	# ~ def increment_odometer(self, miles):
		# ~ """Add the given amount to odometer reading."""
		# ~ self.odometer_reading += miles
	
# ~ my_new_car = Car('audi', 'a4', 2016)
# ~ print(my_new_car.get_descriptive_name())
# ~ my_new_car.update_odometer(15000)
# ~ my_new_car.read_odometer()
# ~ my_new_car.update_odometer(100)
# ~ my_new_car.read_odometer()
# ~ my_new_car.increment_odometer(100)
# ~ my_new_car.read_odometer()

# ~ class Restaurant():
	# ~ """A simple restaurant."""
	# ~ def __init__(self, restaurant_name, cuisine_type, number_served=0):
		# ~ self.restaurant_name = restaurant_name
		# ~ self.cuisine_type = cuisine_type
		# ~ self.number_served = number_served
		
	# ~ def describe_restaurant(self):
		# ~ print("Welcome to " + self.restaurant_name.title() + " we serve "
			# ~ + self.cuisine_type + ".")
		
	# ~ def open_restaurant(self):
		# ~ print(self.restaurant_name.title() + " is now open for business!")

	# ~ def set_number_served(self, served):
		# ~ self.number_served = served
		
	# ~ def increment_number_served(self, increment):
		# ~ self.number_served += increment

# ~ restaurant_0 = Restaurant('ping yu', 'chinese', 10)
# ~ restaurant_1 = Restaurant('krafti', 'western', 25)
# ~ restaurant_2 = Restaurant('muthu curry', 'indian')

# ~ restaurant_0.describe_restaurant()
# ~ restaurant_0.open_restaurant()
# ~ print('\n')
# ~ restaurant_1.describe_restaurant()
# ~ restaurant_1.open_restaurant()
# ~ print('\n')
# ~ restaurant_2.describe_restaurant()
# ~ restaurant_2.open_restaurant()

# ~ print(restaurant_0.number_served)
# ~ restaurant_2.set_number_served(95)
# ~ restaurant_2.increment_number_served(95)
# ~ print(restaurant_2.number_served)

# ~ class Car():
	# ~ """A simple attempt to represent a car."""
	# ~ def __init__(self, make, model, year):
		# ~ self.make = make
		# ~ self.model = model
		# ~ self.year = year
		# ~ self.odometer_reading = 0
		
	# ~ def get_descriptive_name(self):
		# ~ long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		# ~ return long_name.title()
		
	# ~ def read_odometer(self):
		# ~ print("This car has " + str(self.odometer_reading) + " miles on it.")
		
	# ~ def update_odometer(self, mileage):
		# ~ if mileage >= self.odometer_reading:
			# ~ self.odometer_reading = mileage
		# ~ else:
			# ~ print("You can't roll back an odometer!")
			
	# ~ def increment_odometer(self, miles):
		# ~ self.odometer_reading += miles


# ~ class Battery():
	# ~ """A simple attempt to model a battery."""
	
	# ~ def __init__(self, battery_size=70):
		# ~ self.battery_size = battery_size
		
	# ~ def describe_battery(self):
		# ~ """Print a statement describing battery size."""
		# ~ print("This car has a " + str(self.battery_size) + "-kWh battery.")
	
	# ~ def get_range(self):
		# ~ """Print a statement about the range this battery provides."""
		# ~ if self.battery_size == 70:
			# ~ range = 240
		# ~ elif self.battery_size == 85:
			# ~ range = 270
			
		# ~ message = "This car can go approximately " + str(range)
		# ~ message += " miles on full charge."
		# ~ print(message)
	
	# ~ def upgrade_battery(self):
		# ~ if self.battery_size == 70:
			# ~ self.battery_size = 85
			# ~ print("Battery size upgraded to 85-kWh")
		# ~ elif self.battery_size == 85:
			# ~ print("No further upgrades can be done to your battery!")


# ~ class ElectricCar(Car):
	# ~ """It's like a car but its electric!"""
	# ~ def __init__(self, make, model, year):
		# ~ """Initialize attributes of parent class.
		# ~ Then initiallizes the attributes to an electric car"""
		# ~ super().__init__(make, model, year)
		# ~ self.battery = Battery()
		
# ~ my_tesla = ElectricCar('tesla', 'model s', 2016)
# ~ print(my_tesla.get_descriptive_name())
# ~ my_tesla.battery.describe_battery()
# ~ my_tesla.battery.get_range()
# ~ my_tesla.battery.upgrade_battery()
# ~ my_tesla.battery.get_range()
# ~ my_tesla.battery.upgrade_battery()
# ~ my_tesla.battery.get_range()

# ~ class Restaurant():
	# ~ """A simple restaurant."""
	# ~ def __init__(self, restaurant_name, cuisine_type, number_served=0):
		# ~ self.restaurant_name = restaurant_name
		# ~ self.cuisine_type = cuisine_type
		# ~ self.number_served = number_served
		
	# ~ def describe_restaurant(self):
		# ~ print("Welcome to " + self.restaurant_name.title() + " we serve "
			# ~ + self.cuisine_type + ".")
		
	# ~ def open_restaurant(self):
		# ~ print(self.restaurant_name.title() + " is now open for business!")

	# ~ def set_number_served(self, served):
		# ~ self.number_served = served
		
	# ~ def increment_number_served(self, increment):
		# ~ self.number_served += increment

# ~ class IceCreamStand(Restaurant):
	# ~ """Ice Cream Stand modeled after a restaurant"""
	# ~ def __init__(self, restaurant_name, cuisine_type, flavours, number_served=0):
		# ~ """Initializing attributes of ICS"""
		# ~ super().__init__(restaurant_name, cuisine_type, number_served=0)
		# ~ self.flavours = flavours

	# ~ def all_flavours(self):
		# ~ print("These are the list of flavours we offer: ")
		# ~ for flavour in self.flavours:
			# ~ print("- " + flavour)

# ~ my_ice_cream_stall_flavours = ['blueberry', 
	# ~ 'strawberry', 
	# ~ 'mango',
	# ~ 'chocolate chips',
	# ~ ]
# ~ my_ice_cream_stall = IceCreamStand('fruity loops', 'ice cream', my_ice_cream_stall_flavours)

# ~ my_ice_cream_stall.describe_restaurant()
# ~ my_ice_cream_stall.open_restaurant()
# ~ my_ice_cream_stall.all_flavours()

# ~ class User():
	# ~ def __init__(self, first_name, last_name, login_attempts=0):
		# ~ self.first_name = first_name
		# ~ self.last_name = last_name
		# ~ self.full_name = first_name + " " + last_name
		# ~ self.login_attempts = login_attempts
		
	# ~ def describe_user(self):
		# ~ print("First name: " + self.first_name.title())
		# ~ print("Last name: " + self.last_name.title())
		# ~ print("Full name: " + self.full_name.title())
	
	# ~ def greet_user(self):
		# ~ print("Hello " + self.full_name.title() + "!")
		
	# ~ def increment_login_attempts(self):
		# ~ self.login_attempts += 1
		
	# ~ def reset_login_attempts(self):
		# ~ self.login_attempts = 0
		
	# ~ def call_login_attempts(self):
		# ~ print("\n" + self.full_name.title() + " have attempted to log in " 
			# ~ + str(self.login_attempts) + " times.")


# ~ class Privileges():
	# ~ def __init__(self, privileges):
		# ~ self.privileges = privileges
	
	# ~ def call_privileges(self):
		# ~ print("These are the privileges you have: ")
		# ~ for privilege in self.privileges:
			# ~ print("- " + privilege)

# ~ class Admin(User):
	# ~ """Admin is a SuperUser"""
	
	# ~ def __init__(self, first_name, last_name, privileges, login_attempts=0):
		# ~ super().__init__(first_name, last_name, login_attempts=0)
		# ~ self.privilege = Privileges(privileges)
	
	


# ~ super_user = Admin('super', 'user', [
	# ~ 'can add post',
	# ~ 'can delete post',
	# ~ 'can ban users'], 5)

# ~ super_user.describe_user()
# ~ super_user.greet_user()
# ~ super_user.privilege.call_privileges()

# ~ from car import Car

# ~ my_new_car = Car('audi', 'a6', 2016)
# ~ print(my_new_car.get_descriptive_name())

# ~ my_new_car.odometer_reading = 23
# ~ my_new_car.read_odometer()

# ~ from electric_car import ElectricCar

# ~ my_tesla = ElectricCar('tesla', 'model t', 2019)
# ~ print(my_tesla.get_descriptive_name())
# ~ my_tesla.battery.describe_battery()
# ~ my_tesla.battery.get_range()

# ~ my_beetle = Car('volkswagen', 'beetle', '1997')
# ~ print(my_beetle.get_descriptive_name())

# ~ from restaurant import Restaurant

# ~ my_restaurant = Restaurant('Ala Mode', 'French', 77)

# ~ my_restaurant.describe_restaurant()

# ~ from user import Admin

# ~ super_user = Admin('albert', 'einstein', [
	# ~ 'can kill users',
	# ~ 'can make people cry',
	# ~ 'can use profanities'])

# ~ super_user.privilege.call_privileges()

# ~ from collections import OrderedDict

# ~ favourite_languages = OrderedDict

# ~ favourite_languages['jen'] = 'python'
# ~ favourite_languages['sarah'] = 'c'
# ~ favourite_languages['edward'] = 'ruby'
# ~ favourite_languages['phil'] = 'python'

# ~ for name, language in favourite_languages.items():
	# ~ print(name.title() + "'s favourite langauge is " + 
	# ~ language.title() + ".")

# ~ from random import randint


# ~ while True:
	# ~ guess_number = input("Make a guess from 1 to 10! Guess: ")
	# ~ x = randint(1,10)
	# ~ print(x)
	# ~ if guess_number == str(x):
		# ~ print("\nWell done you have guessed it right!")
		# ~ play_again = input("Do you want to play again? (y/n)")
		# ~ if play_again == 'y':
			# ~ print('\n')
			# ~ continue
		# ~ elif play_again == 'n':
			# ~ break
	# ~ elif guess_number != str(x):
		# ~ print("\nOh no, better luck next time!")
		# ~ play_again = input("Do you want to play again? (y/n)")
		# ~ if play_again == 'y':
			# ~ continue
			# ~ print('\n')
		# ~ elif play_again == 'n':
			# ~ break

# ~ from random import randint

# ~ def rolling():	
	# ~ print("\nHere are your rolls: ")
	# ~ print('\n' + str(r_1) + "  " + str(r_2) + "  " + str(r_3) +
	# ~ "  " + str(r_4) + "  " + str(r_5))
	
# ~ print("Let's play Yahtzee")
"""Rolling dice game. To win roll 5 for all 5 dice"""

"""Manual Version"""
# ~ number_of_rolls = 0
# ~ while True:
	# ~ message = "To roll the dice, press [ENTER]."
	# ~ message += "If not, type 'quit'."
	# ~ want_to_roll = input(message)
	# ~ if want_to_roll == "":
		# ~ number_of_rolls += 1
		# ~ r_1 = randint(1,6)
		# ~ r_2 = randint(1,6)
		# ~ r_3 = randint(1,6)
		# ~ r_4 = randint(1,6)
		# ~ r_5 = randint(1,6)
		# ~ rolling()
		# ~ if r_1 == r_2 == r_3 == r_4 == r_5 == 5:
			# ~ print("YAHTZEE!!!")
			# ~ print("\nIt took you " + str(number_of_rolls) + " to win!")
			# ~ number_of_rolls = 0
		# ~ else:
			# ~ continue

# ~ """Automatic Yahtzee!"""
# ~ def start_rolling():
	# ~ auto_roll = True
	# ~ number_of_rolls = 0
	# ~ while auto_roll:
		# ~ r_1 = randint(1,6)
		# ~ r_2 = randint(1,6)
		# ~ r_3 = randint(1,6)
		# ~ r_4 = randint(1,6)
		# ~ r_5 = randint(1,6)
		# ~ rolling()
		# ~ number_of_rolls += 1
		# ~ if r_1 == r_2 == r_3 == r_4 == r_5 == 5:
			# ~ print("YAHTZEE!!!")
			# ~ print("\nIt took you " + str(number_of_rolls) + " to win!")
			# ~ number_of_rolls = 0
			# ~ auto_roll = False
		# ~ else:
			# ~ continue

# ~ begin_game = input("Would you like to start rolling? (y/n) ")
# ~ if begin_game == 'y':
	# ~ start_rolling()
# ~ else:
	# ~ print("Thank you for playing!")

# ~ from random import randint

# ~ class Die():
	# ~ """Simple Dice roller"""
	# ~ def __init__(self, number_of_sides):
		# ~ self.sides = number_of_sides
		
	# ~ def roll_die(self):
		# ~ x = randint(1, self.sides)
		# ~ print(x)
		
# ~ six_sided_die = Die(20)
# ~ six_sided_die.roll_die()

# ~ Chapter 10!! 40 more pages to alien invasion!

# ~ with open('pi_digits.txt') as file_object:
	# ~ for line in file_object:
		# ~ print(line.rstrip())
		

# ~ with open('python_resource_files\chapter_10\pi_digits.txt') as file_object:
	# ~ lines = file_object.readlines()
	
# ~ print(lines)
# ~ for line in lines:
	# ~ print(line.rstrip())

# ~ pi_string = ''
# ~ for line in lines:
	# ~ pi_string += line.strip()
# ~ print(pi_string)
# ~ print(len(pi_string))
# ~ filename = 'python_resource_files\chapter_10\pi_million_digits.txt'

# ~ with open(filename) as file_object:
	# ~ lines = file_object.readlines()
# ~ pi_string = ''
# ~ for line in lines:
	# ~ pi_string += line.strip()
	
# ~ print(pi_string[:52] + '...')
# ~ print(len(pi_string))

# ~ birthday = input("Enter your birthday in the form of ddmmyy: ")
# ~ if birthday in pi_string:
	# ~ print("Your birthday appears in the first million digits of pi!")
# ~ else:
	# ~ print("Your birthday does not appear in the first million digits of pi.")

# ~ with open('learning_python.txt') as file_object:
	# ~ for line in file_object:
		# ~ print(line.strip())
		
	# ~ lines = file_object.readlines()
# ~ for a in lines:
	# ~ print(a.strip())

# ~ with open("learning_python.txt") as file_object:
	# ~ for line in file_object:
		# ~ print(line.strip())
	# ~ doggy_file = file_object.readlines()

# ~ doggy_string = '' 
# ~ for lines in doggy_file:
	# ~ doggy_string += '\n' + lines.rstrip()
# ~ print(doggy_string)
# ~ catty_string = doggy_string.replace('dog', 'cat')
# ~ print(catty_string)

# ~ filename = 'learning_python.txt'

# ~ with open(filename, 'a') as file_object:
	# ~ file_object.write("I love finding meaning in large datasets.\n")
	# ~ file_object.write("I love creating apps that can run in the browser.\n")

# ~ while True:
	# ~ user_name = input("What is your name? ")
	# ~ if user_name == 'quit':
		# ~ break
	# ~ else:
		# ~ print("Welcome " + user_name + '!')
		# ~ with open('guest_book.txt', 'a') as file_object:
			# ~ file_object.write("\nUsername: " + user_name)
		# ~ programming_love = input("Why do you like programming " + user_name + "?")
		# ~ with open('guest_book.txt', 'a') as file_object:
			# ~ file_object.write("\nReasons for liking programming: " + programming_love)

# ~ try:
	# ~ print(5/0)
# ~ except ZeroDivisionError:
	# ~ print("You can't devide by zero!")

# ~ print("Give me two numbers and I will divide them.")
# ~ print("Enter 'q' to quit.")

# ~ while True:
	# ~ first_number = input("\nFirst number: ")
	# ~ if first_number == 'q':
		# ~ break
	# ~ second_number = input("\nSecond number: ")
	# ~ if second_number == 'q':
		# ~ break
	# ~ try:	
		# ~ answer = int(first_number)/int(second_number)
	# ~ except ZeroDivisionError:
		# ~ print("\nYou can't devide by zero!")
	# ~ else:
		# ~ print(answer)

# ~ filename = 'garbage_text.txt'

# ~ def count_words(filename):
	# ~ """ To count number of words in a file! """
	# ~ try:
		# ~ with open(filename) as f_obj:
			# ~ contents = f_obj.read()
	# ~ except FileNotFoundError:
		# ~ msg = "Sorry, the file '" + filename + "' does not exist."
		# ~ print(msg)
		# ~ pass
	# ~ else:
		# ~ words = contents.split()
		# ~ num_words = len(words)
		# ~ print("The file contains " + str(num_words) + " number of words!")

# ~ filenames = ['garbage_text.txt', 'guest_book.txt', 'pi_million_digits.txt', 'nope.txt']
# ~ for filename in filenames:
	# ~ count_words(filename)

# ~ print("I can help you add two numbers!")
# ~ print("Key in 'q' to end the program.")

# ~ while True:
	# ~ first_number = input("\nFirst number: ")
	# ~ if first_number == 'q':
		# ~ break
	# ~ second_number = input("\nSecond number: ")
	# ~ if second_number == 'q':
		# ~ break
	# ~ try:
		# ~ answer = int(first_number) + int(second_number)
	# ~ except ValueError:
		# ~ print("Please enter numbers, not text!")
	# ~ else:
		# ~ print("\nThe answer is " + str(answer) + "!")

# ~ filenames = ['cats.txt', 'dogs.txt']
# ~ for filename in filenames:
	# ~ try:	
		# ~ with open(filename) as file_object:
			# ~ read_file = file_object.read()

	# ~ except FileNotFoundError:
		# ~ print("The file " + filename + " does not exist!")
		
	# ~ else:
		# ~ print(read_file)
	
# ~ filename = 'garbage_text.txt'

# ~ with open(filename) as file_object:
	# ~ read_file = file_object.read()
# ~ print(read_file.lower().count('row'))

# ~ import json

# ~ numbers = [2, 3, 5, 7, 11, 13]

# ~ filename = 'numbers.json'
# ~ with open(filename, 'w') as f_obj:
	# ~ json.dump(numbers, f_obj)

# ~ import json

# ~ filename = 'numbers.json'
# ~ with open(filename) as f_obj:
	# ~ numbers = json.load(f_obj)

# ~ print(numbers)

# ~ import json

# ~ username = input("What is your name? ")

# ~ filename = 'username.json'
# ~ with open(filename, 'w') as f_obj:
	# ~ json.dump(username, f_obj)
	# ~ print("We'll remember you when you come back, " + username + "!")

# ~ import json

# ~ filename = 'username.json'

# ~ with open(filename) as f_obj:
	# ~ username = json.load(f_obj)
	# ~ print("Welcome back " + username + "!")
# ~ import json

# ~ def greet_user():
	# ~ """Greet user by name."""
	# ~ filename = 'username.json'
	# ~ try:
		# ~ with open(filename) as file_object:
			# ~ username = json.load(file_object)
	# ~ except FileNotFoundError:
			# ~ username = input("What is your name?")
			# ~ with open(filename, 'w') as file_object:
				# ~ json.dump(username, file_object)
				# ~ print("We'll remember you when you come back " + uusername + '.')
	# ~ else:
			
			# ~ print("Welcome back " + username + "!")

# ~ greet_user()

# ~ i 


# ~ import json

# ~ def get_new_fav_num():
	# ~ fav_number = input("What is your favourite number? ")
	# ~ filename = 'favnum.json'
	# ~ with open(filename, 'w') as f_obj:
		# ~ json.dump(fav_number, f_obj)
		# ~ print("We will remember your favourite number!")

# ~ def get_fav_num():
	# ~ filename = 'favnum.json'
	# ~ try:
		# ~ with open(filename) as f_obj:
			# ~ fav_number = json.load(f_obj)
		# ~ return fav_number
	# ~ except FileNotFoundError:
		# ~ return None

# ~ def show_fav_num():
	# ~ favourite_number = get_fav_num()
	# ~ if favourite_number:
		# ~ print("I know your favourite number! It is " + favourite_number + ".")
	# ~ else:
		# ~ get_new_fav_num()

# ~ show_fav_num()

# ~ def get_formatted_name(first, last):
	# ~ full_name = first + ' ' + last
	# ~ return full_name.title()
	
# ~ from name_function import get_formatted_name

# ~ print("Enter 'q' at any time to quit.")
# ~ while True:
	# ~ first = input("\nFirst Name: ")
	# ~ if first == 'q':
		# ~ break
	# ~ last = input("Last Name: ")
	# ~ if last == 'q':
		# ~ break
	
	# ~ formatted_name = get_formatted_name(first, last)
	# ~ print("\tNeatly formatted name: " + formatted_name + '.')

# ~ import unittest
# ~ from name_function import get_formatted_name

# ~ class NameTestCase(unittest.TestCase):
	# ~ """Tests for name_function.py"""
	
	# ~ def test_first_last_name(self):
		# ~ """Do names like 'Janis Joplin' work?"""
		# ~ formatted_name = get_formatted_name('janis', 'joplin')
		# ~ self.assertEqual(formatted_name, 'Janis Joplin')
	
# ~ unittest.main()

# ~ import unittest
# ~ from name_function import get_formatted_name

# ~ class NamesTestCase(unittest.TestCase):
	# ~ """Tests for 'name_function.py'."""
	
	# ~ def test_first_last_name(self):
		# ~ """Do names like Albert Einstein work?"""
		# ~ formatted_name = get_formatted_name('albert', 'einstein')
		# ~ self.assertEqual(formatted_name, 'Albert Einstein')
		
	# ~ def test_first_last_middle_name(self):
		# ~ """Do names like Gloria Poppy Borger work?"""
		# ~ formatted_name = get_formatted_name('gloria', 'borger', 'poppy')
		# ~ self.assertEqual(formatted_name, 'Gloria Poppy Borger')
		
# ~ unittest.main()
# ~ import unittest
# ~ from city_functions import get_city_country

# ~ class CityCountryTest(unittest.TestCase):
	# ~ """Test for city_functions.py"""
	# ~ def test_city_country(self):
		# ~ """Do places like 'Madrid, Spain' work?"""
		# ~ formatted_city_country = get_city_country('madrid', 'spain')
		# ~ self.assertEqual(formatted_city_country, 'Madrid, Spain')
		
	# ~ def test_city_country_population(self):
		# ~ """Test for city_functions_population"""
		# ~ formatted_city_country_population = get_city_country('bangkok', 'thailand', '5000000')
		# ~ self.assertEqual(formatted_city_country_population, 'Bangkok, Thailand - population 5000000')
# ~ unittest.main()

# ~ from survey import AnonymousSurvey

# ~ # Define a question and make a survey.
# ~ question = "What language did you first learn to speak?"
# ~ my_survey = AnonymousSurvey(question)

# ~ # Show the question, and store responses
# ~ my_survey.show_question()
# ~ print("Enter 'q' at any time to quit.\n")
# ~ while True:
	# ~ response = input("Language: ")
	# ~ if response == 'q':
		# ~ break
	# ~ my_survey.store_response(response)

# ~ # Show the survey results.
# ~ print("\nThank you for your response!")
# ~ my_survey.show_results()

# ~ import unittest
# ~ from survey import AnonymousSurvey

# ~ class TestAnonymousSurvey(unittest.TestCase):
	# ~ """Tests for class AnonymousSurvey"""
	
	# ~ def setUp(self):
		# ~ """
		# ~ Create a survey and a set of responses to be tested.
		# ~ """
		# ~ question = "What language did you first learn to speak?"
		# ~ self.my_survey = AnonymousSurvey(question)
		# ~ self.input_responses = ['English', 'Spanish', 'Chinese']

	# ~ def test_store_single_response(self):
		# ~ self.my_survey.store_response(self.input_responses[0])
		# ~ self.assertIn(self.input_responses[0], self.my_survey.responses)
		
	# ~ def test_store_three_responses(self):
		# ~ for response in self.input_responses:
			# ~ self.my_survey.store_response(response)
		# ~ for response in self.input_responses:
			# ~ self.assertIn(response, self.my_survey.responses)

# ~ unittest.main()

# ~ import unittest
# ~ from employee import Employee

# ~ class TestEmployee(unittest.TestCase):
	# ~ """Tests class Employee"""
	
	# ~ def setUp(self):
		# ~ self.employee_0 = Employee('adn', 'azhari', 1)
		
	# ~ def test_give_default_raise(self):
		# ~ new_salary = self.employee_0.salary + 5000
		# ~ self.employee_0.give_raise()
		# ~ self.assertEqual(new_salary, self.employee_0.salary)
	
	# ~ def test_give_custom_raise(self):
		# ~ custom_raise = 5402
		# ~ new_salary = self.employee_0.salary + 5402
		# ~ self.employee_0.give_raise(5402)
		# ~ self.assertEqual(new_salary, self.employee_0.salary)

# ~ unittest.main()


















