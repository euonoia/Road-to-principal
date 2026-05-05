#Please write a function named chessboard, which prints out a chessboard made out of ones and zeroes. The function takes an integer argument, which specifies the length of the side of the board. See the examples below for details:

#chessboard(3)
#print()
#chessboard(6)
#Sample output
#101
#010
#101

#101010
#010101
#101010
#010101
#101010
#010101

# Write your solution here

def chessboard(times):
    """
    Generates a binary representation of a chessboard pattern.
    Uses coordinate parity (sum of row and column indices) to toggle between '1' and '0'.
    """
    i = 1

    # Outer Loop: Manages the rows of the board
    while i <= times:
        j = 1

        # Inner Loop: Manages the individual characters (cells) within each row
        while j <= times:
            # Parity Logic: If the sum of the row (i) and column (j) is even, print '1'.
            # This creates the alternating pattern regardless of board size.
            if (i + j) % 2 == 0:
                print("1", end="")
            else:
                print("0", end="")
            j += 1
            
        # Move to the next line after completing a full row
        print()
        i += 1

    # Final spacing for output clarity
    print()

# Testing the function
if __name__ == "__main__":
    chessboard(3)