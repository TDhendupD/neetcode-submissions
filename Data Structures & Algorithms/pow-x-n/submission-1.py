class Solution:
    def myPow(self, x: float, n: int) -> float:
        if (n==0):
            return 1
        ans = x
        flag = False
        if (n<0):
            n = n*-1
            flag = True
        for i in range(n-1):
            ans = ans * x
        if (flag == True):
            ans = 1/ans
        return ans