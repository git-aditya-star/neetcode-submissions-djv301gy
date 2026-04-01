class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for idx, num in enumerate(nums):
            subtracted = target - num
            if subtracted in dict:
                return [dict[subtracted], idx]
            if num not in dict:
                dict[num] = idx