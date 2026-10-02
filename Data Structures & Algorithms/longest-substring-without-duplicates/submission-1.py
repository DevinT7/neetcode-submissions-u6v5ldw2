class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        # if len(s) <= 1:
        #     return 1
        
        right = 0
        left = 0
        maximum = 0
        for right in range(len(s)):
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1
            hashset.add(s[right])
            window_size = right - left + 1
            if window_size > maximum:
                maximum = window_size
        return maximum
