# Functions Go Here
# This function will ask the user to input a string and will then return their response if it isn't blank
def string_check(question):
    """Checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    response = input(question)

    # Checks if the response is blank
    if response == "":
        print(f"This cannot be blank")
        return None
    else:
        return response

# Main Routine Goes Here

while True:
    string = string_check("What is the name of your recipe? ")
    if string != None:
        print(f"Your recipe has been named {string}")
    else:
        continue