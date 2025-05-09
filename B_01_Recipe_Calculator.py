"""This program can be used to calculate the cost of a salad recipe by asking
the user to input an ingredient and amount, with which the program will
calculate the price of the individual ingredients + the entire recipe"""
## Imports go here
import json

## Functions go here
def make_statement(statement, decoration, lines=1):
    """Creates headings (3 lines), subheadings (2 lines) and
    emphasised text / mini-headings (1 line). Only use emoji for
    single line statements"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * int(len(middle) / 2)

    if len(statement) < 1:
        print("Statement failed to generate, no statement was inputted")
    elif len(statement) > 100:
        print("Statement failed to generate, 100 character limit exceeded")
    else:
        if lines == 1:
            print(middle)
        elif lines == 2:
            print(middle)
            print(top_bottom)
        else:
            print(top_bottom)
            print(middle)
            print(top_bottom)
def ingredient_check(question, num_letters=3):
    """Checks that users enter the full word
    or the first letter of a word from a list of valid responses"""
    with open('food_dictionary.txt', 'r') as file:
        valid_ingredients = [line.strip() for line in file]
    valid_ingredients_list = open('food_dictionary.txt').read()

    while True:

        response = input(question).lower()

        # If the user inputs 'xxx', the loop will return 'xxx' which tells the code in the main function to stop the loop
        if response == 'xxx':
            return 'xxx'

        for item in valid_ingredients:

            # Check if response is in the list of valid ingredients
            if response == item:
                return item
            # Checks if the response is in the list of valid ingredients and allows the user to input 3 letters instead of the entire word
            elif response == item[:num_letters]:
                return item

        # Prints the list of valid ingredients so the user knows what they can input
        print(f"Please choose an option from the following...\n{valid_ingredients_list}")
def string_check(question, char_limit):
    """Checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    response = input(question)

    if len(response) > char_limit:
        print(f"Please do not exceed the {char_limit} character limit")
        return None

    if response == "":
        print(f"This cannot be blank")
        return None

    has_number = any(char.isdigit() for char in response)
    if has_number == True:
        print("Please only input characters from the latin alphabet")
        return None
    elif has_number == False:
        return response
def num_check(question, char_min, char_max):
    """Checks users enter an integer / float that is more than zero (or the optimal exit code)"""

    response = input(question)

    try:
        amount = int(response)
        if amount < char_min:
            print(f"Please enter an integer between {char_min} and {char_max}")
        elif amount > char_max:
            print(f"Please enter an integer between {char_min} and {char_max}")
        else:
            print(f"You have added {amount}x {chosen_ingredient} to your recipe")
            return int(amount)
    except ValueError:
        print("Please enter an integer")
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

## Main routine goes here

# Declare the program to the user using the make statement function
make_statement("Salad Recipe Calculator", "🥗", 1)
make_statement("Enter ingredients to add to your recipe, enter 'xxx' to stop adding ingredients", "ℹ️", 1)
print()

# Use the string check function to ask the user for a name for their recipe
while True:
    recipe_name = string_check("Please enter a name for your recipe: ", 25)

    if recipe_name == None:
        continue
    else:
        print(f"You're recipe is called {recipe_name}")
        break

# Ask the user to input an ingredient and amount of said ingredient using the ingredient check and price checker functions
ingredient_list = []
total_price = 0

# Begins asking the user for ingredients
while True:
    chosen_ingredient = ingredient_check("Enter an ingredient for your recipe: ", 3)
    # Allows the user to stop inputting ingredients by inputting 'xxx'
    if chosen_ingredient == "xxx":
        break
    else:
        while True:
            amount_ingredient = num_check(f"Enter an amount of {chosen_ingredient}: ", 1, 99)

            if amount_ingredient == None:
                continue
            else:
                for i in range(0, amount_ingredient):
                    ingredient_list.append(chosen_ingredient)
                for i in range(0, amount_ingredient):
                    added_price = price_checker(chosen_ingredient, 3)
                    total_price += added_price
                break
        print(f"Your recipe so far includes: {ingredient_list}")
        print(f"Your total cost so far is: ${total_price}")

make_statement(recipe_name, "🥗", 1)
print(f"Your recipe includes: {ingredient_list}")
print(f"Your total cost is: {total_price}")
print("Thanks for using this recipe calculator!")