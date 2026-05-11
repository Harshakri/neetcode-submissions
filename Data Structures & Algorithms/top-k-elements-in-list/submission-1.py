import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        vals = {}
        heap = []

        for num in nums:
            if num in vals:
                vals[num] += 1
            else:
                vals[num] = 1
        
        for key, val in vals.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))
        return [h[1] for h in heap]
               
        
        
