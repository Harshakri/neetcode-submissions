class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ordered = []
        data = {}

        for word in strs:
            tmp = "".join(sorted(word))
            ordered.append(tmp)
            data[tmp] = []
        
        for index, key in enumerate(ordered):
            data[key].append(strs[index])
        
        return list(data.values())