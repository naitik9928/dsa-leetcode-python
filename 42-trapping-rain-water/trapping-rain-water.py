class Solution:
    def trap(self, height: List[int]) -> int:
        left_max=[height[0]]*len(height)
        i=1
        water_stored=0
        right_max=[height[len(height)-1]]*len(height)
        j=len(height)-2
        while i<len(height):
            store=max(left_max[i-1],height[i])
            left_max[i]=store
            i+=1
        while j>=0:
            store=max(right_max[j+1],height[j])
            right_max[j]=store
            j-=1
        k=0
        while k<len(left_max):
            water_stored+=min(left_max[k],right_max[k])-height[k]
            k+=1
        return water_stored       