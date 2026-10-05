class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # so we're looking through the array
        # and finding the k most frequent elements
        # ex k is 2, so the 2 most frequent elements
        # would be 2 and 3 in ex 1

        # are we assuming the list is sorted or unsorted?
        # can k be larger than the number of values in the array?
        # would probably start thinking of using a hashmap
        # to keep track of how many times a number has come up
        # would then go through the hashmap and see
        # what k values are the highest
        # and then it would be that corresponding number 
        # returned in the array

        # going through every element would be o(nlogn), but we could
        # use the bucket sorting algorithm to make 
        # n buckets and groups numbers
        # based on frequencies from 1 to n
        # after that, we pick the top k numbers
        # from the buckets, starting from n 
        # all the way to 1

        #example: [1,1,1,2,2,100]

        # so bucket 1 would have a 100, since 100 only happens once
        # bucket 2 would have 2, since 2 happens twice
        # bucket 3 would have 1, since 1 happens 3 times
        # we stop at n because the most times a value could occur
        # is the length of the array/n times

        count = {}
        freq = []
        for i in range(len(nums) + 1):
            freq.append([])
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result




