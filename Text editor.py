# Key
# rt = read only, text file(file must exist); 
# r+ = read, write, text file(file must exist)
# wt = write only, text file(creates new file if non-existent)
# at = append only, text file(creates new file if non-existent)


with open('Test.txt', 'wt') as file:
    file.write(input('Enter some text to the new file: '))

with open('Test.txt', 'rt') as file:
    print(file.readlines())

