from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sorted_tuples = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_tuples[i][0])
        return result