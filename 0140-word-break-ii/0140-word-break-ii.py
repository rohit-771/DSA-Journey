class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n=len(s)
        res=[]
        curr=[]
        def fun(i):
            if i==n:
                res.append(" ".join(curr))
                return
            for j in range(i, n):
                temp=s[i:j+1]
                if temp in wordDict:
                    curr.append(temp)
                    fun(j+1)
                    curr.pop()
        fun(0)
        return res
    