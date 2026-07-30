class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int target = nums.length / 2;
        
        // 2. Iterate through the Array
        for (int num : nums) {
            // 3. Update the Count (using the getOrDefault trick)
            map.put(num, map.getOrDefault(num, 0) + 1);
            
            // 4. Check for the Winner
            if (map.get(num) > target) {
                return num;
            }
        }
        
        // The problem guarantees a majority element exists, 
        // but Java requires a return statement outside the loop just in case.
        return -1; 
    }
}