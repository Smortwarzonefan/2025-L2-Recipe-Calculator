# Functions go here
def num_check(question):
    """Checks users enter an integer / float that is more than zero (or the optimal exit code)"""

    error = "Please enter an integer"

    while True:

        try:
            # Changes response to an integer and check that it's more than zero
            response = int(input(question))

            return response

        except ValueError:
            print(error)

# Main routine goes here

# Loop for testing purposes:
while True:
    # For testing purposes, the item that the user has chosen is lettuce
    item = "lettuce"
    # Ask the user how much of their chosen food item they want and returns the value
    amount = num_check(f"Please enter an amount of {item}: ")

    # Output error message / success message
    if amount < 1:
        print(f"Please enter an integer between 1 and 99")
        continue
    elif amount > 99:
        print(f"Please enter an integer between 1 and 99")
        continue
    else:
        print(f"You have added {amount}x {item} to your recipe")
