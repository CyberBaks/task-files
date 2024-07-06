with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for e in file:
        recipes_name = e.strip()
        ingredients_count = file.readline()
        ingredients = []
        for t in range(int(ingredients_count)):
            recipes = file.readline().strip().split(' | ')
            product, quantity, measure = recipes
            ingredients.append({'ingredient_name': product, 'quantity': quantity, 'measure': measure})
        file.readline()
        cook_book[recipes_name] = ingredients

for recipe, ingredients in cook_book.items():
    print(f"{recipe}:")
    for ing in ingredients:
        print(f'{ing}')