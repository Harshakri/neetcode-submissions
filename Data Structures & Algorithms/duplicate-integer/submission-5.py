class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        oglen = len(nums)
        nums = set(nums)
        adjlen = len(nums)
        print(oglen, adjlen)
        if oglen == adjlen:
            return False
        return True
