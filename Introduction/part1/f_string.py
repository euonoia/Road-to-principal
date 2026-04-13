#task: expected output 
#my name is Tim Tester, I am 20 years old
#my skills are
# - python (beginner)
# - java (veteran)
# - programming (semiprofessional)
#I am looking for a job with a salary of 2000-3000 euros per month
# needs to be translated into f string these are the not f string version of the code 
name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print("my name is ", name, " , I am ", age, "years old")
print("my skills are")
print("- ", skill1, " (", level1, ")")
print("- ", skill2, " (", level2, ")")
print("- ", skill3, " (", level3, " )")
print("I am looking for a job with a salary of", lower, "-", upper, "euros per month")

# the fixed version of the code with f string
name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000
# the variables is fixed as is the only problem i see is there is no f strings
# i handled he spacings first 
print(f"my name is {name}, I am {age} years old\n")
print("my skills are")
#now we will apply the f strings on here
print(" "+f"- {skill1} ({level1})")
print(" "+f"- {skill2} ({level2})")
print(" "+f"- {skill3} ({level3})\n")
#now we will apply f string on here
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")

#challenge on here is the new f string format and how to use it to make the code more readable and easier to understand. I also learned that f strings can be used to format strings in a more efficient way and it can also make the code more concise. Overall, this was a good learning experience for me.