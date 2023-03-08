# filename = open('test.md')
#
# print (filename, "\n")
# print ("Filename is :",filename.name)
# print("File content is: ", filename.read())
#
# filename.close()
#
# print("\n==============================================\n")

file = open("test.txt")
raw_file = file.read()
formatted_file = raw_file.replace(" | ", "\n")
output = formatted_file.split("\n")
print(raw_file, "...(Raw File Content:)")
print(formatted_file, "...(Formatted File Content:)")
print(output, "...(Final Output:)")