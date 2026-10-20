class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = {}
        
        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i], 0)
        
        for c in t:
            if counts.get(c,0) == 0:
                return False
            else:
                counts[c] -= 1
        
        return True
