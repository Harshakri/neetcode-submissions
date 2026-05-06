class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        copy = nums.copy()
        for i in range(len(copy)):
            temp = copy.pop(0)
            if temp in copy:
                return True
        return False