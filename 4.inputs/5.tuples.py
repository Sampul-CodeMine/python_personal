print('USING TUPLES\n')
# === TUPLES =======
# Tuples are immutable - they cannot be modified. They are like constants.
# You cannot add, delete, update or delete from the TUPLES

names = "dukeson", "samson", "angel", "frank", "williams"
# another way to define or create a tuple is
animals = ("dog", "cat", "cow", "camel", "frog")
print(names)
print("\n{}".format(animals))
print("Is Owl in the animal list? : " )
print("Owl" in animals)
# creating a new tuple from existing tuples
new_tup = animals + names

print(new_tup)
