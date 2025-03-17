# Functions Go Here
def ingredient_check(question, valid_ingredients=['cheese', 'lettuce', 'tomato', 'chicken',
'pasta','rocket', 'onion', 'capsicum', 'spring onion', 'soy sauce', 'vinegar', 'salt', 'pepper'], num_letters = 3):
    """Checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        if response == 'xxx':
            return 'xxx'

        for item in valid_ingredients:

            # Check if response is in the entire word
            if response == item:
                return item

            elif response == item[0]:
                return item

        print(f"Please choose an option from the following: {valid_ingredients}")
# Main Routine Goes Here
recipe = []

while True:
    ingredient = ingredient_check("Please enter an ingredient: ")
    if ingredient == 'xxx':
        break
    recipe.append(ingredient)
    print(f"You added {ingredient} to your recipe")
    print()
    print(f"You're recipe so far is {recipe}")
