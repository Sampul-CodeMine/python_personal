from sys import argv
from os.path import exists

scriptName, fromFile, toFile = argv

print('Copying from {} to {} : ' .format(fromFile, toFile))

inFile = open(fromFile)
inData = inFile.read()

print('The input file:\n\n{}\n is bytes long'.format(inData))
print('Does the output file exist? %r' % exists(toFile))
print('Ready. Hit RETURN to continue, CTRL + C to abort.')
input('>>  ')
outFile = open(toFile, 'w+')
outFile.write(inData)
print()
print('All Done!')
outFile.close()
inFile.close()
# showing the content of the main file
inContent = open(fromFile)
print('The content of {} (Main File) is thus: ' .format(fromFile))
print(inContent.read())
inContent.close()
# showing the content of the new file created
outContent = open(toFile)
print('The content of {} (Copied / New File) is thus: ' .format(toFile))
print(outContent.read())
outContent.close()
