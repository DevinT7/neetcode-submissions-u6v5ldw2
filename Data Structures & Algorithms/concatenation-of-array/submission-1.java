class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] ans = new int[nums.length*2];
        for (int j = 0; j < nums.length; j++){
            ans[j] = nums[j];
        }
        int index = ans.length/2;
        for (int j = 0; j < nums.length; j++){
            ans[index] = nums[j];
            index++;
        }
        // for (int i = 0; i < 2;){
        //     for (int j = 0; j < nums.length; j++){
        //         ans[j] = nums[j];
        //         index++;
        //     }
        //     i++;
        // }
        return ans;
    }
}