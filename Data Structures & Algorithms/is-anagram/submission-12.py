class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

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


             

        