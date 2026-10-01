class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # for an example, if i is 0, then it would do 2 * 4 which
        # is 8, then 8 * 6, which is 48
        # continues throughout the length of the array
        # one pointer that always starts at the start of the array,
        # and if that pointer is equal to i, then move it forward
        # if its not equal to i, keep that number, and multiply it to the sum
        # o(n) without using //
        # get the product of everything before and after i
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res