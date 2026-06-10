class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        values=nums
        store={}
        count=0
        n=len(values)
        for i in range(0,n):
            store[values[i]]=store.get(values[i],0)+1
        max_value=max(store.values())
        dict_keys=[x for x in store.keys()]
        for i in dict_keys:  
            if max_value==store[i]:
                count+=1
        return count*max_value