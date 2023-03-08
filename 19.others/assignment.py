import os as op_sys


def open_locks(stud_no, lock_no):
    keys = [1 for i in range(lock_no)]
    for j in range(2, stud_no+1):
        keys = [-1*keys[i] if (i+1)%j == 0 else keys[i] for i in range(len(keys))]
    return keys.count(1)


def most_touchable_lockers(no_of_students, no_of_lockers):
    keys = [1 for i in range(no_of_lockers)]
    for j in range(2, no_of_students + 1):
        keys = [1+keys[i] if (i+1)%j == 0 else keys[i] for i in range(len(keys))]
    ms = max(keys)
    return keys.index(ms) + 1


the_open_lockers = open_locks(50, 50)
the_most_opened = most_touchable_lockers(50, 50)
the_open_lockers2 = open_locks(100, 100)
the_most_opened2 = most_touchable_lockers(100, 100)

op_sys.system('cls')
print('==== FOR 50 STUDENTS AND 50 LOCKERS ====\n')
print("Number of still opened lockers: {}".format(the_open_lockers))
print("Number of most opened lockers: {}".format(the_most_opened))

print('\n\n==== FOR 100 STUDENTS AND 100 LOCKERS ====\n')

print("Number of still opened lockers: {}".format(the_open_lockers2))
print("Number of most opened lockers: {}".format(the_most_opened2))
exit(0)
