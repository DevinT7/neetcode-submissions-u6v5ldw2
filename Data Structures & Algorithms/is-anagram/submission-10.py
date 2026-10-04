class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # return sorted(s) == sorted(t)

        # countS = {}
        # countT = {}
        
        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # for c in countS:
        #     if countS[c] != countT.get(c, 0):
        #         return False
        # return True

        counts = {}

        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i], 0)
        
        for c in t:
            if counts.get(c,0) == 0:
                return False
            else:
                counts[c] -= 1
        return True

        # s = sorted(s)
        # t = sorted(t)
        # for i in range(len(s)):
        #     if s[i] != t[i]:
        #         return False
        # return True
