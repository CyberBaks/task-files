def new_cook_book(file_path):
	with open(file_path, encoding='utf-8') as file:
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
	return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):
	result_list = {}
	for dish in dishes:
		if dish in cook_book:
			for ingredient in cook_book[dish]:
				ingredient_name = ingredient['ingredient_name']
				quantity = ingredient['quantity'] * person_count
				if ingredient_name in result_list:
					result_list[ingredient_name]['quantity'] += quantity
				else:
					result_list[ingredient_name] = {'measure': ingredient['measure'], 'quantity': quantity}
	return result_list


file_path = 'recipes.txt'
cook_book = new_cook_book(file_path)
new_list = get_shop_list_by_dishes(cook_book, ['Омлет', 'Омлет'], 2)
print(new_list)
