class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        check=nums1[:m]
        check1=nums2[:n]
        i,j=0,0
        k=0
        result=[]
        while i<len(check) and j<len(check1):
            if check[i]<=check1[j]:
                nums1[k]=check[i]
                k+=1
                i+=1
            else:
                nums1[k]=check1[j]
                k+=1
                j+=1
        if i<len(check):
            while i<len(check):
                nums1[k]=check[i]
                k+=1
                i+=1
        if j<len(check1):
            while j<len(check1):
                nums1[k]=check1[j]
                k+=1
                j+=1 
            