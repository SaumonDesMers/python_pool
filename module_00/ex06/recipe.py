title = '{:_^50}\n'
cookbook = {
    'sandwich': {'ingredients': {'ham', 'bread', 'cheese', 'tomatoes'}, 'meal': 'lunch', 'prep_time': '10'},
    'cake': {'ingredients': {'flour', 'sugar', 'eggs'}, 'meal': 'dessert', 'prep_time': '60'},
    'salade': {'ingredients': {'avocado', 'arugula', 'tomatoes', 'spinach'}, 'meal': 'lunch', 'prep_time': '15'},
}


def print_recipe(name):
    print(title.format(name.upper()))
    for key, value in cookbook[name].items():
        print(key + ':', value)


def print_cookbook():
    for name in cookbook:
        print_recipe(name)
        print()


def del_recipe(name):
    del cookbook[name]


def add_recipe():
    name = input('\nName:')
    cookbook[name] = {}
    cookbook[name]['ingredients'] = list(filter(None, input('List of ingredients separated by spaces:').split(' ')))
    cookbook[name]['meal'] = input('Type of meal:')
    cookbook[name]['prep_time'] = input('Preparation time:')


while (1):
    print('Please select an option by typing the corresponding number:')
    print('1: Add a recipe')
    print('2: Delete a recipe')
    print('3: Print a recipe')
    print('4: Print the cookbook')
    print('5: Quit')
    n = input('>>')
    if n == '1':
        add_recipe()
    elif n == '2':
        name = input('\nPlease enter the recipe\'s name you want to delete:\n>>')
        del_recipe(name)
    elif n == '3':
        name = input('\nPlease enter the recipe\'s name to get its details:\n>>')
        print_recipe(name)
    elif n == '4':
        print_cookbook()
    elif n == '5':
        print('\nCookbook closed.')
        exit()
    else:
        print('\nBad input')
    print()
