from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        min_heap = []
        for key in freq.keys():
            if (len(min_heap) == k):
                heapq.heappushpop(min_heap, (freq[key], key))
            else:
                heapq.heappush(min_heap, (freq[key], key))
            
        res = []
        for i in range(len(min_heap)):
            
            res.append(heapq.heappop(min_heap)[1])
            # res.append(min_heap[i][1])
        return res