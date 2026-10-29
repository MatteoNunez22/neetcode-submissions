class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # Insert all points (d, x, y) to a minHeap
        minHeap = []
        for x, y in points:
            dist = x**2 + y**2
            minHeap.append([dist, x, y])
        heapq.heapify(minHeap)

        # Pop the heap k times
        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(minHeap)
            res.append([x, y])

        # Return the popped array
        return res