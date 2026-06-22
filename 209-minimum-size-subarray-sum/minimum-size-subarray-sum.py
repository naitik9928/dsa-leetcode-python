class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        minimum_len=float("inf")
        current_sum=0
        for right in range(len(nums)):
            current_sum+=nums[right]
            while current_sum>=target:
                minimum_len=min(minimum_len,right-left+1)
                current_sum-=nums[left]
                left+=1

        return 0 if minimum_len==float("inf") else minimum_len