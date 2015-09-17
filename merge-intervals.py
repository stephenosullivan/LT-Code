__author__ = 'stephenosullivan'

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
        intervals.sort(key=lambda interval: interval.start)
        output = []
        if intervals:
            prev_start = intervals[0].start
            prev_end = intervals[0].end
            for i in range(1, len(intervals)):
                start = intervals[i].start
                end = intervals[i].end

                # overlap
                if prev_end >= start:
                    if prev_end < end:
                        prev_end = end

                # no overlap, so save
                else:
                    output.append(Interval(prev_start, prev_end))
                    prev_start = start
                    prev_end = end

            output.append(Interval(prev_start, prev_end))

        return output
