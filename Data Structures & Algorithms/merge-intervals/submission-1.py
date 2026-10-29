class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        # Sort intervals based on starting time
        intervals.sort()

        # Merge intervals one by one
        res = []
        start, end = intervals[0]
        for interval in intervals:
            # Overlapping = merge!
            if interval[0] <= end:
                end = max(end, interval[1])
            # Non-overlapping
            else:
                res.append([start, end])
                start, end = interval
        res.append([start, end])
        
        return res