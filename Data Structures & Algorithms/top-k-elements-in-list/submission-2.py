from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        min_heap = []
        for key in freq.keys():
            heapq.heappush(min_heap, (freq[key], key))
            if len(min_heap)> k:
                heapq.heappop(min_heap)

        res = []
        for i in range(k):
            
            res.append(heapq.heappop(min_heap)[1])
        return res