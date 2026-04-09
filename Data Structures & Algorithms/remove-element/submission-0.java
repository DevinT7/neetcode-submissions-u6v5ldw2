class Solution {
    public int removeElement(int[] nums, int val) {
        int n = nums.length;
        int count = 0;
        for (int i = 0; i < n;){
            if (nums[i] != val){
                i++;
            }
            else if(nums[i] == val){
                nums[i] = nums[n-1];
                n--;
            }
        }
        return n;
    }
}