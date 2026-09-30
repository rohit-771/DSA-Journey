class Solution:
    def tribonacci(self, n: int) -> int:
        dp=[-1]*(n+1)
        def trib(i, dp):
            if i==0:
                return 0
            if i<=2:
                return 1
            if dp[i] != -1:
                return dp[i]
            dp[i] = trib(i-1, dp)+trib(i-2, dp)+trib(i-3, dp)
            return dp[i]
        return trib(n, dp)
            
