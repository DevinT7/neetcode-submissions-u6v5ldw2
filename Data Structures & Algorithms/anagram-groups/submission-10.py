class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:

            count = [0] * 26

            for c in word:
                # ascii values of a character 
                # a = 80 b = 81 c = 82
                # +- 1
                # c = b
                # 81 - 80 -> b
                # += 1 -> We've seen 1 b
                count[ord(c) - ord("a")] += 1
            groups[tuple(count)].append(word)
        return list(groups.values())



        