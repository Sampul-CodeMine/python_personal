import os as op_sys


class StudentClass:
    course_details_build_up = []

    def __init__(self):
        pass

    def accept_alias(self):
        op_sys.system('cls')
        prompt = "Enter Your Key (Confidential and Kept for references): "
        alias = input(prompt).lower()
        return alias

    def accept_name(self):
        op_sys.system('cls')
        prompt = "Enter Student Name: "
        name = input(prompt).upper()
        return name

    def check_result(self, val):
        result_out = {}
        if 70 <= val <= 100:
            result_out['Score'] = 'A'
            result_out['CourseGrade'] = 4.0
            result_out['Remark'] = 'Excellent'
        elif 60 <= val <= 69:
            result_out['Score'] = 'B'
            result_out['CourseGrade'] = 3.5
            result_out['Remark'] = 'Very Good'
        elif 50 <= val <= 59:
            result_out['Score'] = 'BC'
            result_out['CourseGrade'] = 3.0
            result_out['Remark'] = 'Good'
        elif 40 <= val <= 49:
            result_out['Score'] = 'C'
            result_out['CourseGrade'] = 2.5
            result_out['Remark'] = 'Credit'
        elif 30 <= val <= 39:
            result_out['Score'] = 'D'
            result_out['CourseGrade'] = 2.0
            result_out['Remark'] = 'Pass'
        elif 25 <= val <= 29:
            result_out['Score'] = 'E'
            result_out['CourseGrade'] = 1.5
            result_out['Remark'] = 'Poor'
        elif val == 0 and val <= 24:
            result_out['Score'] = 'F'
            result_out['CourseGrade'] = 1.0
            result_out['Remark'] = 'Fail'
        return result_out

    def accept_course_details(self):
        op_sys.system('cls')
        total_course_unit = 0  # TCU is the total Course Unit
        total_value_point = 0  # TVP is the total value point for all the courses
        course_build_up = {}
        result_build = {}
        gpa_result = {}
        count = 1
        print("==== Enter Courses ==== Enter Q to [Q]uit ====")
        while True:
            details_build = {}
            course_title = input("\nCourse Title: ")
            if not course_title == 'Q':
                details_build['Title'] = course_title.upper()
                details = ["Units", "Test", "Exam"]
                prompt = "Course {}: ".format(details[0])
                while True:
                    try:
                        resp = int(input(prompt))
                        if resp >= 1 and resp != 0:
                            if resp <= 10:
                                unit_result = resp
                                total_course_unit += unit_result
                                details_build[details[0]] = unit_result
                                break
                            else:
                                print('Course unit cannot be more than 10.')
                                continue
                        else:
                            print('Invalid Input')
                            continue
                    except ValueError:
                        print('Numeric data needed.')
                        continue
                    break

                prompt = "Course {}: ".format(details[1])
                while True:
                    try:
                        resp = int(input(prompt))
                        if resp > 1 and resp != 0:
                            if resp <= 30:
                                test_result = resp
                                details_build[details[1]] = test_result
                                break
                            else:
                                print('Test score cannot be more than 30 marks.')
                                continue
                        else:
                            print('Invalid Input')
                            continue

                    except ValueError:
                        print('Numeric data needed.')
                        continue
                    break

                prompt = "Course {}: ".format(details[2])
                while True:
                    try:
                        resp = int(input(prompt))
                        if resp > 1 and resp != 0:
                            if resp <= 70:
                                exam_result = resp
                                details_build[details[2]] = exam_result
                                break
                            else:
                                print('Exam score cannot be more than 70 marks.')
                                continue
                        else:
                            print('Invalid Input')
                            continue

                    except ValueError:
                        print('Numeric data needed.')
                        continue
                    break
                course_sum = test_result + exam_result
                details_build['Total'] = course_sum

                course_checker = self.check_result(course_sum)
                total_value_point += float(course_checker['CourseGrade']) * float(unit_result)

                details_build['Result'] = self.check_result(course_sum)
                course_build_up['Course{}'.format(count)] = details_build
            else:
                break
            count += 1
        tcu = total_course_unit
        tvp = total_value_point
        gpa = tvp / tcu

        result_build['TCU'] = tcu
        result_build['TVP'] = tvp
        result_build['GPA'] = round(gpa, 2)
        gpa_result['FINAL'] = result_build

        self.course_details_build_up.append(course_build_up)
        self.course_details_build_up.append(gpa_result)

        return self.course_details_build_up


if __name__ == '__main__':
    student = StudentClass()

    stud_info = {}
    stud_name = {}
    stud_course_info = {}
    stud_build_up = []

    student_alias_key = student.accept_alias()
    student_fullname = student.accept_name()
    student_courses = student.accept_course_details()

    stud_name['Name'] = student_fullname
    stud_build_up.append(stud_name)

    stud_course_info['CourseDetails'] = student_courses
    stud_build_up.append(stud_course_info)

    stud_info[student_alias_key] = stud_build_up

    op_sys.system('cls')
    print('\n ============ STUDENTS INFORMATION ============')
    """get information about the student"""
    get_key = input("Enter Student's Key: ").lower()
    if get_key not in stud_info:
        print('Invalid Student Key provided.')
        exit(0)
    op_sys.system('cls')
    print("Details of the student for this semester:\n{}".format(stud_info[get_key]))







print('\n\nThank you for visiting.....')
exit(0)