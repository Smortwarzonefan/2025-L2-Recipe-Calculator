# Imports go here
from zipfile import error

import prices_dictionary
import json

# Functions go here
# This function will calculate the cost of individual ingredients
def price_checker(item, num_letters):
    """Calculates the price of the recipe by getting the set price from
    a list of prices"""
    with open('prices_dictionary.py', 'r') as file:
        valid_ingredients = [line.strip() for line in file]
    valid_ingredients_list = open('prices_dictionary.py').read()

    js = json.loads(valid_ingredients_list)

    item = item.lower()
    error = "Sorry, this ingredient is not recognised"

    if item == "xxx":
        return "xxx"

    for i in js:

        # Checks if response is in the list of valid ingredients
        if item == i:
            return js[item]
        if item == i[:num_letters]:
            return js[i]

    # Prints the list of valid ingredients so the user knows what they can input
    print(error)

# Main routine goes here
while True:
    ingredient = input("Name an ingredient: ")
    ingredient_cost = price_checker(ingredient, 3)
    # Stops asking the user for ingredients if they input 'xxx'
    if ingredient_cost == "xxx":
        break
    elif ingredient_cost != None:
        print(ingredient_cost)
    else:
        continue
