# Functions go here
# This function will ask the user to input a number between the set character limit
def num_check(question, char_min, char_max):
    """Checks users enter an integer / float that is more than zero (or the optimal exit code)"""

    response = input(question)

    is_int = any(char.isdigit() for char in response)
    if is_int == True:
        if response < char_min:
            print(f"Please enter an integer between {char_min} and {char_max}")
        elif response > char_max:
            print(f"Please enter an integer between {char_min} and {char_max}")
        else:
            print(f"You have added {amount}x {item} to your recipe")
    elif is_int == False:
        print("Please enter an integer")

# Main routine goes here

# Loop for testing purposes:
while True:
    # For testing purposes, the item that the user has chosen is lettuce
    item = "lettuce"
    # Ask the user how much of their chosen food item they want and returns the value
    amount = num_check(f"Please enter an amount of {item}: ", 1, 99)
