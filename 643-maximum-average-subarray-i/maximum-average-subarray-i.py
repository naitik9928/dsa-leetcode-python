class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum_avg=float("-inf")
        current_sum=0
        i=1
        j=0
        while j<k:
            if j<k:
                current_sum+=nums[j]
                j+=1
        if current_sum>maximum_avg:
            maximum_avg=current_sum
        while i<=len(nums)-k:
            current_sum=current_sum-nums[i-1]+nums[i+(k-1)]
            i+=1
            if current_sum>maximum_avg:
                maximum_avg=current_sum
        return maximum_avg/k