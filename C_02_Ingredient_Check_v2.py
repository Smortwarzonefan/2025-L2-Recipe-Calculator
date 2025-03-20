# Functions Go Here
# This function will ask the user for a food item, check if it's a valid salad ingredient, then return the value
def ingredient_check(question, num_letters = 3):
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
# Main Routine Goes Here
recipe = []

# Uses the ingredient checker to ask the user for an ingredient and then adds it to a list for testing purposes
while True:
    ingredient = ingredient_check("Please enter an ingredient: ")
    if ingredient == 'xxx':
        break
    recipe.append(ingredient)
    print(f"You added {ingredient} to your recipe")
    print()
    print(f"You're recipe so far is {recipe}")
