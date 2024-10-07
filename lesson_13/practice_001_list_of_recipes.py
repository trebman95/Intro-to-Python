# You have a list of recipes, where each recipe contains the ingredients each recipe needs:
recipes = [
    ["yeast", "flour"],
    ["bread", "meat"],
    ["flour", "meat"]
]

# You also have a list of available ingredients.
ingredients = ["yeast", "flour", "meat"]


# Return a list of all recipes that can be made with the ingredients you have.
# Output: [["yeast","flour"], ["flour","meat"]]

def makeable_recipes(recipes, ingredients):

    makeable_recipes = []
    for recipe in recipes:
        can_make = True
        for ingredient in recipe:
            if ingredient not in ingredients:
                can_make = False
                break
        if can_make:
            makeable_recipes.append(recipe)
    return makeable_recipes

print(makeable_recipes(recipes, ingredients))



