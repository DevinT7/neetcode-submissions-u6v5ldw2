class Solution {
    public String mergeAlternately(String word1, String word2) {
        String combined = "";
        int indexOfA = 0;
        int indexOfB = 0;
        if (word1.length() == word2.length()){
            for (int i = 0; i < word1.length(); i++){
                combined += word1.charAt(i);
                combined += word2.charAt(i);
            }
        }
        else if (word1.length() > word2.length()){
            for (int i = 0; i < word2.length(); i++){
                combined += word1.charAt(i);
                combined += word2.charAt(i);
                indexOfA++;
            }
            for (int j = indexOfA; j < word1.length(); j++){
                combined += word1.charAt(j);
            }
        }
        else{
            for (int i = 0; i < word1.length(); i++){
                combined += word1.charAt(i);
                combined += word2.charAt(i);
                indexOfB++;
            }
            for (int j = indexOfB; j < word2.length(); j++){
                combined += word2.charAt(j);
            }
        }
        return combined;
    }
}