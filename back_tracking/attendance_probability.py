# ## Question
#
# In a university, your attendance determines whether you will be
# allowed to attend your graduation ceremony.
# You are not allowed to miss classes for four or more consecutive days.
# Your graduation ceremony is on the last day of the academic year,
# which is the Nth day.
#
# Your task is to determine the following:
#
# 1. The number of ways to attend classes over N days.
# 2. The probability that you will miss your graduation ceremony.
#
# Represent the solution in the string format as "Answer of (2) / Answer
# of (1)", don't actually divide or reduce the fraction to decimal
#
# Test cases:
#
# for 5 days: 14/29
#
# for 10 days: 372/773

class Solve:
    def __init__(self, days):
        self.arr = []
        self.days = days

    def list_of_way(self):
        arr = []
        self.find(self.days, "", arr)
        return arr

    def find(self, days, attendance_pattern, arr):
        if days == 0:
            arr.append(attendance_pattern)
        else:
            # At any given day there are only two possibalities
            self.find(days - 1, attendance_pattern + 'A', arr)  # absent in class
            self.find(days - 1, attendance_pattern + 'P', arr)  # present in class

# obj = Solve(6)
# way = obj.list_of_way()
# print(way)
# print(len(way))
# total_missing_way = len(list(filter(lambda x: 'AAAA' in x, way)))
# total_attend_way = len(way) - total_missing_way
# print( total_missing_way, total_attend_way)


# find max possible way to attend the ceromonie
# AAAAA nCr 5!/

"""
1 -> 2
2 -> 4
3 -> 8
4 -> 16 1
5 -> 32 3
6 -> 64, 8
7 -> 128, 20

day = 5
 AAAAA PPPPP
if day==1:
    return 2
else
  call function + n
   
"""

def num_of_way(day):
    if day == 4:
        return 16
    return num_of_way(day-1) + num_of_way(day-2) + num_of_way(day-3)

print(num_of_way(10))







