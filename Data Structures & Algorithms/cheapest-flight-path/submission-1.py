class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Make initial prices array
        prices = [float("inf")] * n
        prices[src] = 0
        # Iterate edges k times
        for i in range(k + 1):
            # Copy prices array
            tmp_prices = prices.copy()
            # Iterate edges
            for s, d, p in flights:
                # If source price is inf, ignore
                if prices[s] == float("inf"):
                    continue
                # Check if each edge make price better
                if (prices[s] + p) < tmp_prices[d]:
                    tmp_prices[d] = prices[s] + p
            prices = tmp_prices

        # return prices value for destination
        return -1 if prices[dst] == float("inf") else prices[dst]