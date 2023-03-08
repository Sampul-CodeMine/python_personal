# Dictionary in Python
print("================== DICTIONARY ====================")
print("\nA dictionary once declared cannot be edited or changed.\n")

monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
print("This is the whole month dictionary: ", monthConversion, "\n")
print("Selecting a key: ", monthConversion["Nov"], "\n")
print("Another way to select a key: ", monthConversion.get("Mar"), "\n")
print("The reason why the get() function is used for getting elements from a dictionary is because you can specify a "
      "default value if that key specified is not available.\n")
print("Find Salute: ", monthConversion.get("Sal", "That key Salute does not exist.\n"))
