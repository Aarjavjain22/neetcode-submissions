class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        i = 0
        j = len(height) - 1
        
        while i < j:
            current_area = min(height[i],height[j]) * (j - i)
            max_water = max(max_water, current_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1 
        return max_water