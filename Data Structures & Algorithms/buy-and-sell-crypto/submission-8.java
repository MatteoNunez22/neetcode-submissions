class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int r = l;
        int maxProfit = 0;

        while (r < prices.length) {
            if (prices[r] > prices[l]) {
                maxProfit = Math.max(prices[r] - prices[l], maxProfit);
            } else {
                l = r;
            }
            r++;
        }

        return maxProfit;
    }
}
