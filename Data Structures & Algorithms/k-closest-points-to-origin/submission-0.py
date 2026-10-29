class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(x, y):
            return math.sqrt(x**2 + y**2)
        
        # Insert all points (d, x, y) to a minHeap
        q = []
        for point in points:
            x, y = point
            heapq.heappush(q, (distance(x, y), x, y))

        # Pop the heap k times
        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(q)
            res.append([x, y])

        # Return the popped array
        return res