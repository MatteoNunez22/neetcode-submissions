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
        i, j, count, maxCount = 0, 0, 0, 0
        while i < len(starts):
            # Smallest number chosen
            start = starts[i]
            end = ends[j]

            # If start chosen, increment
            if start < end:
                count += 1
                i += 1
            # If end chosen, decrement
            elif end < start:
                count -= 1
                j += 1
            # If start == end, move pointers
            else:
                i += 1
                j += 1
            # Keep track of count
            maxCount = max(maxCount, count)

        # Return maximun count
        return maxCount