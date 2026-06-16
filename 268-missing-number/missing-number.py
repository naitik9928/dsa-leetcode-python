class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        k=len(nums)
        k_sum=(k*(k+1))/2
        nums_sum=0
        for i in nums:
            nums_sum+=i
        if nums_sum==k_sum:
            return 0
        if nums_sum!=k_sum:
            return int(k_sum-nums_sum)