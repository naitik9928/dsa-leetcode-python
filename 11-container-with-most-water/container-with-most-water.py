class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        max_area=0
        while i<j:
            check=min(height[i],height[j])*(j-i)
            if check>max_area:
                max_area=check
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
            
        return max_area
            