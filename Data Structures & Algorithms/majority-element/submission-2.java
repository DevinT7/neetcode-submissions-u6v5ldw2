class Solution {
    public int majorityElement(int[] nums) {
        int max = 0;
        int highest = 0;
        for (int i = 0; i < nums.length; i++){
            int count = 0;
            for (int j = 0; j < nums.length; j++){
                if (nums[i] == nums[j]){
                    count++;
                }
            }
            if (count > max){
                max = count;
                highest = nums[i];
            }
        }
        return highest;
    }
}