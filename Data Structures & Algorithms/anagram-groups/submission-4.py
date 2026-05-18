class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}

        for word in strs:
            ordered = "".join(sorted(word))
            if ordered in data:
                data[ordered].append(word)
            else:
                data[ordered] = [word]
        res = list(data.values())

        return res
         