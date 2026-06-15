class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k%=n
        val=nums[n-k:]
        store=nums[:n-k]
        nums[:k]=val
        nums[k:]=store
        