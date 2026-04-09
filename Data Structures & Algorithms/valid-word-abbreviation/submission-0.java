class Solution {
    public boolean validWordAbbreviation(String word, String abbr) {
        int i = 0, j = 0;
        
        while (i < word.length() && j < abbr.length()) {
            if (Character.isDigit(abbr.charAt(j))) {
                // No leading zeros
                if (abbr.charAt(j) == '0') return false;
                
                // Extract the full number
                int num = 0;
                while (j < abbr.length() && Character.isDigit(abbr.charAt(j))) {
                    num = num * 10 + Character.getNumericValue(abbr.charAt(j));
                    j++;
                }
                i += num; // skip 'num' chars in word
                
            } else {
                // Letters must match exactly
                if (word.charAt(i) != abbr.charAt(j)) return false;
                i++;
                j++;
            }
        }
        
        return i == word.length() && j == abbr.length();
    }
}