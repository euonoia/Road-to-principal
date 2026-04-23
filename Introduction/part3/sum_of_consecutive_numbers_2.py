#Please write a new version of the program in the previous exercise. In addition to the result it should also print out the calculation performed:

#Sample output
#Limit: 2
#The consecutive sum: 1 + 2 = 3

#Sample output
#Limit: 10
#The consecutive sum: 1 + 2 + 3 + 4 = 10

#Sample output
#Limit: 18
#The consecutive sum: 1 + 2 + 3 + 4 + 5 + 6 = 21

#You may assume the number typed in by the user is always equal to 2 or higher.

#stops if the the total_sum is less than limit
#e.g. limit = 10
limit = int(input("limit:"))
#this will update as the loop does not hit the limit
total_sum = 1 
#this prints out the 1 + 2
current_sum = 2
path = "1"

    #stops the loop if the total_sum is less than limit
while total_sum < limit:
    #this will execute first so that if the loop stops at the limit it will print out the previous
    #e.g. 1 + 2 + 3 + 4
    path += " + " + str(current_sum)

    #this will add total_sum value based on the current_sum value 
    #e.g. 1 + 2 = 3, 3 + 3 = 6, 6 + 4 = 10
    total_sum += current_sum 
    # will keep incrementing the current_sum if the limit still not meet
    current_sum += 1 

#prints the path first which stop early rather than completing the full loop and the total_sum of the updated total_sum
print(f"The consecutive sum: {path} = {total_sum}")