import time
import datetime
import argparse

time = datetime.datetime.now()
print("Current Date and Time: ", time.strftime("%Y-%m-%d %H:%M:%S"))
print("Current Date: ", time.strftime("%d/%m/%Y"))
print("Current Time: ", time.strftime("%I:%M:%S %p"))
print("Long Date: ", time.strftime("%a, %b %d, %Y"))

print("\n\n=============== T I M E R  A P P L I C A T I O N ==============\n\n")


def count_down_timer(x, now=datetime.datetime.now):
    target = now()
    one_sec_later = datetime.timedelta(seconds=1)
    for remaining in range(x, 0, -1):
        target += one_sec_later
        print(datetime.timedelta(seconds=remaining-1), 'remaining', end="\r")
        time.sleep((target - now()).total_se)