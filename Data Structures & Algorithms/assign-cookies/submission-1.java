class Solution {
    public int findContentChildren(int[] g, int[] s) {
        // Step 1: Sort both arrays
        Arrays.sort(g);
        Arrays.sort(s);
        
        int childPtr = 0;
        int cookiePtr = 0;
        
        // Step 2: Iterate through cookies and children
        while (childPtr < g.length && cookiePtr < s.length) {
            // If the current cookie can satisfy the current child
            if (s[cookiePtr] >= g[childPtr]) {
                childPtr++; // Move to the next child
            }
            // Always move to the next cookie
            cookiePtr++;
        }
        
        // The number of content children is the index reached in the greed array
        return childPtr;
    }
}