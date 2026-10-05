class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        # would use a hashmap to make sure that we can match 
        # characters that have the same characters as
        # another string
        for string in strs:
            key = "".join(sorted(string))
            hashmap[key].append(string)
        return list(hashmap.values())