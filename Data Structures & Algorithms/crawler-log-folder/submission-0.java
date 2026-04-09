class Solution {
    public int minOperations(String[] logs) {
        int depth = 0;

        for (String log : logs) {
            if (log.equals("../")) {
                // Go to parent, but don't go below main folder (0)
                if (depth > 0) {
                    depth--;
                }
            } else if (!log.equals("./")) {
                // It's a "x/" move, so go deeper
                depth++;
            }
            // If it's "./", we do nothing, so no need for an extra else
        }

        return depth;
    }
}