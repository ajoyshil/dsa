"""
Given an array of intervals intervals where intervals[i] = [starti, endi],
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
"""
from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    end, count = float('-inf'), 0

    for s, e, in sorted(intervals, key = lambda x: x[1]):
        if s >= end:
            end = e
        else:
            count += 1
    return count


arr = [[1,2],[2,3],[3,4],[1,3],[1,4],[3,6]]
tem = eraseOverlapIntervals(arr)
print(tem)
