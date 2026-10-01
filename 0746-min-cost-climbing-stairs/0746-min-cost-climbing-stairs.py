class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n=len(cost)
        dp=[-1]*(n)
        def fun(i, dp):
            if i>=n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            dp[i] = cost[i]+min(fun(i+1, dp), fun(i+2, dp))

            return dp[i]
        return min(fun(0, dp), fun(1, dp))
        