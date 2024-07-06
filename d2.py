with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for e in file:
        recipes_name = e.strip()
        ingredients_count = file.readline()
        ingredients = []
        for t in range(int(ingredients_count)):
            recipes = file.readline().strip().split(' | ')
            product, quantity, measure = recipes
            ingredients.append({'ingredient_name': product, 'quantity': int(quantity), 'measure': measure})
        file.readline()
        cook_book[recipes_name] = ingredients


def get_shop_list_by_dishes(dishes, person_count):
    result_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_1 = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                if ingredient_1 in result_list:
                    result_list[ingredient_1] += quantity
                else:
                    result_list[ingredient_1] = {'measure': measure, 'quantity': quantity}
        return result_list

new_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(new_list)