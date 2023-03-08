class Rectangle:
    def __init__(self, length, breadth):
        self.breadth = breadth
        self.length = length


    def find_perimeter(self):
        perimeter = (self.length + self.breadth) * 2
        return perimeter


    def find_area(self):
        area = self.length * self.breadth
        return area


    def show_display(self):
        params = "Rectangle Length: {}\nRectangle Breadth: {}\n".format(self.length, self.breadth)
        comp_area = self.find_area()
        comp_perimeter = self.find_perimeter()
        params += "Perimeter: {}\nArea: {}".format(comp_area, comp_perimeter)
        print(params)


try:
    rect_breadth = float(input("Enter Breadth: "))
    rect_height = float(input('Enter Height: '))
    rectangle = Rectangle(rect_height, rect_breadth)
    rectangle.find_area()
    rectangle.find_perimeter()
    rectangle.show_display()
except ValueError as err:
    print("Error: Numeric data needed: ", err)
    exit()