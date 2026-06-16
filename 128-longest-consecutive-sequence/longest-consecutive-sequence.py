class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store=set(nums)
        max_len=0
        for num in store:
            if num-1 not in store:
                start=num
                length=1
                while start+1 in store:
                    length+=1
                    start+=1
                if max_len<length:
                    max_len=length
        return max_len