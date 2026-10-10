class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        words = s1.split() + s2.split()
        freq = {}

        for word in words:
            freq[word] = freq.get(word, 0) + 1

        ans = []

        for word in words:
            if freq[word] == 1:
                ans.append(word)
                freq[word] = 0

        return ans
        