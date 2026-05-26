def find_increasing_pairs(arr):
    count = 0  # Start our counter at 0
    
    # Notice the -1 to keep us safe from crashing!
    for i in range(len(arr) - 1): 
        # Your turn: Check if the next number (arr[i+1]) 
        # is strictly greater than the current number (arr[i])
        if arr[i + 1] > arr[i]:
            count += 1  # Add 1 to our count if it is!
            
    return count

# Test case:
print(find_increasing_pairs([1, 3, 2, 5]))  # Should print 2