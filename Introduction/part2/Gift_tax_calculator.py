#Some say paying taxes makes Finns happy, so let's see if the secret of happiness lies in one of the taxes set out in Finnish tax code.

#According to the Finnish Tax Administration, a gift is a transfer of property to another person against no compensation or payment. If the total value of the gifts you receive from the same donor in the course of 3 years is €5,000 or more, you must pay gift tax.

gift = int(input("Value of gift:"))

gift = int(input("Value of gift:"))

if gift < 5000:
    print("No tax!")
elif gift >= 1000000:
    minus = gift - 1000000
    add = 142100 + minus * 0.17
    print(f"Amount of tax: {add} euros")
elif gift >= 200000:
    minus = gift - 200000
    add = 22100 + minus * 0.15
    print(f"Amount of tax: {add} euros")
elif gift >= 55000:
    minus = gift - 55000
    add = 4700 + minus * 0.12
    print(f"Amount of tax: {add} euros")
elif gift >= 25000:
    minus = gift - 25000
    add = 1700 + minus * 0.10
    print(f"Amount of tax: {add} euros")
elif gift >= 5000:
    minus = gift - 5000
    add = 100 + minus * 0.08
    print(f"Amount of tax: {add} euros")
else:
    print("No Tax!")
    
#Reflection: i am starting to love this coding! 
    