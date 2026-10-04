class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        max_length = 0
        for num in nums:
            length = 1
            if (num-1) not in hashset:
                while (num + length) in hashset:
                    length += 1
            if max_length < length:
                max_length = length
        return max_length
