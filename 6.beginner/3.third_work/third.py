# This is an exercise that declares and use variables.
cars = 100
spaceInCar = 4.0
drivers = 30
passengers = 90
carsNotDriven = cars - drivers
carsDriven = drivers
carpool_capacity = carsDriven * spaceInCar
averagePassengersPerCar = passengers / carsDriven

print('There are ', cars, ' cars available.')
print('There are only ', drivers, ' drivers available.')
print('There will be ', carsNotDriven, ' empty cars today.')
print('We can transport ', carpool_capacity, ' people today.')
print('We have ', passengers, ' to carpool today.')
print('We need to put about ', averagePassengersPerCar, ' in each car.')

# this is the end of the program.
