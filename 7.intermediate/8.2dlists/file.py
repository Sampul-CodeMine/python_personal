print ( "\n 2D LIST \n ")

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print ( "The grid is : ", number_grid )
print ("Length of the grid : ", len(number_grid))
print ("Access specific element in the grid : ", number_grid[0][2])
print ("Access specific element in the grid : ", number_grid[1][1])
print ("Access specific element in the grid : ", number_grid[2][0])
print ("Access specific element in the grid : ", number_grid[3][0])

print ("\n  NESTED LOOPS  =============\n")

for row in number_grid:
    print (row)
print ("\n========================================\n")
for row in number_grid:
    for col in row:
        print (col)