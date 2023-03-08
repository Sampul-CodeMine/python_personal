# imports the sys class to accept parameters or arguments in the command line.
from sys import argv

# adding the number of arguments to be expected in the command lines
scriptName, fileName = argv

# assigning the file object to a variable
file = open(fileName)

print('This is the content of your file presently:\n')
print(file.read())

# close the file stream for opened file variable
file.close()

# confirm if you want to erase the file's contents
print('Do the following on {} '.format(fileName))
print('Press A - To APPEND to {}'.format(fileName))
print('Press O - To OVERWRITE {}'.format(fileName))
print('Press C - To CANCEL Actions')

# accept inputs
prompt = input(':>> ')

if prompt == "A" or prompt == "a":

    print()
    print('Opening {} and appending to its contents.'.format(fileName))
    target = open(fileName, 'a')

    # we are going to accept inputs and write the new contents to the file that was recently erased.
    print()
    print('We are going to add new contents to the file...')
    print()
    firstLine = input('First Line:: ')
    secondLine = input("Second Line:: ")
    thirdLine = input('Third Line:: ')
    print()
    print('Writing the contents of the three lines to the new lines.')
    print()
    target.write(firstLine)
    target.write('\n')
    target.write(secondLine)
    target.write('\n')
    target.write(thirdLine)
    target.write('\n')
    # closing the filestream for writing to the file
    target.close()

elif prompt == "O" or prompt == "o":

    # creating a variable to handle erase and writing to file
    print()
    print('Opening {} and erasing its contents.'.format(fileName))
    target = open(fileName, 'w')
    target.truncate()

    # we are going to accept inputs and write the new contents to the file that was recently erased.
    print()
    print('We are going to add new contents to the file...')
    print()
    firstLine = input('First Line:: ')
    secondLine = input("Second Line:: ")
    thirdLine = input('Third Line:: ')
    print()
    print('Writing the contents of the three lines to the new lines.')
    print()
    target.write(firstLine)
    target.write('\n')
    target.write(secondLine)
    target.write('\n')
    target.write(thirdLine)
    target.write('\n')
    # closing the filestream for writing to the file
    target.close()

else:
    print('We are not making changes to the file.')


# We are going to display the new content of the file that was overwritten
newFile = open(fileName)
print()
print('The new contents of {} is:'.format(fileName))
print()
print(newFile.read())
print('End of Program\n')
