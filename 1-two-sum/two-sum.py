class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store={}
        result=[]
        for i in range(len(nums)):
            sub=target-nums[i]
            if sub in store:
                result.append(i)
                result.append(store[sub])
            else:
                store[nums[i]]=i
        return result