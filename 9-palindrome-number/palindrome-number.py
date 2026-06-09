class Solution:
    def isPalindrome(self, x: int) -> bool:
        result=0
        sign= 1 if x>0 else -1
        num=abs(x)
        while num!=0:
            last_digit=num%10
            result=result*10+last_digit
            num=num//10
        result=result*sign
        if result <=-2**31 or result>=2**31-1:
            return False

        if result<0 or result!=x:
            return False
        if result==x:
            return True
        

        