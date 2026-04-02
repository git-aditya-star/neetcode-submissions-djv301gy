class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cum_list = [0]*len(nums)
        rev_cum_list = [0]*len(nums)
        cum_val = 1
        for idx, num in enumerate(nums):
            cum_val *= num
            cum_list[idx] = cum_val
        cum_val = 1
        for idx in range(len(nums)-1, -1, -1):
            cum_val *= nums[idx]
            rev_cum_list[idx] = cum_val
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(rev_cum_list[i+1])
            elif i == len(nums)-1:
                res.append(cum_list[i-1])
            else:
                res.append(cum_list[i-1]* rev_cum_list[i+1])
        return res