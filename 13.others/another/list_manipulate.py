print("First Method\n======================================================")
list_full = [
    ["Corinthians", "5.2", "Flamingo", "1"],
    ["Sao Paulo", "0", "Botafogo", "2.022"],
    ["Vasco Da Gama", "4", "Fluminense", "4"],
    ["Culluc Slave", "7", "Fluprint", "3.2"]
]
print(list_full, " .... Original List")

names = []
nums = []
for it_loops in list_full:
    for name, num in zip(it_loops[::2], it_loops[1::2]):
        names.append(name)
        nums.append(num)

print(names, " ... Names extracted")
print(nums, " ... Numbers extracted")

print("\nAnother Method\n======================================================")
name = []
num = []
flattened = [item for va in list_full for item in va]
name = flattened[::2]
num = flattened[1::2]
revised = dict(zip(name, num))
print(list_full, " .... Original List")
print(flattened, " ... Flattened Out Extracted List")
print(names, " ... Names extracted")
print(nums, " ... Numbers extracted")
print(f'\n[revised]\n')
for nm, nu in revised.items():
    print(f'{nm:_<15}: {nu}')


print("\nAnother Method\n======================================================")

ext_names = []
ext_nums = []

a = [[ext_names.append(itst) if itst.isalpha() else ext_nums.append(itst) for itst in its] for its in list_full]

# for its in list_full:
#     for itst in its:
#         if itst.isalpha():
#             ext_names.append(itst)
#         else:
#             ext_nums.append(itst)
print(list_full, " .... Original List")
print(names, " ... Names extracted")
print(nums, " ... Numbers extracted")