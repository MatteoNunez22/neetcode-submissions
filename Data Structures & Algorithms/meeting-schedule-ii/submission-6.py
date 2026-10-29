"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Store starts and ends in arrays and sort them
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        # Traverse both arrays with 2 points
        count = res = 0
        s = e = 0
        while s < len(start):
            # If start chosen, increment
            if start[s] < end[e]:
                s += 1
                count += 1
            # If end chosen, decrement
            elif end[e] < start[s]:
                e += 1
                count -= 1
            # If start == end, move pointers
            else:
                s += 1
                e += 1
            # Keep track of count
            res = max(res, count)

        # Return maximun count
        return res