class Solution {
    public boolean isSubsequence(String s, String t) {
        boolean contain = false;
        int j = 0;
        for (int i = 0; i < t.length(); i++){
            if (j < s.length() && t.charAt(i) == s.charAt(j)){
                j++;
                //contain = true;
                }
            }
        
        return j == s.length();
    }
}