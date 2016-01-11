# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return intervals
        sortedIntervals = sorted(intervals, key=lambda x: x.start)
        mergedIntervals = [sortedIntervals[0]]
        i = 1
        while i < len(sortedIntervals):
            if (sortedIntervals[i].start <= mergedIntervals[-1].end):
                if (sortedIntervals[i].end >= mergedIntervals[-1].end):
                    mergedIntervals[-1] = Interval(mergedIntervals[-1].start, sortedIntervals[i].end)
            else:
                mergedIntervals.append(sortedIntervals[i])
            i += 1
            
        return mergedIntervals
