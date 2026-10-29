class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        dict={}
        for ch in arr:
            if ch in dict:
                dict[ch]+=1
            else:
                dict[ch]=1
        l = []
        for ch, fr in dict.items():
            l.append((fr, ch))
        l.sort(reverse=True)

        removed=0
        ans=0
        for f, ele in l:
            ans+=1
            removed+=f
            if removed>=len(arr)/2:
                break
        return ans