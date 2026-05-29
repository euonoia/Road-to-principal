def palindrome(x):
    text_x = str(x)
    reversed = x[::-1]

    if text_x == reversed:
        return True
    else:
        return False

palindrome("-121")