#The following program contains several syntactic errors. Please fix the program so that the syntax is in order and the program works as specified by the examples below.

 #number = input("Please type in a number: ")
  #if number>100
   #print("The number was greater than one hundred")
    #number - 100
    ##print("Its value is now"+ number)
 #print(number + " must be my lucky number!")
 #print("Have a nice day!)
 
#Sample output
#Please type in a number: 13
#13 must be my lucky number!
#Have a nice day!

#Sample output
#Please type in a number: 101
#The number was greater than one hundred
#Now its value has decreased by one hundred
#Its value is now 1
#1 must be my lucky number!
#Have a nice day!

# what i must do is to see the error by running test i can locate the bug 

# this is the error FAIL: PythonEditorTest: test_over_hundred_0
#Make sure that you can run the program with input 101

# i run the program and see this IndentationError on line 2: unexpected indent

# now i must fix the indentation 

# i must check if the if else have : to make this finally work 

# i have observed that this if statement the second if statement is properly syntaxed and i must change the - into <

# i have seen on input if the number is integer we must do int(input(""))

# i have fixed the indent error to satisfy the error

# upon looking for the error message i stumbled upon this FAIL: PythonEditorTest: test_over_hundred_2
#EOL while scanning string literal (<string>, line 9), i know to myself that i will use f string

# I comment out the line 8,9,10 and found out the print statement of 7 and 10 doesnt close

# new error FAIL: PythonEditorTest: test_over_hundred_1
#Instead of five rows, your program's output is in 1 rows with input 410 and FAIL: PythonEditorTest: test_under_hundred_2
#Instead of two rows, your program's output is in 4 rows with input 84

# now that i have fixed all the syntaxes i will now proceed to fix the logic 

# it said on here anything below the 100 it needs to print the 13 must be my lucky day and have nice day and if the number is more than a hundred it will get the subtracted to show the its value is now 1 1 must be my lucky winner and have a nice day

# this is now the working fixed version
number = int(input("Please type in a number: "))

if number < 100:
   print(f"{number} must be my lucky number!")
   print(f"Have a nice day!")

if number > 100:
    print("The number was greater than one hundred")
    print("Now its value has decreased by one hundred")

    subtract = number - 100

    print(f"Its value is now {subtract}")
    print(f"{subtract} must be my lucky number!")
    print("Have a nice day!")
    
#learned: I am getting confident on myself