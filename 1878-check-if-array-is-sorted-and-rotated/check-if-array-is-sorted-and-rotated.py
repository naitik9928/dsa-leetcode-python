class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        
        for i in range(n):
            # Check if current > next (circular check)
            if nums[i] > nums[(i + 1) % n]:
                count += 1
            if count > 1:
                return False
        
        return True