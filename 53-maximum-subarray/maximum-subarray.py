class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum=float("-inf")
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            if maximum<total:
                maximum=total
            if total<0:
                total=0
        return maximum