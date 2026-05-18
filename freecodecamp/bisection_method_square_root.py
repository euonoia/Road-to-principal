def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    # Check for negative inputs since real square roots don't exist for them
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    
    # Base case: The square root of 1 is always 1
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
        
    # Base case: The square root of 0 is always 0
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    # Main logic for all other numbers
    else:
        # Initialize search boundaries. 'max' handles numbers between 0 and 1 correctly.
        low = 0
        high = max(1, square_target)
        root = None # Placeholder until we find a close enough answer
        
        # Limit the search loops to prevent an infinite loop
        for _ in range(max_iterations):
            # Find the exact midpoint of our current range
            mid = (low + high) / 2
            square_mid = mid**2

            # Check if our current guess is close enough to the target within our tolerance
            if abs(square_mid - square_target) < tolerance:
                root = mid
                break # Exit the loop early because we found a valid answer

            # If our guess is too small, shift the lower boundary up to the midpoint
            elif square_mid < square_target:
                low = mid
                
            # If our guess is too big, shift the upper boundary down to the midpoint
            else:
                high = mid

        # Handle the case where the loop finished all iterations without hitting the tolerance
        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
    
        # Success case: Print the final approximation
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    
    return root

# Define the number you want to test (you can call the function with this N)
N = 16