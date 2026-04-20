#The table below outlines the grade boundaries on a certain university course. Please write a program which asks for the amount of points received and then prints out the grade attained according to the table.

#   points	                grade
#   < 0                 impossible!
#   -49	                    fail
#   50-59	                  1
#   60-69	                  2
#   70-79	                  3
#   80-89	                  4
#   90-100	                  5
#   > 100	             impossible!

points = int(input("How many points[0-100]:"))

#i put some print grade on here and use the end syntax to align it with the grade so the Grade print is not always declared
print("Grade: ",end="")

if points < 0:
    print("impossible!")
elif points <= 49:
    print("fail")
elif points <= 59:
    print("1")
elif points <= 69:
    print("2")
elif points <= 79:
    print("3")
elif points <= 89:
    print("4")
elif points <= 100:
    print("5")
else:
    print("impossible!")
