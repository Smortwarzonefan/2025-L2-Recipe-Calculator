# Functions Go Here
# This function will ask the user to input a string and will then return their response if it isn't blank, doesn't contain numbers and isn't longer than the set character limit
def string_check(question, char_limit):
    """Checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    response = input(question)

    if len(response) > char_limit:
        print(f"Please do not exceed the {char_limit} character limit")
        return None

    if len(response) == "":
        print(f"This cannot be blank")
        return None

    has_number = any(char.isdigit() for char in response)
    if has_number == True:
        print("Please only input characters from the latin alphabet")
        return None
    elif has_number == False:
        return response

# Main Routine Goes Here

while True:
    string = string_check("What is the name of your recipe? ", 25)
    if string != None:
        print(f"Your recipe has been named {string}")
    else:
        continue