class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums)
        i,j=0,len(nums)-1
        k=len(nums)-1
        while i<=j:
            if nums[i]**2 >nums[j]**2:
                result[k]=nums[i]**2
                k-=1
                i+=1
            else:
                result[k]=nums[j]**2
                k-=1
                j-=1
        return result         