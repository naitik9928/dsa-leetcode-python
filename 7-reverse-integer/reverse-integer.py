class Solution:
    def reverse(self, x: int) -> int:
        result=0
        num=abs(x)
        sign=1 if x>0 else -1

        while num!=0:
            last_digit=num%10
            result=result*10+last_digit
            num=num//10

        result=result*sign
        if result < -2**31 or result >2**31-1:
            return 0
        return result
