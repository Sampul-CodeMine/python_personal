weight_stone = input("How many stones do you weigh?: ")

weight_kg = float(weight_stone) * 6.350293

truncated_kg = round(weight_kg, 2)
# truncated_kg = round(weight_kg * 100) / 100

print(type(weight_stone))
print(type(weight_kg))
print("if you are", str(weight_stone) + "stones, then your weight in Kilogram is:", str(truncated_kg) + "kg")
