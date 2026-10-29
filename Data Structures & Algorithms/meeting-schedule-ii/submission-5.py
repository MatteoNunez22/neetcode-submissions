"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Store starts and ends in arrays
        starts, ends = [], []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)

        # Sorts the arrays
        starts.sort()
        ends.sort()

        # Travers both arrays with 2 points
        s, e, count, maxCount = 0, 0, 0, 0
        while s < len(starts):
            # Smallest number chosen
            start = starts[s]
            end = ends[e]

            # If start chosen, increment
            if start < end:
                count += 1
                s += 1
            # If end chosen, decrement
            elif end < start:
                count -= 1
                e += 1
            # If start == end, move pointers
            else:
                s += 1
                e += 1
            # Keep track of count
            maxCount = max(maxCount, count)

        # Return maximun count
        return maxCount