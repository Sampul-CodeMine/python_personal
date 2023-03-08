import os as op_sys


def open_lockers(no_of_students, no_of_lockers):
    keys = []
    for i in range(no_of_lockers):
        keys.append(1)
        for j in range(2, no_of_students+1):
            if (i+1)%j == 0:
                keys[i] = -1 * keys[i]
            keys[i] = keys[i]
    return keys.count(1)


def most_touched_lockers(no_of_students, no_of_lockers):
    keys = []
    for i in range(no_of_lockers):
        keys.append(1)
        for j in range(2, no_of_students + 1):
            if (i + 1) % j == 0:
                keys[i] = 1 + keys[i]
            keys[i] = keys[i]

    maxim = max(keys)
    return keys.index(maxim) + 1


op_sys.system('cls')
print('==== FOR 50 STUDENTS AND 50 LOCKERS ====\n')
print("Number of still opened lockers: {}".format(open_lockers(50, 50)))
print("Number of most opened lockers: {}".format(most_touched_lockers(50, 50)))

print('\n\n==== FOR 100 STUDENTS AND 100 LOCKERS ====\n')

print("Number of still opened lockers: {}".format(open_lockers(100, 100)))
print("Number of most opened lockers: {}".format(most_touched_lockers(100, 100)))
exit(0)