class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals based on starting time
        intervals.sort(key=lambda pair: pair[0])

        # Merge intervals one by one
        res = [intervals[0]]
        for start, end in intervals:
            lastEnd = res[-1][1]
            # Overlapping = merge!
            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end)
            # Non-overlapping
            else:
                res.append([start, end])
        
        return res