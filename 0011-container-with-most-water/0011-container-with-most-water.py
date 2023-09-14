class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_val = 0
        i,j = 0, len(height)-1
        
        while i < j:
            l = min(height[i], height[j])
            w = j-i
            max_val = max(max_val, l*w)
            
            if height[i] <= height[j]:
                i+= 1
            else:
                j -= 1
        
        return max_val
        