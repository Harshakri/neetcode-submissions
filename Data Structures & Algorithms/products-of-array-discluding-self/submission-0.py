class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        
        for i in range(len(nums)):
            left = 1
            right = 1
            for x in nums[:i]:
                left *= x
            for y in nums[i+1:]:
                right *= y
            res.append((left*right))
        return res
            
            