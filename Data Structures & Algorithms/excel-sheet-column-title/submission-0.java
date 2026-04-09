class Solution {
    public String convertToTitle(int columnNumber) {
        StringBuilder result = new StringBuilder();
        
        while (columnNumber > 0) {
            // Step 1: Shift to 0-indexed
            columnNumber--;
            
            // Step 2: Get the character (0 -> 'A', 25 -> 'Z')
            char currentChar = (char) ('A' + (columnNumber % 26));
            result.append(currentChar);
            
            // Step 3: Move to the next "digit"
            columnNumber /= 26;
        }
        
        // The characters were added from right to left, so reverse them
        return result.reverse().toString();
    }
}