#Please write a function named print_many_times(text, times), which takes a string and an integer as arguments. The integer argument specifies how many times the string argument should be printed out:

#print_many_times("hi", 5)

#print()

#text = "All Pythons, except one, grow up"
#times = 3
#print_many_times(text, times)

#Sample output
#hi
#hi
#hi
#hi
#hi

#All Pythons, except one, grow up.
#All Pythons, except one, grow up.
#All Pythons, except one, grow up.

def print_many_times(text, times):
    """
    Repeats a given string a specific number of times using a while loop.
    text: The string to be displayed
    times: The number of iterations
    """
    # Initialize the loop counter
    i = 1

    # Iterative execution: Continue printing until the counter exceeds the 'times' parameter
    while i <= times:
        print(text)
        # Increment the control variable to prevent an infinite loop
        i += 1

    # Print a newline for visual separation after the loop completes
    print()
    
# Test block: Calls the function with 'python' as data and '5' as the iteration limit
if __name__ == "__main__":
    print_many_times("python", 5)