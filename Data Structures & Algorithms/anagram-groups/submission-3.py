class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        # would use a hashmap to make sure that we can match 
        # characters that have the same characters as
        # another string
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')]+=1
            hashmap[tuple(count)].append(string)
        return list(hashmap.values())