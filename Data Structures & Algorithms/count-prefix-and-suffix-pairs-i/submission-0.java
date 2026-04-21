class Solution {
    public int countPrefixSuffixPairs(String[] words) {
        int count = 0;
        
        // Iterate through the array with a nested loop to find pairs (i, j)
        for (int i = 0; i < words.length; i++) {
            // Start j at i + 1 to ensure the condition i < j is always met
            for (int j = i + 1; j < words.length; j++) {
                if (isPrefixAndSuffix(words[i], words[j])) {
                    count++;
                }
            }
        }
        
        return count;
    }

    private boolean isPrefixAndSuffix(String str1, String str2) {
        // str1 must be at the very beginning AND the very end of str2
        return str2.startsWith(str1) && str2.endsWith(str1);
    }
}