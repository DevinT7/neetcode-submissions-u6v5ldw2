class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int fixed = 0;
        for (int i = 0; i < nums.length; i++){
            if (nums[i] % 2 == 0){
                int temp = nums[fixed];
                nums[fixed] = nums[i];
                nums[i] = temp;
                fixed++;
            }
        }
        return nums;
    }
}