#Please write a program which asks for the user's name. If the name is Huey, Dewey or Louie, the program should recognise the user as one of Donald Duck's nephews.

#In a similar fashion, if the name is Morty or Ferdie, the program should recognise the user as one of Mickey Mouse's nephews.

#Some examples:

#Sample output
#Please type in your name: Morty
#I think you might be one of Mickey Mouse's nephews.

#Sample output
#Please type in your name: Huey
#I think you might be one of Donald Duck's nephews.

#Sample output
#Please type in your name: Ken
#You're not a nephew of any character I know of.

name = input("Please type in your name:")


if name == "Morty":
    print("I think you might be one of Mickey Mouse's nephews.")
elif name == "Ferdie":
    print("I think you might be one of Mickey Mouse's nephews.")
elif name == "Louie":
    print("I think you might be one of Donald Duck's nephews.")
elif name == "Dewey":
    print("I think you might be one of Donald Duck's nephews.")
elif name == "Huey":
    print("I think you might be one of Donald Duck's nephews.")
else:
    print("not a nephew of any character I know of.")

# this one is hard I listed all the nephews and I changed the I because on else the I keep messing me up
