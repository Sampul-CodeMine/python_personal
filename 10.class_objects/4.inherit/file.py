from Chef import Chef
from ChineseChef import ChineseChef

print("============================ FROM THE CHEF CLASS \n")
# Referencing only the Chef class
myChef = Chef()
myChef.make_chicken()
myChef.make_salad()

print("\n============================ FROM THE CHINESECHEF CLASS \n")
# Referencing only the ChineseChef class
myChineseChef = ChineseChef()
myChineseChef.make_fried_rice()
myChineseChef.make_frog()

print("\n============================ ACCESSING THE CHEF CLASS FROM THE CHINESECHEF CLASS DUE TO INHERITANCE \n")
# Referencing the functions in the chef class from the ChineseChef class
myChineseChef.make_chicken()
myChineseChef.make_salad()

print("\n============================ OVERRIDING INHERITANCE  \n")
# Referencing the functions in the chef class from the ChineseChef class and overriding one of the functions
myChef.make_special_dish()
myChineseChef.make_special_dish()
