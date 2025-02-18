import math

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


spicy_food = {
    "name": "Griot",
    "cuisine": "Haitian",
    "heat_level": 10,
}



def get_names(spicy_foods):
    names_list = []
    for food in spicy_foods:
        names_list.append(food["name"])
    return names_list

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_foods.append(food)
    return spiciest_foods


def print_spicy_foods(spicy_foods):
        emoji = "🌶"
        for food in spicy_foods:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {emoji*food['heat_level']}")
print_spicy_foods(spicy_foods)
    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))


def print_spiciest_foods(spicy_foods):
    emoji = "🌶"
    for food in spicy_foods:
        if food["heat_level"] > 5:
           print(f"{food['name']} ({food['cuisine']}) | Heat Level: {emoji*food['heat_level']}") 
print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):
    heat_level = []
    for food in spicy_foods:
        heat_level.append(food["heat_level"])
    return math.floor(sum(heat_level)/len(heat_level))
print(get_average_heat_level(spicy_foods))


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
print(create_spicy_food(spicy_foods, spicy_food))
