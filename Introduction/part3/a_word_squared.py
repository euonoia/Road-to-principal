#Please write a function named squared, which takes a string argument and an integer argument, and prints out a square of characters as specified by the examples below.

#squared("ab", 3)
#print()
#squared("aybabtu", 5)
#Sample output
#aba
#bab
#aba

#aybab
#tuayb
#abtua
#ybabt
#uayba
def squared(text, size):
    """
    Generates a square grid of characters by cyclically iterating through 
    the provided 'text' string.
    """
    row = 0
    index = 0

    # Outer Loop: Controls the vertical progression (rows)
    while row < size:
        col = 0
        
        # Inner Loop: Controls the horizontal progression (columns)
        while col < size:
            # Cyclic Indexing Logic: Use the modulo operator (%) to wrap 
            # the index back to 0 once it exceeds the string length.
            char = text[index % len(text)]
            
            print(char, end="")
            
            # Increment the global character pointer and local column counter
            index += 1
            col += 1
            
        # Line break after each row is fully populated
        print()
        row += 1

    # Final spacing for visual clarity
    print()

if __name__ == "__main__":
    squared("aybabtu", 5)