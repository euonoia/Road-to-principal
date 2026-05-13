def verify_card_number(card_number):
    # 1. Reverse the card number string
    # The Luhn algorithm works from right to left. 
    # [::-1] is the most efficient way to flip a string in Python.
    card_number_reversed = card_number[::-1]

    # 2. Handle the "Odd" Positions (1st, 3rd, 5th digits from the right)
    # [::2] starts at index 0 and takes every second character.
    # These digits are summed exactly as they are.
    sum_of_odd_digits = 0
    odd_digits = card_number_reversed[::2]
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    # 3. Handle the "Even" Positions (2nd, 4th, 6th digits from the right)
    # [1::2] starts at index 1 and takes every second character.
    # These digits must be doubled and processed before summing.
    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        
        # If doubling results in a two-digit number (e.g., 14),
        # add the two digits together (1 + 4 = 5).
        if number >= 10:
            # (number // 10) gets the first digit, (number % 10) gets the second.
            number = (number // 10) + (number % 10)
        
        sum_of_even_digits += number

    # 4. Final Validation
    # Total both sums. If the total ends in 0, the card is valid.
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main():
    # Example card number with dashes
    card_number = '4111-1111-4555-1142'
    
    # Cleaning the data: create a translation table to remove dashes and spaces
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    # Execute validation and print result
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

# Standard practice: call the main function to start the program
main()