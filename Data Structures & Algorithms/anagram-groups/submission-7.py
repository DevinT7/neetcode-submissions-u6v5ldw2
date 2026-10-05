class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # used = [False] * len(strs)
        # result = []

        # for i in range(len(strs)):
        #     if used[i]:
        #         continue
        #     group = [strs[i]]
        #     used[i] = True

        #     for j in range(i + 1, len(strs)):
        #         if not used[j] and sorted(strs[i]) == sorted(strs[j]):
        #             group.append(strs[j])
        #             used[j] = True
        #     result.append(group)
        # return result

        groups = defaultdict(list)
        for words in strs:
            key = "".join(sorted(words))
            groups[key].append(words)
        return list(groups.values())

        