import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password using the string module built-ins
    letters = string.ascii_letters  # Contains both lowercase and uppercase letters (a-z, A-Z)
    digits = string.digits          # Contains numbers (0-9)
    symbols = string.punctuation    # Contains special characters/symbols (e.g., !, @, #, $)

    # Combine all individual character sets into one master pool
    all_characters = letters + digits + symbols

    # Infinite loop to keep generating passwords until one meets all security criteria
    while True:
        password = ''
        # Build a password character by character up to the specified length
        for _ in range(length):
            # secrets.choice is cryptographically secure, unlike the standard random module
            password += secrets.choice(all_characters)
        
        # Define a list of tuples linking user-requested minimums to regular expression patterns
        constraints = [
            (nums, r'\d'),                     # \d matches any digit (0-9)
            (special_chars, fr'[{symbols}]'),  # Matches any individual symbol defined in string.punctuation
            (uppercase, r'[A-Z]'),             # Matches capital letters
            (lowercase, r'[a-z]')              # Matches lowercase letters
        ]

        # Check constraints: Evaluate if the generated password satisfies all minimum counts        
        if all(
            # len(re.findall(...)) counts how many times a specific pattern appears in the password
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            # If every single check in the 'all()' generator passes, break out of the infinite loop
            break
    
    # Return the verified, secure password string
    return password
    
# Generate a default 16-character password using the function
new_password = generate_password()
print('Generated password:', new_password)