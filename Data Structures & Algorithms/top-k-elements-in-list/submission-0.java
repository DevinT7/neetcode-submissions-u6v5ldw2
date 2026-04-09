class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Step 1: Count frequencies
        int[] freq = new int[2001];
        for (int num : nums) {
            freq[num + 1000]++;
        }

        // Step 2: Create and initialize buckets
        List<Integer>[] buckets = new List[nums.length + 1];
        for (int i = 0; i <= nums.length; i++) {
            buckets[i] = new ArrayList<>();
        }

        // Step 3: Fill buckets
        for (int i = 0; i < freq.length; i++) {
            if (freq[i] > 0) {
                buckets[freq[i]].add(i - 1000);
            }
        }

        // Step 4: Read from end, collect k elements
        int[] result = new int[k];
        int idx = 0;
        for (int i = nums.length; i >= 0 && idx < k; i--) {
            for (int num : buckets[i]) {
                result[idx++] = num;
                if (idx == k) break;
            }
        }

        return result;
    }
}