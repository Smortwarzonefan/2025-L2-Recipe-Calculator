# Imports go here
from zipfile import error

import prices_dictionary

# Functions go here
# This function will calculate the cost of individual ingredients
def price_checker(item):
    """Calculates the price of the recipe by getting the set price from
    a list of prices"""

    item = item.lower()
    error = "Sorry, this ingredient is not recognised"

    if item == "cheese":
        cost = prices_dictionary.cheese
        return(f"${cost}")
    elif item == "lettuce":
        cost = prices_dictionary.lettuce
        return(f"${cost}")
    elif item == "tomato":
        cost = prices_dictionary.tomato
        return(f"${cost}")
    elif item == "chicken":
        cost = prices_dictionary.chicken
        return(f"${cost}")
    elif item == "pasta":
        cost = prices_dictionary.pasta
        return(f"${cost}")
    elif item == "rocket":
        cost = prices_dictionary.rocket
        return(f"${cost}")
    elif item == "onion":
        cost = prices_dictionary.onion
        return(f"${cost}")
    elif item == "capsicum":
        cost = prices_dictionary.capsicum
        return(f"${cost}")
    elif item == "spring onion":
        cost = prices_dictionary.spring_onion
        return(f"${cost}")
    elif item == "soy sauce":
        cost = prices_dictionary.soy_sauce
        return(f"${cost}")
    elif item == "vinegar":
        cost = prices_dictionary.vinegar
        return(f"${cost}")
    elif item == "salt":
        cost = prices_dictionary.salt
        return(f"${cost}")
    elif item == "pepper":
        cost = prices_dictionary.pepper
        return(f"${cost}")
    elif item == "beef":
        cost = prices_dictionary.beef
        return(f"${cost}")
    elif item == "steak":
        cost = prices_dictionary.steak
        return(f"${cost}")
    elif item == "egg":
        cost = prices_dictionary.egg
        return(f"${cost}")
    elif item == "sesame oil":
        cost = prices_dictionary.sesame_oil
        return(f"${cost}")
    elif item == "pork":
        cost = prices_dictionary.pork
        return(f"${cost}")
    elif item == "butter":
        cost = prices_dictionary.butter
        return(f"${cost}")
    elif item == "olive oil":
        cost = prices_dictionary.olive_oil
        return(f"${cost}")
    elif item == "peanut oil":
        cost = prices_dictionary.peanut_oil
        return(f"${cost}")
    elif item == "mayonnaise":
        cost = prices_dictionary.mayonnaise
        return(f"${cost}")
    elif item == "xxx":
        return("xxx")
    else:
        return error

# Main routine goes here
while True:
    ingredient = input("Name an ingredient: ")
    ingredient_cost = price_checker(ingredient)
    if ingredient_cost == "xxx":
        break
    else:
        print(ingredient_cost)