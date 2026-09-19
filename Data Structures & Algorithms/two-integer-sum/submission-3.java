class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> dict = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int diff = target - num;

            if (dict.containsKey(diff)) {
                int[] array = { dict.get(diff), i };
                return array;
            }

            dict.put(num, i);
        }

        return new int[] {};
    }
}
