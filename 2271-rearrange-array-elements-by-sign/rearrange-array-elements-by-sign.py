class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=1
        p=0
        l=len(nums)
        result=[0]*l
        for num in nums:
            if num>=0:
                result[p]=num
                p+=2
            else:
                result[n]=num
                n+=2
        return result
