class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}

        for word in strs:
            tmp = "".join(sorted(word))
            if tmp in data:
                data[tmp].append(word)
            else:
                data[tmp] = [word]
        res = list(data.values())

        return res