class Solution:
    def findLucky(self, arr: list[int]) -> int:

        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        ans = -1

        for num in freq:
            if freq[num] == num:
                ans = max(ans, num)

        return ans
            