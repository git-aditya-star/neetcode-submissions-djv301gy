from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = []
        count_nums = [[] for n in range(len(nums)+1)]
        for key, value in freq.items():
            count_nums[value].append(key)

        for i in range(len(count_nums)-1, 0, -1):
            for j in count_nums[i]:
                res.append(j)
                if len(res) == k:
                    return res

        return res