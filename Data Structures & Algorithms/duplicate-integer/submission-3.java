class Solution {
    public boolean hasDuplicate(int[] nums) {
       Arrays.sort(nums);
       boolean x = false;
       for (int i = 0; i < nums.length-1; i++){
        int temp = nums[i];
        if (temp == nums[i+1]){
            //temp = nums[i+1];
            x = true;
        }
       }
       return x; 
    }
}