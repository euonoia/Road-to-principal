def convert_to_snake_case(pascal_or_camel_cased_string):

    # Use a list comprehension to look at every single letter in the input string
    snake_cased_char_list = [
        # IF the character is capital (uppercase), put an underscore in front and make it lowercase
        '_' + char.lower() if char.isupper()
        # ELSE, just keep the character exactly as it is (it's already lowercase)
        else char
        for char in pascal_or_camel_cased_string
    ]

    # Join the list of characters back into a single string.
    # .strip('_') removes any accidental underscore at the very beginning (from the first capital letter).
    return ''.join(snake_cased_char_list).strip('_')

def main():
    # Test the function with a PascalCase string
    print(convert_to_snake_case('IAmAPascalCasedString'))

    
# Run the program
main()