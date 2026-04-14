#in the python programming language printing will result to be spaced down what we want on here is to print the single line like ths
#print("Hi ", end="")
#print("there!")
#output
#Hi there!
#based on the given code we will use the end= parameter to make the print statement to be on the same line
#the given problem is 
#print(5)
#print(" + ")
#print(8)
#print(" - ")
#print(4)
#print(" = ")
#print(5 + 8 - 4) this code needs to be appeared on the same line
#first approach i will apply is this
 
#print(5 end="") but it doesnt work

#print(" + ", end="") i found out that the + and 8 is in the same line now i will apply the same approach

#print(end="" " + ", end="") i tried this approach to see if the 5 will come down but it didnt work

#print(5, end="") i tried this approach with the comma and some how the 5 + 8 is in the same line now

#this is the final working version of the code

print(5, end="")
print(" + ", end="")
print(8, end="")
print(" - ", end="")
print(4, end="")
print(" = ", end="")
print(5 + 8 - 4)

#reflection: I learned that when the print is print(5) i can use , to make the next print statement to be on the same line and also i can use end="" to make the next print statement to be on the same line as well. I also learned that i need to stay calm and see for each possible solution




