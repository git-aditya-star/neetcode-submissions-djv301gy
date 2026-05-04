class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if nums[0] < nums [-1]:
            return nums[0]
        
        if nums[-1] < nums[-2]:
            return nums[-1]

        
        l =0
        r =len(nums)-1

        mini = nums[0]
        
            

        while l  <= r:
            if nums[l] < nums[r]:
                mini = min(mini, nums[l])
                break
            
            m = (l+r) // 2
            mini = min(mini, nums[m])

            if nums[m] >= nums[l]:
                l = m +1
            else:
                r = m -1
        return mini

