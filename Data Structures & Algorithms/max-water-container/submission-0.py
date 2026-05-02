class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights)-1

        max_water = -1
        while left < right:
            min_height = min(heights[left] , heights[right])
            vol = min_height * (right - left)
            if vol > max_water:
                max_water = vol
            
            if heights[left] == min_height:
                left+=1
            else: 
                right-=1

        return max_water

            
