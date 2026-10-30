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
            weight, node = heapq.heappop(minHeap)
            # Add this to visit set
            if node not in visit:
                visit.add(node)
                # Keep count of time t
                t = weight
                # For each popped, add its edges to minHeap
                if node in edges:
                    for v, w in edges[node]:
                        if v not in visit:
                            heapq.heappush(minHeap, (w + weight, v))

        # If visit length == n, return t. Otherwise, return -1
        return t if len(visit) == n else -1