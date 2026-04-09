class Solution {
    public int scoreOfString(String s) {
        int sum = 0;
        for (int i = 0; i < s.length()-1; i++){
            char temp = s.charAt(i);
            char temp2 = s.charAt(i+1);
            sum += (int)(Math.abs(temp2-temp));
            //sum+= ascii;
        }
        return sum;
    }
}