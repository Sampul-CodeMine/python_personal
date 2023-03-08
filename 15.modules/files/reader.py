# A safer way to close files in Python

try:
    # Open a file for access or reading from a directory
    file = open('sample.md', 'r', encoding='utf-8')

    print(file.read())  # Reading the content of the file

finally:
    # Closing the file so as not to be accessed any longer
    file.close()


# Another way to safely open and close files in Python programming language.
with open('sample.md', 'a', encoding='utf-8') as file:
    file.write("Adding A New Line To The File\n")

with open('sample.md', 'r', encoding='utf-8') as file:
    file.read()
    teller = file.tell()
    print("Tell:: {}".format(teller))
    from_num = 200
    print("File Content at {}:\n{}".format(from_num, file.read(from_num)))

    seeker = file.seek(0)
    print("File Content at {}:\n{}".format(from_num, file.read(from_num)))

# Reading a file line by line
print("\n=============================================================\nPrint a File Line By Line===================\n")
with open('sample.md', mode='r', encoding='utf-8') as fil:
    for line in fil:
        print(line, end='')

# Reading a file line by line using the readline keyword
print("\n===============================\nPrint a File Line By Line Using ReadLine keyword===================\n")
with open('sample.md', mode='r', encoding='utf-8') as fil:
    print(fil.readline())
