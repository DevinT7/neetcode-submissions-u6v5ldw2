class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def find_left():
            left = 0
            right = len(nums) - 1
            result = -1
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    result = mid
                    right = mid - 1
                if nums[mid] < target:
                    left = mid + 1
                if nums[mid] > target:
                    right = mid - 1
            return result
        def find_right():
            left = 0
            right = len(nums) - 1
            result = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    result = mid
                    left = mid + 1
                if nums[mid] < target:
                    left = mid + 1
                if nums[mid] > target:
                    right = mid - 1
            return result
        return [find_left(), find_right()]