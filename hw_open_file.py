def make_recipes_dict(file):
    recipes = {}

    with open (file, "r", encoding = 'utf-8') as f:
        for line in f:
            dish = line.strip()
            ingredients_number = int(f.readline().strip())
            ingr_list = []
            for ingredient_number in range(ingredients_number):
                ingr_dict = {}
                portion = f.readline().strip()
                portion = portion.split(' | ')
                ingr_dict['ingredient_name'] = str(portion[0])
                ingr_dict['quantity'] = int(portion[1])
                ingr_dict['measure'] = portion[2]
                ingr_list.append(ingr_dict)
            recipes[dish] = ingr_list
            f.readline()
    return recipes

def get_shop_list_by_dishes(dishes, person_count):
    recipes_dict = make_recipes_dict("ingredient")
    dishes_user = set(dishes)
    dish_set = set(recipes_dict.keys())
    dishes_wanted = dishes_user.intersection(dish_set)
    ingredients_needed = {}
    for dish in dishes_wanted:
        ingredients = recipes_dict[dish]
        for ingredient in ingredients:
            dict_1 = {}
            dict_1['measure'] = ingredient['measure']
            if ingredient['ingredient_name'] in ingredients_needed.keys():
                ingredient_item = ingredient['ingredient_name']
                dict_1['quantity'] = ingredient['quantity'] * int(person_count) + ingredients_needed[ingredient_item]['quantity']
            else:
                dict_1['quantity'] = ingredient['quantity'] * int(person_count)
            ingredients_needed[ingredient['ingredient_name']] = dict_1
    return ingredients_needed


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

