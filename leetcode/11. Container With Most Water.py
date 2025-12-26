class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        max_area = (j - i) * min(height[i], height[j])
        while i < j:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            
            area = (j - i) * min(height[i], height[j])
            if area > max_area:
                max_area = area
        
        return max_area
