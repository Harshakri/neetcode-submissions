class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        tmp = 0
        final = 0
        for num in nums:
            if num == 1:
                tmp += 1
            else:
                final = max(final, tmp)
                tmp = 0
        return max(final, tmp)      