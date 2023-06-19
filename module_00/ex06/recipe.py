cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': '10'
    },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': '60'
    },
    'salade': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': '15'
    },
}


def print_recipe(name):
    if name not in cookbook:
        print('recipe {} doesn\'t exist'.format(name))
        return
    print('{:_^50}\n'.format(name.upper()))
    for key, value in cookbook[name].items():
        print(key + ':', value)


def print_cookbook():
    for name in cookbook:
        print_recipe(name)
        print()


def del_recipe(name):
    if name not in cookbook:
        print('recipe {} doesn\'t exist'.format(name))
        return
    del cookbook[name]


def add_recipe(name, ingredients, meal, prep_time):
    cookbook[name] = {}
    cookbook[name]['ingredients'] = ingredients
    cookbook[name]['meal'] = meal
    cookbook[name]['prep_time'] = prep_time


print('Please select an option:')
print('1: Add a recipe')
print('2: Delete a recipe')
print('3: Print a recipe')
print('4: Print the cookbook')
print('5: Quit')

while (1):
    n = input('>>')

    if n == '1':
        name = input('\nName:')
        ingredients = list(
            filter(None, input('Ingredients separated by spaces:').split(' '))
        )
        meal = input('Type of meal:')
        prep_time = input('Preparation time:')
        add_recipe(name, ingredients, meal, prep_time)
    elif n == '2':
        name = input('\nPlease enter the recipe\'s name:\n>>')
        del_recipe(name)
    elif n == '3':
        name = input('\nPlease enter the recipe\'s name:\n>>')
        print_recipe(name)
    elif n == '4':
        print_cookbook()
    elif n == '5':
        print('\nCookbook closed.')
        exit()
    else:
        print('\nBad input')
    print()
