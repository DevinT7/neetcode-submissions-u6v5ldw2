class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder clean = new StringBuilder();
        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if (Character.isLetterOrDigit(c)){
                clean.append(Character.toLowerCase(c));
            }
        }
        String t = clean.toString();
        int i = 0; 
        int j = t.length() - 1;
        while (i < j){
            if (t.charAt(i) != t.charAt(j)){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}
