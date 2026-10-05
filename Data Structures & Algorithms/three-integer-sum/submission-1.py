class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # found = set()
        # n = len(nums)

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         for k in range(j + 1, n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 found.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        # return [list(t) for t in found]

        nums.sort()
        result = []
        n = len(nums)

        for i in range(n-2):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = n-1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return result