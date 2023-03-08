# imports the students file where all functions are defined
import Students as Student

student_info = {}  # dictionary to hold complete student's information
stud_name = {}  # dictionary to hold student's name
courses_info = {}  # dictionary to hold the courses and courses details
build_up = []  # list to build up the student_info dictionary

alias = Student.accept_alias()  # get the student's alias used to store students info in the dictionary
student_name = Student.accept_name()  # get the student's name
course_details = Student.accept_course_details()  # gets the student course information

stud_name['Name'] = student_name
build_up.append(stud_name)
courses_info['Course_Details'] = course_details
build_up.append(courses_info)
student_info[alias] = build_up

print("\n\n==============GET STUDENT'S DETAILS==================\n")
# Getting information from the Students Information Dictionary

get_key = input("Enter student's Key: ")
if get_key not in student_info:
    print("Invalid student key")
else:
    Student.op_sys.system('cls')
    print("\n\n==============STUDENT'S RESULT==================\n")
    print(student_info[get_key])
    first_part = student_info[get_key]
    name_info = first_part[0]
    print("\nStudent's Name: {}".format(name_info['Name']))
    course_info = first_part[1]
    print("Student's Course Details:\n")
    course = course_info['Course_Details']

    # give_course = c['Course'+str(val + 1)]
    # print(give_course)
    # print("Course Title: {}".format(give_course['Title']))
    # print("Course Unit: {}".format(give_course['Units']))
    # print("Course Test: {}".format(give_course['Test']))
    # print("Course Exam: {}".format(give_course['Exam']))
    # print("Course Total: {}".format(give_course['Total']))
    # result = give_course['Result']
    # print("Course Value: {}".format(result['CourseGrade']))
    # print("Course Grade: {}".format(result['Score']))
    # print("Course Remark: {}".format(result['Remark']))
    # print()
    #

