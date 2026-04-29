sentence = input("Please type in a sentence: ")

char = input("Please type in a character: ")

index = sentence.find(char)

if index != -1:
    print(sentence[index:index + 3])
else:
    print("Invalid sentence")


