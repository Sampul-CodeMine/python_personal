li  = [3, 2, 4, 1]
sol = [elem*2 for elem in [item+1 for item in li]]
print(sol)

"""Another Method for this List Comprehension"""

itm = []
for item in li:
    val = item+1
    itm.append(val*2)
print(itm)

print()
print()

"""Another example"""
name = {'name': 'Ehis Dukeson'}
result = {'unit': 2, 'test': 21, 'exam': 33, 'total': 54}
print(name)
print(result)
keys = list(name.keys()) + list(result.keys())
rex = list(name.values()) + list(result.values())
print(keys)
print(rex)