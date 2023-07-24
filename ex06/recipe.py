import sys
import string


def recipe_name():
	print("here is all the recipe: ")
	for x in cookbook:
		print(x)
	print('----------------\n')

def recipe_details(name):
	print (f"for make a {name} we need: ")

	#i print my ingredient
	for x in cookbook[name]['ingredient']:
		print (x)


	print ('\nthis meal it a', cookbook[name]['meal'])
	time = cookbook[name]['prep_time']
	print (f'and it took {time} minute to be ready for eat')
	print('----------------\n')


def remove_recipe(name):
	del cookbook[name]


def add_recipe():
	recipe_name = input("enter a name: ")
	if recipe_name in cookbook.keys():
		print('it already exist')
		return
	my_str = [input(">>>>Enter a the ingredient: ")]
	ingredient = my_str
	while my_str != [''] :
		my_str = [input(">>>>other ingredient ? If not press on enter: ")]
		ingredient += my_str
	meal = input(">>>>enter a meal: ")
	time_prep = input(">>>>enter the time of preparation: ")
	new_recipe = {
		recipe_name:{
		'ingredient': ingredient,
		'meal': meal,
		'prep_time': time_prep
		}
	}
	cookbook.update(new_recipe)
	print(new_recipe)

cookbook = {
'Sandwich':{
'ingredient': ['ham', 'bread', 'cheese', 'tomatoes'],
'meal': 'lunch',
'prep_time': '10'
},

'Cake':{
'ingredient': ['flour', 'sugar', 'eggs'],
'meal': 'dessert',
'prep_time': '60'
},

'Salad':{
'ingredient': ['avocado', 'arugula', 'tomatoes', 'spinach'],
'meal': 'lunch',
'prep_time': '15'
}

}


print("welcom to the programme!")
print('this is the valide option: ')
print('1: add recipe\n2: delete recipe\n3: print recipe\n4: print the cookbook')
print("5: quit")
my_option = input("please choose the number of your option: ")
while(my_option != '5'):
	try:
		if my_option == '4':
			recipe_name()
		elif my_option == '3':
			the_recipe = input('wich one do you want see ? ')
			recipe_details(the_recipe)
		elif my_option == '2':
			to_remove = input('wich one do you want remove ? ')
			remove_recipe(to_remove)
		elif my_option == '1':
			add_recipe()
		else:
			print("this number doesn't exist")
		my_option = input("please choose the number of your option: ")
	except:
		print("ERROR")
print("good bye")
