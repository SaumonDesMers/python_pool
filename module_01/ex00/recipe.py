class Recipe:
    def __init__(self, name, cooking_lvl, ingredients, description, recipe_type):
        if (type(name) != str
            or type(cooking_lvl) != int
            or type(ingredients) != list
            or type(description) != str
            or type(recipe_type) != str):
            print('Bad input')
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
    
    def __str__(self):
        txt = "Name: {}\nCooking level: {}\nIngredients: {}\nDescription: {}\nRecipe type: {}"
        return txt.format(*self.__dict__.values())
