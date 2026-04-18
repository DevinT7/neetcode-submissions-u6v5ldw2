class Solution {
    public int minimumRecolors(String blocks, int k) {
        int n = blocks.length();
        int currentWhites = 0;

        // 1. Calculate white blocks in the first window of size k
        for (int i = 0; i < k; i++) {
            if (blocks.charAt(i) == 'W') {
                currentWhites++;
            }
        }

        // Initialize minOps with the first window's white count
        int minOps = currentWhites;

        // 2. Slide the window across the rest of the string
        for (int i = k; i < n; i++) {
            // Add the incoming character
            if (blocks.charAt(i) == 'W') {
                currentWhites++;
            }
            // Remove the outgoing character (at index i - k)
            if (blocks.charAt(i - k) == 'W') {
                currentWhites--;
            }

            // Update minimum operations found so far
            minOps = Math.min(minOps, currentWhites);
        }

        return minOps;
    }
}