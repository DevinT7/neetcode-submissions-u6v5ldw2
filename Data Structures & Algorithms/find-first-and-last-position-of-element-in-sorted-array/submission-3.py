class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # walk through the array
        # once i find target, start tracking the index
        # in the form of a counter
        # save the index of when i first land on target 
        # temp = i
        # every time i keep seeing target
        # count += 1
        # once i land on value that's != target
        # return [temp, temp + count]

        # first = -1
        # last = -1

        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         if first == -1:
        #             first = i
        #         last = i
        
        # return [first,last]

        # binary search approach
        # [5, 7, 7, 8, 8, 10]
        def find_bound(is_first):
            bound = -1
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    bound = mid
                    if is_first:
                        right = mid - 1
                    else:
                        left = mid + 1
            return bound
        
        return [find_bound(True), find_bound(False)]

