class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sett = set()
        already_marked = set()
        for num in nums:
            sett.add(num)
        max=1
        for num in sett:
            curr = num
            curr_max = 1
            if curr in already_marked:
                continue
            while curr +1 in sett:
                
                curr_max+=1
                
                if curr_max > max:
                    max = curr_max
                curr+=1
                already_marked.add(curr)
        return max
