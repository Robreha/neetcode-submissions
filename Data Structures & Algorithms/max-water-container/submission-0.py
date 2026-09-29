class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxArea= 0

        l= 0
        r = len(heights) - 1

        while (l<r):
            currArea = min(heights[l], heights[r]) * (r-l)
            if (maxArea < currArea):
                maxArea = currArea

            if (heights[r] == heights[l]):
                l+= 1
                r -=1
            elif (heights[r] < heights[l]): 
                r -=1
            else:
                l +=1

        return maxArea
        
            
            
                
