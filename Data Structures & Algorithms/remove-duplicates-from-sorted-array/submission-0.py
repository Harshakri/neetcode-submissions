class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dups = []
        for num in nums[:]:
            if num in dups:
                nums.remove(num)
                continue
            else:
                dups.append(num)
        k = len(dups)
        return k