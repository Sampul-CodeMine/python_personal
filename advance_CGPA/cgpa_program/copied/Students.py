class GPA(object):
    # data attributes
    """Helps  to calculate the GPA and CGPA"""
    arg1 = arg2 = sub_data = scale = credits = None
    init_course = init_get_credit = total_credits = temp = 0

    def get_course(self):
        self.arg1 = int(input("Number of courses you registered for: "))
        pass

    def get_subject(self, value):
        self.arg2 = value
        pass

    def get_scale(self):
        self.scale = int(input("Enter the scale value (5 or 10): "))
        pass

    def get_subject_data(self):
        self.sub_data = input("Enter the grade: ")
        pass

    def get_grade_data(self):
        if self.scale == 10:
            grade1 = {'s': 10, 'a': 9, 'b': 8, 'c': 7, 'd': 5, 'e': 3, 'f': 0}
            x = grade1[self.sub_data]
        else:
            grade2 = {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1, 'f': 0}
            x = grade2[self.sub_data]
        return x

    def get_credits(self):
        self.credits = int(input("Enter Course Unit/Credit: "))
        pass

    def gpa(self):
        print("CALCULATE GPA")
        sem = int(input("Semester: ? "))
        self.get_scale()
        if self.scale == 5 or self.scale == 10:
            self.get_course()
            if self.arg1 >= 2:
                self.calculate_gpa()
            else:
                print("To calculate the GPA you should have at least 2 subjects minimum.")
        else:
            print("You have not entered the scale correctly. Please try again.")
        pass

    def calculate_gpa(self):
        while self.init_course != self.arg1:
            self.init_course = self.init_course + 1
            self.get_credits()
            self.init_get_credit = self.credits
            self.get_subject_data()
            # type(self.get_subject_data())
            self.temp = self.init_get_credit * self.get_grade_data() + self.temp
            self.total_credits = self.total_credits + self.init_get_credit

        gpa = round((self.temp + .0) / (self.total_credits + .0), 2)
        out_this = """
        You have registered for total credits: {} and you have acquired GPA: {}
        """.format(self.total_credits, gpa)
        print(out_this)
        pass

    def cgpa(self):
        print("CALCULATE YOUR CGPA")
        semesters = input("How many semesters CGPA has to be found for: ")
        counter = temp_init = temp_total_credits = 0
        self.get_scale()
        if self.scale == 5 or self.scale == 10:
            while counter != semesters:
                counter += 1
                print("Enter the details of the semester: {}".format(counter))
                self.get_course()
                self.calculate_gpa()
                temp_init = self.temp + temp_init
                temp_total_credits = temp_total_credits + self.total_credits
                self.arg1 = self.init_course = self.temp = self.total_credits = 0
                print("\n")
            cgpa = round((temp_init + .0) / (temp_total_credits + .0), 2)
            output_this = """
            You have registered for total credits: {} and you have acquired CGPA: {}
            """.format(temp_total_credits, cgpa)
            print(output_this)
        else:
            print("You have not entered the scale correctly. Please try again.")
        pass


if __name__ == '__main__':
    init = GPA()
    init.cgpa()
