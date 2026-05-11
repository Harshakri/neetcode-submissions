import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        vals = {}
        heap = []

        for num in nums:
            vals[num] = 1 + vals.get(num, 0)
        
        for key, val in vals.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))

        return [h[1] for h in heap]
               
        
        
