from sys import argv
scriptName, inputFile = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline())


currentFile = open(inputFile)
print()
print('First let us print the whole file:\n')
print_all(currentFile)
print('Now let us kind of rewind like a tape.\n')
rewind(currentFile)
print('\nLet us print three lines separately:\n\n')
currentLine = 1
print('First Line:')
print_a_line(currentLine, currentFile)

currentLine = currentLine + 1
print('\nSecond Line:')
print_a_line(currentLine, currentFile)

currentLine = currentLine + 1
print('\nThird Line:')
print_a_line(currentLine, currentFile)
print()
