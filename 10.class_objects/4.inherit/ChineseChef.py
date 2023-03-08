from Chef import Chef  # imports the chef class


# the ChineseChef class in parenthesis will inherit all the variables and methods / functions from the Chef class
class ChineseChef(Chef):

    def make_fried_rice(self):
        print("The Chinese Chef makes fried rice.")

    def make_frog(self):
        print("The Chinese Chef makes special Frog soup.")

    def make_special_dish(self):
        print("The Chinese Chef makes a special chinese native dish.")
