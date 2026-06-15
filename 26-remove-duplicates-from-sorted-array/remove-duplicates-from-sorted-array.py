class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        space={}
        j=0
        for i in nums:
            if i not in space.values():
                space[j]=i
                j+=1
    
        extra=list(space.values())
        nums[0:len(extra)]=extra[0:len(extra)]
        return len(extra)
