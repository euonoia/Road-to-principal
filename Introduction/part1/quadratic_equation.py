#Please write a program for solving a quadratic equation of the form ax²+bx+c. The program asks for values a, b and c. It should then use the quadratic formula to solve the equation. The quadratic formula expressed with the Python sqrt function is as follows:

#x = (-b ± sqrt(b²-4ac))/(2a).

#You can assume the equation will always have two real roots, so the above formula will always work.

#An example of expected behaviour:

#Sample output
#Value of a: 1
#Value of b: 2
#Value of c: -8

#The roots are 2.0 and -4.0

from math import sqrt

#  Get the inputs
a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))

# Calculate the "discriminant" (the part under the square root)
discriminant = b**2 - 4*a*c

# 3. Calculate the two roots using the quadratic formula
root1 = (-b + sqrt(discriminant)) / (2 * a)
root2 = (-b - sqrt(discriminant)) / (2 * a)

# 4. Print the results
print(f"The roots are {root1} and {root2}")