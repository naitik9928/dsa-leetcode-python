class Solution:
    def reverseString(self, s: List[str]) -> None:
        def reverse_helper(left:int,right:int)->None:
            if left>=right:
                return
            s[left],s[right]=s[right],s[left]
            reverse_helper(left+1,right-1)
        return reverse_helper(0,len(s)-1)
        