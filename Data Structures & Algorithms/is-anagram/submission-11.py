class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
            sCount, tCount = {}, {}
            if len(s) != len(t):
                return False
            for i in range(len(s)):
                sCount[s[i]] = 1 + sCount.get(s[i], 0)
            #     tCount[t[i]] = 1 + tCount.get(t[i], 0)

            #     for c in sCount:
            #         if sCount[c] != tCount.get(c, 0):
            #             return False
            # return True
            for ch in s:
        """

        if len(s) != len(t):
            return False
        
        freq = {}
        for ch in s:
            freq[ch] = 1 + freq.get(ch, 0)

        for ch in t:
            if ch not in freq or freq[ch] == 0:
                return False
            else:
                freq[ch] -= 1
        return True


             

        