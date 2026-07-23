class Solution {
    public int[] twoSum(int[] nums, int target) {
        int num = 0;
        int sum = 0;
        int curr[] = new int [2];
        for (int i = 0; i < nums.length; i++){
            for (int j = i+1; j < nums.length; j++){
                if (nums[i] + nums[j] == target && i != j){
                   curr[0] = i;
                   curr[1] = j;
                }
            }
        }
        return curr;
    }
}