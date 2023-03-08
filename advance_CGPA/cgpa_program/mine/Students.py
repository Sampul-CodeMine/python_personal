import os as op_sys


def accept_alias():
    op_sys.system('cls')
    prompt = "Enter Your Key (Confidential and Kept for references): "
    alias = input(prompt)
    return alias.lower()


def accept_name():
    op_sys.system('cls')
    prompt = "Enter Student Name: "
    name = input(prompt)
    return name.upper()


course_details_build_up = []


def accept_course_details():
    op_sys.system('cls')
    total_course_unit = 0  # TCU is the total Course Unit
    total_value_point = 0  # TVP is the total value point for all the courses
    course_build_up = {}
    result_build = {}
    gpa_result = {}
    each_build = []
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
                            unit_result = 0
                            continue
                    else:
                        print('Invalid Input')
                        unit_result = 0
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
                            test_result = 0
                            continue
                    else:
                        print('Invalid Input')
                        test_result = 0
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
                            exam_result = 0
                            continue
                    else:
                        print('Invalid Input')
                        exam_result = 0
                        continue

                except ValueError:
                    print('Numeric data needed.')
                    continue
                break

            course_sum = test_result + exam_result
            details_build['Total'] = course_sum

            course_checker = check_result(course_sum)
            total_value_point += float(course_checker['CourseGrade']) * float(unit_result)

            details_build['Result'] = check_result(course_sum)
            course_build_up['Course{}'.format(count)] = details_build
        else:
            break
        count += 1
    tcu = total_course_unit
    tvp = total_value_point
    gpa = tvp / tcu

    result_build['TCU'] = tcu
    result_build['TVP'] = tvp
    result_build['GPA'] = round(gpa,2)
    gpa_result['FINAL'] = result_build

    course_details_build_up.append(course_build_up)
    course_details_build_up.append(gpa_result)

    return course_details_build_up


def check_result(val):
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
