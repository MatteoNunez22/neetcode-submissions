class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for source, target, weight in times:
            edges[source].append((target, weight))

        visited = set()
        time = 0
        minHeap = [(0, k)]

        while minHeap:
            cur_weight, cur_node = heapq.heappop(minHeap)
            if cur_node in visited:
                continue
            visited.add(cur_node)
            time = cur_weight

            for neighbor_node, neighbor_weight in edges[cur_node]:
                if neighbor_node not in visited:
                    heapq.heappush(minHeap, (neighbor_weight + cur_weight, neighbor_node))
        
        return time if len(visited) == n else -1