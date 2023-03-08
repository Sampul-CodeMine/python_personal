##list_range = int(input("Range: "))
##items = []
##for i in range(0, 12):
##    items.append(list_range * 2**i)
##
##print(items)
##print()
##print("Another Method\n")
##item_list = [list_range * 2**i for i in range(0, 12) ]
##print(item_list)
##
###Another work
##print()
##text = input("Enter Sentence: ")
##word_count = len(text.split())
##sentence_length = text.replace(" ", "")
##print(len(sentence_length) / word_count)
##
### another Work
##print()
##contacts = {"David":["123-456-789", "david@test.com"],"James":["123-789-456", "james@test.com"], "Bob":["789-098-123", "bob@test.com"], "Amy":["103-126-789", "amy@test.com"]}
##name = input("Enter Name: ")
##if name in contacts:
##    result = contacts.get(name)
##    print(result[1])
##else:
##    print("Not found")
### another Work
##print()
##import math
##points = [(12, 55), (880, 123), (64, 64), (190, 1024), (77,  33), (42, 11), (0, 90)]
##distance = [math.sqrt((x**2) + (y**2)) for (x,y) in points]
##
##print(min(distance))
##
##print()
##a, b, c, d, *e, f, g = range(20)
##print(len(e))

##string1 = input("First Sentence: ")
##string2 = input("Second Sentence: ")
##s1 = set(string1.split())
##s2 = set(string2.split())
##print("First Split : {}".format(s1))
##print("Second Split: {}".format(s2))
##
##
##print(len(s1 & s2))

data = {"100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54": 19, "097-32": 33, "065-135": 64, "99-043": 80, "111-99": 11, "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, "055-967": 35, "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59, "001-233": 9, "089-111": 15, "090-090": 17, "56-777": 23, "44-909": 27, "13-111": 21, "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, "87-436": 12, "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, "87-430": 40}
values = data.values()
normal_reading = 0
sampling_reading = 0

def calc(num):
    total = 0
    for i in values:
        if i >= num:
            total  += 20
        else:
            total += 5
    return total

sampling_age = int(input("Enter Age: "))
normal_reading = calc(18)
sampling_reading = calc(sampling_age)

difference = ((sampling_reading - normal_reading) / normal_reading ) * 100
print(int(difference))
