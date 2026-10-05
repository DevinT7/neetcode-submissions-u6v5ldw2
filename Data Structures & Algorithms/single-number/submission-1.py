class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # hashmap = {}
        # for num in nums:
        #     if num in hashmap:
        #         hashmap[num] += 1
        #     else:
        #         hashmap[num] = 1
        # for key, val in hashmap.items():
        #     if val == 1:
        #         return key
        res = 0
        for n in nums:
            res = res ^ n
        return res
        