#!/usr/bin/python3

import csv
import json

with open("persons.json", mode="r") as fn:
    data = json.load(fn)

with open("persons.csv", mode="w", newline="") as fn:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(fn, fieldnames=fieldnames)
    writer.writeheader()
    for d in data:
        writer.writerow(d)
