class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        store=[]
        n=len(nums)
        nums.sort()
        for review in range(0,n-2):
            i=review+1
            j=len(nums)-1
            if review>0 and nums[review-1] ==nums[review]:
                continue 
            
            while i<j:
                target=0-(nums[review])
                addition=nums[i]+nums[j]
                if addition==target:
                    store1=[]
                    store1.append(nums[review])
                    store1.append(nums[i])
                    store1.append(nums[j])
                    store.append(store1)
                    j-=1
                    i+=1
                    while i<j and nums[i]==nums[i-1]:
                        i+=1
                    while i<j and nums[j]==nums[j+1]:
                        j-=1
                elif addition<target:
                    i+=1
                else:
                    j-=1
            
        return store