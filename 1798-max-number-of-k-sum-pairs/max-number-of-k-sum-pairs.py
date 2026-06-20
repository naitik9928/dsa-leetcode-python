class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count=0
        i=0
        nums.sort()
        j=len(nums)-1
        while i<j:
            sum=nums[i]+nums[j]
            if sum==k:
                i+=1
                j-=1
                count+=1
            elif sum>k:
                j-=1
            else:
                i+=1
        return count