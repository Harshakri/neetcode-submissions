class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_of_anagrams = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord("a")] += 1

            curr_key = tuple(count)
            group_of_anagrams[curr_key].append(word)

        output = list()
        for key, value in group_of_anagrams.items():
            output.append(value)

        return output