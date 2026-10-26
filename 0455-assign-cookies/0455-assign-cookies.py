class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n=len(g)
        m=len(s)
        i=0
        j=0
        c=0
        while i<n and j<m:
            if g[i]<=s[j]:
                c+=1
                i+=1
            j+=1
        return c
        
        