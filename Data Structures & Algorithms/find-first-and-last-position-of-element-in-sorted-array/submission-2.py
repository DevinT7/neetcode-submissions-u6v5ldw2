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

        first = -1
        last = -1

        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        
        return [first,last]
