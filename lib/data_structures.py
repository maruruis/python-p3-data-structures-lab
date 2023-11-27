def get_names(spicy_foods):
    names = []
    for spicy_food in spicy_foods:
        names.append(spicy_food["name"])
    return names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for spicy_food in spicy_foods:
        if spicy_food["heat_level"] > 5:
            spiciest_foods.append(spicy_food)
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        print(spicy_food["name"] + " 🌶️")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if spicy_food["cuisine"] == cuisine:
            return spicy_food
    return None

def print_spiciest_foods(spicy_foods):
    for spicy_food in spicy_foods:
        print(spicy_food["name"] + " 🌶️")

def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    for spicy_food in spicy_foods:
        total_heat_level += spicy_food["heat_level"]
    average_heat_level = total_heat_level / len(spicy_foods)
    return average_heat_level

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods