class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sett = set()
        already_marked = set()
        for num in nums:
            sett.add(num)
        max=1

        count_dict = {}
        for num in sett:
            curr = num
            curr_max = 1
            if curr in already_marked:
                continue
            while curr +1 in sett:
                next = curr+1
                if next in count_dict:
                    curr_max += count_dict[next] 
                    if curr_max > max:
                        max = curr_max
               
                    already_marked.add(curr)
                    break
                    
                else :
                    curr_max+=1
                    curr+=1

                if curr_max > max:
                    max = curr_max
               
                already_marked.add(curr)
            count_dict[num] = curr_max
        return max
