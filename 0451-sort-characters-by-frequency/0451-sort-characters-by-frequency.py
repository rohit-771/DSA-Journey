class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for ch in s:
            freq[ch] = freq.get(ch, 0)+1

        arr=[]
        for ch , fr in freq.items():
            arr.append((fr, ch))
        
        arr.sort(reverse=True)

        temp=[]
        for fr, ch in arr:
            temp.append(ch*fr)
        return "".join(temp)