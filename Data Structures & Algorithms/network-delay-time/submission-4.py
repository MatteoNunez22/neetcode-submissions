class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build edges dict
        edges = {}
        for u, v, w in times:
            if u not in edges:
                edges[u] = []
            edges[u].append((v, w))

        # Start heap with node k and weight 0
        minHeap = [(0, k)]
        visit = set()
        t = 0

        # Dijkstra algorithm
        while minHeap:
            # Pop lowest weight in minHeap 
            w1, n1 = heapq.heappop(minHeap)
            # Add this to visit set
            if n1 not in visit:
                visit.add(n1)
                # Keep count of time t
                t = w1
                # For each popped, add its edges to minHeap
                if n1 in edges:
                    for n2, w2 in edges[n1]:
                        if n2 not in visit:
                            heapq.heappush(minHeap, (w2 + w1, n2))

        # If visit length == n, return t. Otherwise, return -1
        return t if len(visit) == n else -1