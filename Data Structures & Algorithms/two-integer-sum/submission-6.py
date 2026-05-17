class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for index, num in enumerate(nums):
            req = target - num
            if req in hmap:
                return [hmap[req], index]
            hmap[num] = index
    