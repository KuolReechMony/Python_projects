# Words counter: Counts words based on the number of spaces


def menu(file_name):
    with open(file_name, "r") as user_file:
        verify = user_file.readable()
        if verify == True:
            output = user_file.read()
        
        return output

text = menu(file_name = input("What file do you want feedback on: "))


words = 0
for i in range(len(text)):
    if text[i] == " ":
        words += 1

print(str(words+1) + " words")

