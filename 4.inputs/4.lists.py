print('USING LISTS\n')
# === LISTs =======

family = ["Stella", "Dukeson", "Moses", "Victory", "Godleads", "Marvellous", "Gift", "Favour", "Kendra", "Bethel"]
allFamily = family
mother = family[0]
me = family[1]
siblings = family[2:6]
grandChildren = family[8:]
wives = family[6:8]
print("All Family: " + str(allFamily))
print("My Mother: " + str(mother))
print("I am: " + str(me))
print("My Siblings: " + str(siblings))
print("Our Wives: " + str(wives))
print("{}'s Grandchildren: {}".format(str(mother), str(grandChildren)))

friends = ["Samson", "Ejike", "Benjamin", "Osagie", "Daniel", "Michael", "Austin", "Franklin"]
print("\nMODIFYING LIST ELEMENTS\n")
print("All Friends: " + str(friends))
print("Changing List Element's value   ====================================\n")
friends[7] = "Andrew"
friends.append("New Friend")
print("All Friends: " + str(friends))

print("\nAdding Elements To the List   ====================================\n")
friends.append("Cadbury")  # this will append a new item to the end of the friends list
print("New Friends List: " + str(friends))
print("Another way to add an element to the friends list is using the insert keyword.")
friends.insert(7, "Fruitfulness")
friends.append("Richie")
friends.append("")
friends.append("Cadbury")
print("New Friends List: " + str(friends))

print("\nDeleting Elements To the List====================================\n")
# Deleting is with the keyword remove()
friends.remove("")
print("New Friends List: " + str(friends))

print("\nCheck how many times an item appears in a List====================================\n")
print("How many times Cadbury appeared in the list: " + str(friends.count("Cadbury")))

print("\nCopying A List unto another List====================================\n")
animals = ["Lions", "Dogs", "Fish", "Beasts"]
friends.extend(animals)
copied = friends.copy()
print("Copied List in New Variable : " + str(copied))

print("\nExtending or Appending A List to Another List====================================\n")
newList = ["Obeche", "Mahogany", "Iroko", "Mangroove"]
print("First List: " + str(friends) + "\nNew List: " + str(newList) + "\n")
friends.extend(newList)
print("All lists appended together: " + str(friends))

print("\nChecking if an item exists in a list and then displays the index of the item===============================\n")
found = friends.index("Cadbury")
print("Found Item 'Cadbury' in the list: " + str(found))

print("\nSort the List Items====================================\n")
friends.sort()
print("Sorted List: " + str(friends))

print("\nSort the List Items in Reversed Form====================================\n")
friends.reverse()
print("Sorted List: " + str(friends))

print("\nPop out the last element from the list====================================\n")
friends.pop()
print("All lists items: " + str(friends))

print("\nReset or clear the list====================================\n")
friends.clear()
print("All lists items: " + str(friends))
