class Solution:
    def fib(self, n: int) -> int:
        if n==1:
            return 1
        if n==0:
            return 0
        store={}
        if n in store.keys():
            return store[n]
        result=self.fib(n-1)+self.fib(n-2)
        store[n]=result
        return result
        