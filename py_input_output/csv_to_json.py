#!/usr/bin/python3

import csv
import json

with open("persons.csv", mode="r") as fn:
    data = csv.reader(fn)
    next(data)
    dst = []
    for r in data:
        lst ={}
        lst["firstname"] = r[0]
        lst["lastname"] = r[1]
        lst["age"] = r[2]
        dst.append(lst)
        

with open("new_persons.json", mode="w") as fn:
    json.dump(dst, fn, indent=2, sort_keys=True)
